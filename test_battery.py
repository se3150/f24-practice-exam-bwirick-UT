import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

def describe_Battery():

    def describe_recharge():
        def it_recharges_within_capacity(partially_charged_battery):
            partially_charged_battery.recharge(20)
            assert partially_charged_battery.getCharge() == 90
        
        def it_recharges_exceeding_capacity(partially_charged_battery):
            partially_charged_battery.recharge(50)
            assert partially_charged_battery.getCharge() == 100
        
        def it_recharges_negative_amount(charged_battery):
            result = charged_battery.recharge(-10)
            assert result is False
            assert charged_battery.getCharge() == 100
        
        def it_recharges_with_external_monitor(partially_charged_battery):
            mock_monitor = Mock()
            partially_charged_battery.external_monitor = mock_monitor
            partially_charged_battery.recharge(20)
            mock_monitor.notify_recharge.assert_called_with(90)

    def describe_drain():
        def it_drains_within_capacity(partially_charged_battery):
            partially_charged_battery.drain(20)
            assert partially_charged_battery.getCharge() == 50
        
        def it_drains_exceeding_charge(partially_charged_battery):
            partially_charged_battery.drain(100)
            assert partially_charged_battery.getCharge() == 0
        
        def it_drains_negative_amount(charged_battery):
            result = charged_battery.drain(-10)
            assert result is False
            assert charged_battery.getCharge() == 100
        
        def it_drains_with_external_monitor(partially_charged_battery):
            mock_monitor = Mock()
            partially_charged_battery.external_monitor = mock_monitor
            partially_charged_battery.drain(20)
            mock_monitor.notify_drain.assert_called_with(50)

