# Import standard python libraries
import sys, os, json

# Import module...
try:
    # ... if running tests from project root
    sys.path.append(".")
    from device.peripherals.modules.led_dac5578.manager import LEDDAC5578
except:
    # ... if running tests from same dir as events.py
    sys.path.append("../../../../")
    from device.peripherals.modules.led_dac5578.manager import LEDDAC5578

# Import device utilities
from device.utilities.modes import Modes

# Import shared memory
from device.state import State

# Set directory for file upload 
os.chdir("../../../../")

# Import test config
device_config = json.load(open("device/peripherals/modules/led_dac5578/tests/config.json"))
peripheral_config = device_config["peripherals"][0]

# Initialize state
state = State()


def test_init():
    led_manager = LEDDAC5578("Test", state, peripheral_config, simulate = True)


def test_turn_on():
    led_manager = LEDDAC5578("Test", state, peripheral_config, simulate = True)
    
    # Try to turn on outside manual mode
    led_manager.mode = Modes.NORMAL
    led_manager.process_event(
        request = {"type": "Turn On"}
    )
    assert led_manager.response["status"] == 400

    # Turn on from manual mode
    led_manager.mode = Modes.MANUAL
    led_manager.process_event(
        request = {"type": "Turn On"}
    )
    assert led_manager.response["status"] == 200


def test_turn_off():
    led_manager = LEDDAC5578("Test", state, peripheral_config, simulate = True)
    
    # Try to turn off outside manual mode
    led_manager.mode = Modes.NORMAL
    led_manager.process_event(
        request = {"type": "Turn Off"}
    )
    assert led_manager.response["status"] == 400

    # Turn off from manual mode
    led_manager.mode = Modes.MANUAL
    led_manager.process_event(
        request = {"type": "Turn Off"}
    )
    assert led_manager.response["status"] == 200
