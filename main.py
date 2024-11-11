import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config


async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
