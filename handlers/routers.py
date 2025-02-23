from utils.common import Routes
from handlers import add_remove_job
from handlers import commands

__routes__ = Routes(routers=(commands.router, add_remove_job.router))


