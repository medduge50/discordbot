import discord
import asyncio
import datetime
import os
import time
import random

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print('제작자:호떡#9460')
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    print('디스코드 봇이 실행되었습니다.')
    
   
   
@client.event
async def on_message(message):
    if message.content.startswith("/정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                        inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/help"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="[help]", value="자신의 정보를 알고싶다면 '/정보'쳐주세요!", inline=False)
        embed.add_field(name="[help]", value="/출근,/퇴근,/임시퇴근이 가능합니다!", inline=False)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/출근"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="[서버닉네임]", value=message.author.display_name, inline=False)
        embed.add_field(name="[id]", value=message.author.id, inline=False)
        embed.add_field(name="[출근]", value="출근하셨습니다.", inline=True)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/퇴근"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="[서버닉네임]", value=message.author.display_name, inline=False)
        embed.add_field(name="[id]", value=message.author.id, inline=False)
        embed.add_field(name="[퇴근]", value="퇴근하셨습니다.", inline=True)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/임시퇴근"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="[서버닉네임]", value=message.author.display_name, inline=False)
        embed.add_field(name="[id]", value=message.author.id, inline=False)
        embed.add_field(name="[임시퇴근]", value="임시퇴근하셨습니다.", inline=True)
        await message.channel.send(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run('access_token')