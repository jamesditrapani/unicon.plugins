
__author__ = "Sritej K V R <skanakad@cisco.com>"

from unicon.bases.routers.connection import BaseSingleRpConnection
from unicon.bases.routers.connection import BaseDualRpConnection

from unicon.plugins.iosxr import service_implementation as svc
from unicon.plugins.iosxe.service_implementation import Ping as IosXePing


from unicon.plugins.iosxr.spitfire.statemachine import SpitfireSingleRpStateMachine,SpitfireDualRpStateMachine
from unicon.plugins.iosxr.spitfire.connection_provider import SpitfireSingleRpConnectionProvider,SpitfireDualRpConnectionProvider
from unicon.plugins.iosxr.spitfire.settings import SpitfireSettings


from unicon.plugins.generic import ServiceList,HAServiceList

class SpitfireServiceList(ServiceList):
    def __init__(self):
        super().__init__()
        self.configure = svc.Configure
        self.attach_console = svc.AttachModuleConsole
        self.bash_console = svc.BashService
        self.ping = IosXePing

class SpitfireHAServiceList(HAServiceList):
    """ Generic dual rp services. """
    def __init__(self):
        super().__init__()
        self.execute = svc.HAExecute
        self.configure= svc.HaConfigureService
        self.switchover = svc.Switchover
        self.bash_console = svc.BashService

class SpitfireSingleRpConnection(BaseSingleRpConnection):
    os = 'iosxr'
    series = 'spitfire'
    chassis_type = 'single_rp'
    state_machine_class = SpitfireSingleRpStateMachine
    connection_provider_class = SpitfireSingleRpConnectionProvider
    subcommand_list = SpitfireServiceList
    settings = SpitfireSettings()

class SpitfireDualRpConnection(BaseDualRpConnection):
    os = 'iosxr'
    series = 'spitfire'
    chassis_type = 'dual_rp'
    state_machine_class = SpitfireDualRpStateMachine
    connection_provider_class = SpitfireDualRpConnectionProvider
    subcommand_list = SpitfireHAServiceList
    settings = SpitfireSettings()