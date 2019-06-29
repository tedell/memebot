"""
MEMES FROM THE IMGFLIP API
"""

import aiohttp
from discord.ext import commands
from libs import macro


async def meme(id, *args):
    async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
        "template_id": id,
        "username": "meestr",
        "password": "yugignuf",
        "text0": args[0],
        "text1": args[1]
    }, ) as response:
        res = await response.json()
        url = res["data"]["url"]
        return url


class ImgFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='imgflip')
    async def imgflip(self, ctx):
        if not ctx.invoked_subcommand:
            await ctx.send(embed=await macro.send("""``futurama``, ``notsimply``, ``aliens``, ``mocking``, 
            ``skeleton``, ``200iq``, ``condescending``, ``facepalm``, ``success``, ``squidward``, ``evil``, 
            ``imagination``, ``society``"""))

    @imgflip.command(name='futurama')
    async def futurama(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(61520, args)))

    @imgflip.command(name='notsimply')
    async def notsimply(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(61579, args)))

    @imgflip.command(name='aliens')
    async def aliens(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(101470, args)))

    @imgflip.command(name='mocking')
    async def mocking(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(102156234, args)))

    @imgflip.command(name='skeleton')
    async def skeleton(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(4087833, args)))

    @imgflip.command(name='200iq')
    async def iq(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(89370399, args)))

    @imgflip.command(name='condescending')
    async def condescending(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(61582, args)))

    @imgflip.command(name='facepalm')
    async def facepalm(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(1509839, args)))

    @imgflip.command(name='success')
    async def success(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(61544, args)))

    @imgflip.command(name='squidward')
    async def squidward(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(101511, args)))

    @imgflip.command(name='evil')
    async def evil(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(235589, args)))

    @imgflip.command(name='imagination')
    async def imagination(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(163573, args)))

    @imgflip.command(name='society', aliases=['joker'])
    async def joker(self, ctx, *args):
        assert len(args) == 2, "Invalid length. Should be 2 text bodies."
        await ctx.send(embed=await macro.img(meme(1790995, args)))


def setup(bot):
    bot.add_cog(ImgFlip(bot=bot))
