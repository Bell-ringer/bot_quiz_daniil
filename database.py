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
                        "database": "d2c4gv7boohhj7",
                        "host": "ec2-176-34-211-0.eu-west-1.compute.amazonaws.com",
                        "password": "771798453e6550bb74ffe3f3d386b9de2ac0183c66d2b3d729ac4fb93591bbaa",
                        "port": 5432,
                        "user": "blaehfiylzuywc"
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
