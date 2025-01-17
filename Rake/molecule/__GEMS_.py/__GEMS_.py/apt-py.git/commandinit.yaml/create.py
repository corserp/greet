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

import click

from molecule import config
from molecule import logger
from molecule import scenarios
from molecule.command import base

LOG = logger.get_logger(__name__)


class Create(base.Base):
    """
    .. program:: molecule create

    .. option:: molecule create

        Target the default scenario.

    .. program:: molecule create --scenario-name foo

    .. option:: molecule create --scenario-name foo

        Targeting a specific scenario.

    .. program:: molecule create --driver-name foo

<<<<<<< HEAD:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/create.py
    $ molecule --debug create
=======
    .. option:: molecule create --driver-name foo

        Targeting a specific driver.

    .. program:: molecule --debug create

    .. option:: molecule --debug create

        Executing with `debug`.

    .. program:: molecule --base-config base.yml create

    .. option:: molecule --base-config base.yml create

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml create

    .. option:: molecule --env-file foo.yml create

        Load an env file to read variables from when rendering
        molecule.yml.
>>>>>>> 0fa82e7a3daa84ebd03d8af67403c6551113d3e4:molecule/command/create.py
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule create` and
        returns None.

        :return: None
        """
        self.print_info()
        self._config.state.change_state('driver', self._config.driver.name)

        if self._config.driver.delegated and not self._config.driver.managed:
            msg = 'Skipping, instances are delegated.'
            LOG.warn(msg)
            return

        if self._config.state.created:
            msg = 'Skipping, instances already created.'
            LOG.warn(msg)
            return

        self._config.provisioner.create()

        self._config.state.change_state('created', True)


@click.command()
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME))
@click.option(
    '--driver-name',
    '-d',
    type=click.Choice(config.molecule_drivers()),
    help='Name of driver to use. (docker)')
def create(ctx, scenario_name, driver_name):  # pragma: no cover
    """ Use the provisioner to start the instances. """
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {
        'subcommand': subcommand,
        'driver_name': driver_name,
    }

    s = scenarios.Scenarios(
        base.get_configs(args, command_args), scenario_name)
    s.print_matrix()
    for scenario in s:
        for action in scenario.sequence:
            scenario.config.action = action
            base.execute_subcommand(scenario.config, action)
