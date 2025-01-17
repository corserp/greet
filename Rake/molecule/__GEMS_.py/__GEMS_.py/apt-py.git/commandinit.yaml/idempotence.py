#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import re

import click

from molecule import logger
from molecule import scenarios
from molecule import util
from molecule.command import base

LOG = logger.get_logger(__name__)


class Idempotence(base.Base):
    """
<<<<<<< HEAD:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/idempotence.py
    Target the default scenario:
=======
    Runs the converge step a second time. If no tasks will be marked as changed
    the scenario will be considered idempotent.

    .. program:: molecule idempotence
>>>>>>> 0fa82e7a3daa84ebd03d8af67403c6551113d3e4:molecule/command/idempotence.py

    .. option:: molecule idempotence

        Target the default scenario.

    .. program:: molecule idempotence --scenario-name foo

    .. option:: molecule idempotence --scenario-name foo

<<<<<<< HEAD:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/idempotence.py
    $ molecule --debug idempotence
=======
        Targeting a specific scenario.

    .. program:: molecule --debug idempotence

    .. option:: molecule --debug idempotence

        Executing with `debug`.

    .. program:: molecule --base-config base.yml idempotence

    .. option:: molecule --base-config base.yml idempotence

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml idempotence

    .. option:: molecule --env-file foo.yml idempotence

        Load an env file to read variables from when rendering
        molecule.yml.
>>>>>>> 0fa82e7a3daa84ebd03d8af67403c6551113d3e4:molecule/command/idempotence.py
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule idempotence` and
        returns None.

        :return: None
        """
        self.print_info()
        if not self._config.state.converged:
            msg = 'Instances not converged.  Please converge instances first.'
            util.sysexit_with_message(msg)

        output = self._config.provisioner.converge(out=None, err=None)

        idempotent = self._is_idempotent(output)
        if idempotent:
            msg = 'Idempotence completed successfully.'
            LOG.success(msg)
        else:
            msg = ('Idempotence test failed because of the following tasks:\n'
                   '{}').format('\n'.join(self._non_idempotent_tasks(output)))
            util.sysexit_with_message(msg)

    def _is_idempotent(self, output):
        """
        Parses the output of the provisioning for changed and returns a bool.

        :param output: A string containing the output of the ansible run.
        :return: bool
        """

        # Remove blank lines to make regex matches easier
        output = re.sub(r'\n\s*\n*', '\n', output)

        # Look for any non-zero changed lines
        changed = re.search(r'(changed=[1-9][0-9]*)', output)

        if changed:
            # Not idempotent
            return False

        return True

    def _non_idempotent_tasks(self, output):
        """
        Parses the output to identify the non idempotent tasks.

        :param (str) output: A string containing the output of the ansible run.
        :return: A list containing the names of the non idempotent tasks.
        """
        # Remove blank lines to make regex matches easier.
        output = re.sub(r'\n\s*\n*', '\n', output)

        # Remove ansi escape sequences.
        output = util.strip_ansi_escape(output)

        # Split the output into a list and go through it.
        output_lines = output.split('\n')
        res = []
        task_line = ''
        for _, line in enumerate(output_lines):
            if line.startswith('TASK'):
                task_line = line
            elif line.startswith('changed'):
                host_name = re.search(r'\[(.*)\]', line).groups()[0]
                task_name = re.search(r'\[(.*)\]', task_line).groups()[0]
                res.append('* [{}] => {}'.format(host_name, task_name))

        return res


@click.command()
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME))
def idempotence(ctx, scenario_name):  # pragma: no cover
    """
    Use the provisioner to configure the instances and parse the output to
    determine idempotence.
    """
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {
        'subcommand': subcommand,
    }

    s = scenarios.Scenarios(
        base.get_configs(args, command_args), scenario_name)
    s.print_matrix()
    for scenario in s:
        for action in scenario.sequence:
            scenario.config.action = action
            base.execute_subcommand(scenario.config, action)
