from utils.common import Routes
from .handlers import commands, add_db

__routes__ = Routes(routers=(commands.router, add_db.router))


