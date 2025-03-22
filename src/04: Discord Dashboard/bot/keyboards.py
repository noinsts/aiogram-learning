from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder


def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Кількість учасників на сервері',
        callback_data="get_member_count"
    )

    builder.button(
        text='Кількість онлайн учасників',
        callback_data="get_online_member_count"
    )

    builder.button(
        text='Кількість учасників в войсах',
        callback_data="get_invoice_member_count"
    )

    return builder.as_markup()
