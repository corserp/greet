# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of GitDB and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
from base import (
                    CompoundDB,
                )

import os
__all__ = ('ReferenceDB', )

class ReferenceDB(CompoundDB):
    """A database consisting of database referred to in a file"""
    
    # Configuration
    # Specifies the object database to use for the paths found in the alternates
    # file. If None, it defaults to the GitDB
    ObjectDBCls = None
    
    def __init__(self, ref_file):
        super(ReferenceDB, self).__init__()
        self._ref_file = ref_file
        
    def _set_cache_(self, attr):
        if attr == '_dbs':
            self._dbs = list()
            self._update_dbs_from_ref_file()
        else:
            super(ReferenceDB, self)._set_cache_(attr)
        # END handle attrs
        
    def _update_dbs_from_ref_file(self):
        dbcls = self.ObjectDBCls
        if dbcls is None:
            # late import
            from git import GitDB
            dbcls = GitDB
        # END get db type
        
        # try to get as many as possible, don't fail if some are unavailable
        ref_paths = list()
        try:
            ref_paths = [l.strip() for l in open(self._ref_file, 'r').readlines()]
        except (OSError, IOError):
            pass
        # END handle alternates
        
        ref_paths_set = set(ref_paths)
        cur_ref_paths_set = set(db.root_path() for db in self._dbs)
        
        # remove existing
        for path in (cur_ref_paths_set - ref_paths_set):
            for i, db in enumerate(self._dbs[:]):
                if db.root_path() == path:
                    del(self._dbs[i])
                    continue
                # END del matching db
        # END for each path to remove
        
        # add new
        # sort them to maintain order
        added_paths = sorted(ref_paths_set - cur_ref_paths_set, key=lambda p: ref_paths.index(p))
        for path in added_paths:
            try:
                db = dbcls(path)
                # force an update to verify path
                if isinstance(db, CompoundDB):
                    db.databases()
                # END verification
                self._dbs.append(db)
            except Exception as e:
                # ignore invalid paths or issues
                pass
        # END for each path to add
        
    def update_cache(self, force=False):
        # re-read alternates and update databases
        self._update_dbs_from_ref_file()
        return super(ReferenceDB, self).update_cache(force)