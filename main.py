import discord
from discord.ext import commands
from discord import *
import datetime
import pytz
import time

INTENTS = Intents.all()
bot = commands.Bot(command_prefix = "/",intents=INTENTS)

TOKEN = "MTExMjY0MzI5OTIzNzQ0NTYzMg.Gn8Tny.0tMrR8h7knJvXUagiLCejGHflv4JeWH1MQMuw4" # 봇 토큰
allotment = [] # 배정 시스템 리스트

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("봇 상태메시지"))
    print("Ready!")

@bot.command(name="차단", description="관리자 전용 명령어 입니다.")
async def ban(ctx, user : discord.Member = None, reason = "사유가 없습니다."):
  permission = ctx.author.guild_permissions.ban_members
  if not ctx.guild:
    err = "해당 명령어는 서버에서만 사용하실수 있어요!"
  elif permission is False:
    err = "당신은 권한이 없습니다!"
  elif user == None:
    err = "차단할 유저를 입력해주세요!"
  elif user.id == ctx.author.id:
    err = "자기 자신을 킥할수 없어요!"
  elif user.guild_permissions.administrator:
    err = "관리자 권한을 가진 사람은 차단 할수 없어요!"
  else:
    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**🚫 유저 차단 안내**", color=0xFFFD05)
    embed.add_field(name="담당 관리자", value=f"{ctx.author.mention} ( {ctx.author} )", inline=False)
    embed.add_field(name="차단 대상자", value=f"{user.mention} ( {user} )", inline=False)
    embed.add_field(name="차단 사유", value=f"```cs\n# {reason}```", inline=False)
    embed.set_footer(text=f"제작 : 스텔#1476")
    #embed.set_thumbnail(url=user.avatar_url)
    await user.send(embed=embed)
    await user.ban(reason=reason)
    return await ctx.send(embed=embed)

  embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**차단 명령어 오류**", description=f"{err}",color=0xff0000)
  await ctx.reply(embed=embed)

@bot.command(name="차단해제", description="관리자 전용 명령어 입니다.")
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, user : discord.Member = None):
    try:
        if id == None:
            embed = discord.Embed(title="**차단 해제 명령어 오류**", description="\❌ 유저가 지정되지 않았습니다.", color=0XDF05FF)
        user = await bot.fetch_user(user)
        await ctx.guild.unban(user)
        embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**🚫 유저 차단 해제 안내**", color = 0XDF05FF)
        embed.add_field(name="담당 관리자", value=f"{ctx.author.mention} ( {ctx.author} )", inline=False)
        embed.add_field(name="차단 해제 대상자", value=f"{user.mention} ( {user} )", inline=False)
        embed.set_footer(text=f"제작 : 스텔#1476")
        return await ctx.reply(embed=embed)
    except:
        embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**🚫 유저 차단 해제 안내**", color = 0XDF05FF)
        embed.add_field(name="담당 관리자", value=f"{ctx.author.mention} ( {ctx.author} )", inline=False)
        embed.add_field(name="차단 해제 대상자", value=f"{user.mention} ( {user} )", inline=False)
        embed.set_footer(text=f"제작 : 스텔#1476")
        embed.set_thumbnail(url=user.avatar_url)
        return await ctx.reply(f"\✅ 성공적으로 `{user}`님의 차단을 해제했어요.")
        await ctx.reply(embed=embed)

@bot.command(name="추방", description="관리자 전용 명령어 입니다.")
async def kick(ctx, user : discord.Member = None, reason = "사유가 없습니다."):
  permission = ctx.author.guild_permissions.manage_roles
  if not ctx.guild:
    err = "해당 명령어는 서버에서만 사용하실수 있어요!"
  elif permission is False:
    err = "당신은 권한이 없습니다!"
  elif user == None:
    err = "킥할 유저를 입력해주세요!"
  elif user.id == ctx.author.id:
    err = "자기 자신을 킥할수 없어요!"
  elif user.guild_permissions.administrator:
    err = "관리자 권한을 가진 사람은 킥할수 없어요!"
  else:
    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**🚫 유저 추방 안내**", color=0xFFFD05)
    embed.add_field(name="담당 관리자", value=f"{ctx.author.mention} ( {ctx.author} )", inline=False)
    embed.add_field(name="차단 대상자", value=f"{user.mention} ( {user} )", inline=False)
    embed.add_field(name="추방 사유", value=f"```cs\n# {reason}```", inline=False)
    embed.set_footer(text=f"제작 : 스텔#1476")
    await user.send(embed=embed)
    await user.kick(reason=reason)
    return await ctx.send(embed=embed)

  embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**추방 명령어 오류**", description=f"{err}",color=0xff0000)
  await ctx.reply(embed=embed)

@bot.command(name="청소", description="관리자 전용 명령어 입니다.")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int = None):
        if amount == None:
            embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), title="**청소명령어 오류**", description=f"\❌ 삭제할 량을 입력하세요.",color=0XDF05FF)
            await ctx.reply(embed=embed)
        else:
            await ctx.channel.purge(limit=amount+1)
            embed = discord.Embed(title="**♻  메시지 삭제 안내**", description=f"메시지 {amount}개가 삭제되었어요!", color = 0XDF05FF, timestamp = datetime.datetime.utcnow())
            embed.set_footer(text=f"제작 : 스텔#1476ㅣ담당자 : {ctx.author}")
            msg = await ctx.send(embed=embed)


# # # 배정 시스템 # # #


@bot.command(name="배정등록", description="관리자 전용 명령어 입니다.")
async def 배정등록(ctx):
    if f"{ctx.author}" in allotment:
        embed = discord.Embed(title="배정 오류", description="이미 배정 대기중입니다.", color = 0xff0000)
        msg = await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="관리자 배정중...", description="관리자를 배정하고 있습니다.", color = 0XDF05FF)
        msg = await ctx.reply(embed=embed)
        allotment.append(f"{ctx.author}")
        time.sleep(1)
        embed = discord.Embed(title="관리자 배정중...", description="배정 대기 목록에 추가하였습니다.", color = 0XDF05FF)
        await msg.edit(embed=embed)

@bot.command(name="배정리스트", description="관리자 전용 명령어 입니다.")
async def 배정리스트(ctx):
    if len(allotment) == 0:
      embed = discord.Embed(title="배정리스트", description=f"배정대기자가 없습니다.")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="배정리스트", description=f"{allotment}")
      await ctx.send(embed=embed)

@bot.command(name="배정하기", description="관리자 전용 명령어 입니다.")
async def 배정하기(ctx, loaduser: discord.Member):
    if f"{loaduser}" in allotment:
      embed = discord.Embed(title="배정을 하는중입니다.", description="배정을 진행하고 있습니다.", color = 0xff0000)
      msg = await ctx.reply(embed=embed)
      
      time.sleep(1)
      allotment.remove(f"{loaduser}")
      embed = discord.Embed(title="배정을 하였습니다.", description=f"{loaduser} 님의 담당관리자 : {ctx.author}", color = 0XDF05FF)
      await msg.edit(embed=embed)
      try:
        loaduserembed = discord.Embed(title="배정이 완료되었습니다.", description=f"{loaduser} 님의 담당관리자 : {ctx.author}", color = 0XDF05FF)
        await loaduser.send(embed=loaduserembed)
      except:
        embed = discord.Embed(title="배정 오류", description="유저에게 알림 전송을 하지 못했습니다.", color = 0xff0000)
        await ctx.send(embed=embed)
    else:
      try:
        embed = discord.Embed(title="배정 오류", description="해당 유저는 배정 대기 목록에 없습니다.", color = 0xff0000)
        msg = await ctx.reply(embed=embed)
      except:
        embed = discord.Embed(title="배정 오류", description="배정 할 유저를 멘션하세요.", color = 0xff0000)
        msg = await ctx.reply(embed=embed)

bot.run(TOKEN)