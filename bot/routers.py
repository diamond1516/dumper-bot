from utils.common import Routes
from .handlers import commands, add_remove_job

__routes__ = Routes(routers=(commands.router, add_db.router))


