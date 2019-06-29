import discord


class Macro:
    @staticmethod
    async def msg(desc=None, title=None, color: discord.Color = discord.Color.purple()):
        embed = discord.Embed(
            type='rich',
            description=desc,
            title=title,
            color=color
        )

    @classmethod
    async def img(cls, image: str, desc: str = None, title: str = None):
        message = await cls.msg(desc=desc, title=title)
        message.set_image(url=image)
        return message

    @classmethod
    async def error(cls, desc: str = None, title: str = None):
        return await cls.msg(desc=desc, title=title,
                             color=discord.Color.red())


err, error = Macro.error, Macro.error
send = Macro.msg, Macro.msg
img = Macro.img, Macro.img
