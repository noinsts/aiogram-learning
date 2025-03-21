import aiohttp


class ExchangeAPI:
    BASE_URL = "https://api.exchangerate.host/latest"

    """
    Потрібно передати API KEY
    або змінити апі
    """

    async def get_exchange_rate(self, currency='USD'):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}?base=UAH') as response:
                if response.status != 200:
                    return f"Помилка API: {response.status}"

                data = await response.json()

                if "rates" not in data:
                    return "Немає даних про курси валют"

                return data["rates"].get(currency.upper(), "Немає даних")
