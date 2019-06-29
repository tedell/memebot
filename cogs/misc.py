"""
MISCELLANEOUS MEMES
"""

import aiohttp
from discord.ext import commands
from libs import macro


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send("""``Do m!imgflip for imgflip command``, ``buttons``, ``brain``, ``boyfriend``, ``threats``, 
        ``clyde``, ``trump``, ``jpeg``, ``changemymind``, ``whowouldwin``, ' '``phcomment``, ``fact``, ``captcha``, 
        ``iphonex``, ``deepfry``, ``magik``, ``trash``' """)

    @commands.command(name="brain")
    async def brain(self, ctx, *args):
        assert len(args) == 4, "Invalid length, should be 4 bodies of text."
        async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
            "template_id": 93895088,
            "username": "meestr",
            "password": "yugignuf",
            "text0": args[0],
            "text1": args[1],
            "text2": args[2],
            "text3": args[3]
        }, ) as response:
            res = await response.json()
            url = res["data"]["url"]
            return ctx.send(embed=await macro.img(url))

    @commands.command(name="distracted")
    async def boyfriend(self, ctx, *args):
        assert len(args) == 3, "Invalid length, should be 3 bodies of text."
        async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
            "template_id": 112126428,
            "username": "meestr",
            "password": "yugignuf",
            "text0": args[0],
            "text1": args[1],
            "text2": args[2],
        }, ) as response:
            res = await response.json()
            url = res["data"]["url"]
            return ctx.send(embed=await macro.img(url))

    @commands.command(name="buttons")
    async def button(self, ctx, *args):
        assert len(args) == 3, "Invalid length, should be 3 bodies of text."
        async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
            "template_id": 87743020,
            "username": "meestr",
            "password": "yugignuf",
            "text0": args[0],
            "text1": args[1],
            "text2": args[2],
        }, ) as response:
            res = await response.json()
            url = res["data"]["url"]
            return ctx.send(embed=await macro.img(url))

    @commands.command(name="nut")
    async def nutbutton(self, ctx, *args):
        assert len(args) == 1, "Invalid length, should be 1 bodies of text."
        async with aiohttp.request(method="POST", url="https://api.imgflip.com/caption_image", params={
            "template_id": 119139145,
            "username": "meestr",
            "password": "yugignuf",
            "text0": args[0]
        }, ) as response:
            res = await response.json()
            url = res["data"]["url"]
            return ctx.send(embed=await macro.img(url))


def setup(bot):
    bot.add_cog(Misc(bot))
