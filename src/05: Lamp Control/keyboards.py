from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text = 'Ввімкнути лампу',
        callback_data = 'turn_on_lamp'
    )

    builder.button(
        text = 'Яркість лампи 20%',
        callback_data = 'brightness_20'
    )

    builder.button(
        text = 'Вимкнути лампу',
        callback_data = 'turn_off_lamp'
    )

    builder.button(
        text = 'Яркість лампи 50%',
        callback_data = 'brightness_50'
    )

    builder.button(
        text = 'Яркість лампи 100%',
        callback_data = 'brightness_100'
    )

    builder.adjust(2)

    return builder.as_markup()
