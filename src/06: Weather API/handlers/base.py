from abc import ABC, abstractmethod
from aiogram import Router
from db.database import Database


class BaseHandler(ABC):
    def __init__(self):
        self.router = Router()
        self.db = Database()

    @abstractmethod
    def register_handlers(self):
        pass
