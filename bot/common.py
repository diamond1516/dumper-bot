from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass
from typing import Tuple
from aiogram import Bot, Dispatcher


class BallsCallbackFactory(CallbackData, prefix="ball"):
    color: str


@dataclass(frozen=True)
class Routes:
    routers: Tuple

    def register_routes(self, dp: Dispatcher):
        for router in self.routers:
            dp.include_router(router)
