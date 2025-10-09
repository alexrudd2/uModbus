import pytest
from serial import serial_for_url

from umodbus.client.serial.rtu import read_coils, send_message


def test_send_message_with_timeout():
    """ Test if TimoutError is raised when serial port doesn't receive enough
    data.
    """
    s = serial_for_url('loop://', timeout=0)
    # As we are using a loop, the sent request will be read back as response.
    # To test timeout use a request that needs more bytes for the response.
    message = read_coils(slave_id=0, starting_address=1, quantity=40)

    with pytest.raises(ValueError):  # noqa: PT011
        send_message(message, s)
