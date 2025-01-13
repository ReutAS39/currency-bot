import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

# Получаем параметры для загрузки переменных среды
settings = Settings()



currencys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}


'''currencys = {
    'биткоин': 'BTC',
    'доллар': 'USD',
    'эфириум': 'ETH',
}'''
