<<<<<<< HEAD
<<<<<<< HEAD
********
=======
.. image:: https://cloud.githubusercontent.com/assets/9895/11250011/11e827d0-8ddf-11e5-80f5-259036d868c2.png
=======
.. image:: ./molecule.png
>>>>>>> initial commit
   :align: center
   :height: 100px
   :width: 200 px
   :scale: 50 %

<<<<<<< HEAD
>>>>>>> Having our image hosted on GH CDN vs repo
Molecule
********

.. image:: https://badge.fury.io/py/molecule.svg
   :target: https://badge.fury.io/py/molecule
   :alt: PyPI Package

.. image:: https://readthedocs.org/projects/molecule/badge/?version=latest
   :target: https://molecule.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository License

Molecule is designed to aid in the development and testing of `Ansible`_ roles.
Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios.  Molecule is opinionated in order to encourage an approach
that results in consistently developed roles that are well-written, easily
understood and maintained.

Molecule uses `Ansible`_ `playbooks`_ to exercise the `role`_ and its
associated tests.  Molecule supports any provider [#]_ that `Ansible`_
supports.

.. [#]

   Providers can be bare-metal, virtual, cloud or containers.  If Ansible can
   use it, Molecule can test it.  Molecule simply leverages Ansible's module
   system to manage instances.

.. _`playbooks`: https://docs.ansible.com/ansible/playbooks.html
.. _`role`: http://docs.ansible.com/ansible/playbooks_roles.html

Quick Start
===========

Installing
----------

.. image:: https://asciinema.org/a/161970.png
   :target: https://asciinema.org/a/161970?speed=5&autoplay=1&loop=1
   :alt: Installing

Creating a new role
-------------------

.. image:: https://asciinema.org/a/161976.png
   :target: https://asciinema.org/a/161976?speed=5&autoplay=1&loop=1
   :alt: Creating a new role

Testing a new role
-------------------

.. image:: https://asciinema.org/a/161977.png
   :target: https://asciinema.org/a/161977?speed=5&autoplay=1&loop=1
   :alt: Testing a new role

Testing an existing role
------------------------

.. image:: https://asciinema.org/a/AkQ4KhxuGAxwn1YJX3tM5BZld.png
   :target: https://asciinema.org/a/AkQ4KhxuGAxwn1YJX3tM5BZld?speed=5&autoplay=1&loop=1
   :alt: Testing an existing role

Docker in Docker
----------------

.. image:: https://asciinema.org/a/172713.png
   :target: https://asciinema.org/a/172713?speed=5&autoplay=1&loop=1
   :alt: Testing an existing role

Documentation
=============

https://molecule.readthedocs.io/

Contact
=======

IRC
---

Join us in the #molecule-users channel on `freenode`_.

.. _`freenode`: https://freenode.net

Forums
------

* `molecule-users`_
* `molecule-dev`_

.. _`molecule-users`: https://groups.google.com/forum/#!forum/molecule-users
.. _`molecule-dev`: https://groups.google.com/forum/#!forum/molecule-dev

Ansible Support
===============

Molecule requires Ansible version 2.2 or later.

.. _`Ansible`: https://docs.ansible.com

License
=======

`MIT`_

.. _`MIT`: https://github.com/metacloud/molecule/blob/master/LICENSE

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.
If you have some other use in mind, contact us.
=======
Molecule
========

Molecule is designed to aid in the development and testing of
`Ansible`_ roles including support for multiple instances, 
operating system distributions, virtualization providers and test frameworks.

It leverages `Vagrant`_ to manage virtual machines,
with support for multiple Vagrant providers (currently VirtualBox and OpenStack).
Molecule supports `Serverspec`_ or `Testinfra`_ to run tests.  Molecule uses an `Ansible`_
`playbook`_ (``playbook.yml``), to execute the `role`_ and its tests.

.. _`Ansible`: https://docs.ansible.com
.. _`Vagrant`: http://docs.vagrantup.com/v2
.. _`Test Kitchen`: http://kitchen.ci
.. _`playbook`: https://docs.ansible.com/ansible/playbooks.html
.. _`role`: http://docs.ansible.com/ansible/playbooks_roles.html
.. _`Serverspec`: http://serverspec.org
.. _`Testinfra`: http://testinfra.readthedocs.org

Documentation
-------------

The documentation is built with ``Sphinx`` and uses the ``bootswatch``
theme ``flatly``.

.. code-block:: bash

  $ tox -e docs

License
-------

MIT

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.  If you have some other use in mind, contact us.
>>>>>>> initial commit

.. _`Creative Commons NoDerivatives 4.0 License`: https://creativecommons.org/licenses/by-nd/4.0/
