import discord
import random
import asyncio
import requests
from config import get_token
from discord.ext.commands import Cog

token = get_token(2)
url = get_token(3)
auth = f'{token}'
head = {'Authorization': 'Brarer' + auth}


def get_players():
    res = requests.get(url, headers=head)
    players = res.json()['data']['attributes']['players']
    return players


class PlayersInformation(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Battlemetric is online')
        while True:
            status_type = random.randint(0, 1)
            if status_type == 0:
                players = get_players()
                print(players)
                await self.bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Activity(type=discord.ActivityType.watching, name=f"ผู้รอดชีวิต {players}/20 คน"))
            else:
                players = get_players()
                print(players)
                await self.bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Activity(type=discord.ActivityType.watching, name=f'ผู้รอดชีวิต {players}/20 คน'))
            await asyncio.sleep(45)


def setup(bot):
    bot.add_cog(PlayersInformation(bot))
