import asyncio
from tortoise import Tortoise, fields
from tortoise.models import Model

# Классы ORM


class Situations(Model):
    id = fields.BigIntField(pk=True)
    situation = fields.IntField()
    text = fields.TextField()
    answer = fields.TextField()
    score = fields.IntField()

    class Meta:
        table = "situations"


# Инициализация базы данных
async def run():
    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": "postgres",
                        "host": "localhost",
                        "password": "postgres",
                        "port": 5432,
                        "user": "postgres"
                    }
                }
            },
            "apps": {
                "models": {
                    "models": ["database"],
                    "default_connection": "default",
                }
            },
        }
    )
    await Tortoise.generate_schemas()


async def loop_db():
    loop = asyncio.get_event_loop()
    loop.create_task(run())
