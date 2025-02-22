from utils.common import Routes
from .handlers import commands, callbacks

__routes__ = Routes(routers=(commands.router, callbacks.router))


