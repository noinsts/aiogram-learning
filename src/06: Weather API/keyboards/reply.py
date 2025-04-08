from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .base import BaseKeyboard


class MainMenuKeyboard(BaseKeyboard):
    def get_keyboard(self):
        kb = [
            [KeyboardButton(text='🗒️ Допомога')],
            [KeyboardButton(text='🏙️ Додати місто')]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
