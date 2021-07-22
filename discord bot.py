import discord, asyncio, random, youtube_dl



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("게임")
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message, discord=None):
    if message.content.startswith("/입장"):
        await message.author.voice.channel.connect()
        await message.channel.send("채널에 입장합니다.")

    if message.content.startswith("/퇴장"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        await voice.disconnect()
        await message.channel.send("채널에 퇴장합니다.")

    if message.content.startswith("/재생"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        url = message.content.split(" ")[1]
        option = {
            'outtmpl' : "file/" + url.split('=')[1] + ".mp3"
        }

        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url, download=False)
            title = info["title"]

        voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3"))
        await message.channel.send(title + "을 재생합니다")



    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("👋")

    if message.content.startswith("몇살이니"):
        await message.channel.send("ㅋ")

    if message.content.startswith("잔다"):
        await message.channel.send("굿나잇")

    if message.content.startswith("우하하하"):
        await message.channel.send("빵빠레")

    if message.content.startswith("닭이 옷을 입을때 내는 소리는?"):
        await message.channel.send("꼭끼오")

    if message.content.startswith("세상에서 가장 착한사자는?"):
        await message.channel.send("자원봉사자")

    if message.content.startswith("토끼털을 빗어주는 빗은?"):
        await message.channel.send("래빗")

    if message.content.startswith("미안한 동물은?"):
        await message.channel.send("오소리")

    if message.content.startswith("오이가 도망가면?"):
        await message.channel.send("오...이런")

    if message.content.startswith("잉"):
        await message.channel.send("기모링")

    if message.content.startswith("헤이 자비스"):
        await message.channel.send("yes master")

    if message.content.startswith("헤이 JARVIS"):
        await message.channel.send("yes master")

    if message.content.startswith("hey JARVIS"):
        await message.channel.send("yes master")

    if message.content.startswith("hey jarvis"):
        await message.channel.send("yes master")

    if message.content.startswith("ㅇㅇㄴㅇ"):
        await message.channel.send("응 니얼굴")

    if message.content.startswith(".짤"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("용가리"):
        await message.channel.send("🐉")

    if message.content.startswith("야"):
        await message.channel.send("왜")

    if message.content.startswith("랜덤"):
        for i in range(1, 5):
            await message.channel.send(random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9']))

    if message.content.startswith("10초 타이머"):
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났습니다")

    if message.content.startswith("투명댓글"):
        await message.channel.send("﻿")

client.run("ODQxOTUxNjczMjE5OTQwMzYz.YJuOmQ.HiRIUOERxkQRgocqp2aMN1bUa4s")