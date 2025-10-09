import pytest

from umodbus import conf
from umodbus.config import Config


@pytest.fixture(scope='module', autouse=True)
def enable_signed_values(request):
    """ Use signed values when running tests it this module. """
    tmp = conf.SIGNED_VALUES
    conf.SIGNED_VALUES = False

    try:
        yield
    finally:
        conf.SIGNED_VALUES = tmp


@pytest.fixture
def config():
    return Config()
