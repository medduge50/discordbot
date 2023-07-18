from discord.ext import tasks
import discord, datetime, pytz, os, requests, asyncio, pymysql, ctypes, sys, re
from discord_webhook import DiscordWebhook, DiscordEmbed

client = discord.Client()

@client.event
async def on_connect(): 
    print("안상현봇")
    game = discord.Game("응애") 
    await client.change_presence(status=discord.Status.online, activity=game)       

@client.event
async def on_message(message):   
    if message.content.startswith("쥐새키야 도움말"):
        embed = discord.Embed(title=f'쥐새키 도움말', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00FF00) 
        embed.add_field(name='쥐새키야 내정보보내', value=f"자신의 정보를 확인할수 있습니다.", inline=False)   
        embed.add_field(name='쥐새키야 정보알려줘 @태그', value=f"태그한사람의 정보를 확인할수 있습니다.", inline=False)      
        embed.add_field(name='쥐새키야 욕해줘', value=f"쥐새키의 욕", inline=False)      
        return await message.channel.send(embed=embed)  

    if message.content.startswith("쥐새키야 내정보보내"):
        embed = discord.Embed(title=f'쥐새키야 사용자 정보', description=f'```사용자 정보\n{message.author}({message.author.id})```', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00FF00) 
        return await message.channel.send(embed=embed)  
    
    if message.content.startswith("쥐새키야 욕해줘"):
        await message.channel.send(f"니얼굴 내얼굴 ㅋ")

    if message.content.startswith("쥐새키야 정보알려줘"):
        try:
            user = message.mentions[0]
        except:
            return await message.channel.send("유저를 맨션해주세요!! 쥐새키가 화를 낼수 있습니다.\n예시 (!업로더 @맨션 사용할 이모지)")
        embed = discord.Embed(title=f'쥐새키야 사용자 정보', description=f'```사용자 정보\n{user}({user.id})```', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00FF00) 
        return await message.channel.send(embed=embed)  

client.run("MTA4Njk5MzAzMzE1NDgwMTY4NQ.GNV0Ww.iGmNYKdS7veq5SZB-ueDEE2vykKSp1xjZKFBZQ")


