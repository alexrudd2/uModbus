from logging import NullHandler, getLogger

log = getLogger('uModbus')
log.addHandler(NullHandler())

from .config import Config  # NOQA
conf = Config()
