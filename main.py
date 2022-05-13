import asyncio
from bot import MyBot
import root


async def main():
    await MyBot.run_bot()


if __name__ == '__main__':
    asyncio.run(main())
