import discord
import re
from discord.ext import commands

TOKEN = 'MTMzODU0OTI0NzUzNjEzNjIwMg.GsLiBV.Uib4w9gZtRuvc1PBEL3Am024VEqRVjas680D74'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='#', intents=intents)
 
# @bot.event
# async def on_ready():
#     print(f'Login bot: {bot.user}')
 
# @bot.command()
# async def hello(message):
#     await message.channel.send('Hi!')

@client.event
async def on_message(message):

    if ":emoji_" in message.content: 
        if message.content.count(":emoji_") > 1: return # 하나 이상의 이모지 거르기
        
        # 이미지 링크
        description = message.content
        emoji = re.findall(r':emoji_[^:]+:', message.content)[0]
        emoji = re.sub(":", "", emoji)
        emoji = re.sub("emoji_", "", emoji)
        url = "https://i.imgur.com/" + emoji + ".png"

        # if ":emoji_hak:" in message.content: url = "https://imgur.com/xgRGNDb.png"
        # elif ":emoji_arca:" in message.content: url = "https://imgur.com/O5sv6jt.png"

        # 닉네임
        author = message.author.display_name
        # 임베드 색상
        color = 0xD3B69C
        if author == "다당": color = 0xc8895b
        # 아바타
        User = await client.fetch_user(message.author.id)
        avatar = message.author.display_avatar

        # 다른 메세지
        description = re.sub(r':emoji_[^:]+:', "", description)
        description = re.sub(r'<\d+>\s*', "", description)
        
        # 임베드 구성
        embed = discord.Embed(description=description, color=color)
        embed.set_author(name=author)
        embed.set_thumbnail(url=avatar)
        embed.set_image(url=url)

        # 메시지 보내기
        await message.channel.send(embed=embed)
        await message.delete()

    # for reaction in message.reactions:  # 이모지를 확인합니다.
    #     print(0)
    #     if reaction.custom_emoji:  # 커스텀 이모지인 경우
    #         print(1)
    #         emoji_url = reaction.emoji.url
    #         response = requests.get(emoji_url)
    #         img = Image.open(BytesIO(response.content))
    #         # 이미지를 128x128 이상으로 조정합니다.
    #         if img.size[0] < 128 or img.size[1] < 128:
    #             img = img.resize((128, 128))
    #         await message.channel.send(file=discord.File(fp=BytesIO(img.tobytes()), filename="resized.png"))
    #     else:  # 기본 이모지인 경우
    #         print(2)
    #         emoji_url = f"https://cdn.discordapp.com/emojis/{reaction.emoji.id}.png?v=1"
    #         response = requests.get(emoji_url)
    #         await message.channel.send(file=discord.File(fp=BytesIO(response.content), filename="resized.png"))

# bot.run(TOKEN)
client.run(TOKEN)

# import discord
# import requests
# from io import BytesIO
# from PIL import Image

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# TOKEN = 'MTA4NjU0Nzg5NzI1ODA5MDYzNw.GHPF9E.Yekn3WnzBpo_wSvKtQsAfModX0Aa2YUFVZS6zA'

# @client.event
# async def on_message(message):
#     if message.author == client.user:  # 봇이 보낸 메시지는 무시합니다.
#         return

#     if len(message.attachments) > 0:  # 첨부파일을 확인합니다.
#         for attachment in message.attachments:
#             if attachment.url.endswith('.png') or attachment.url.endswith('.jpg') or attachment.url.endswith('.jpeg'):
#                 # URL에서 이미지를 가져옵니다.
#                 response = requests.get(attachment.url)
#                 img = Image.open(BytesIO(response.content))

#                 # 이미지를 128x128 이상으로 조정합니다.
#                 if img.size[0] < 128 or img.size[1] < 128:
#                     img = img.resize((128, 128))
#                 await message.channel.send(file=discord.File(fp=BytesIO(img.tobytes()), filename="resized.png"))
#                 return  # 첨부파일 하나에 대해서만 처리합니다.

# client.run(TOKEN)
