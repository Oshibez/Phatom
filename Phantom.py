import discord
import random
from discord import app_commands
from discord.ext import commands
from Ping import ping
import os
from datetime import datetime
from idle import timer

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

cmdcaller = "c-"

badge = ""

Whitelisted = "team", "I am fan", "greenninja"


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Tameing.io"))
  await bot.change_presence(status=discord.Status.online)
  print("Bot is Up and Ready!")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@bot.tree.command(name="badge")
@app_commands.describe(thing_to_say="Enter badge name")
async def say(interaction: discord.Interaction, thing_to_say: str):
  if (interaction.user.name == "Oshibez"):
    badge = open("oshibez.txt", "w")
    badge.write(thing_to_say)
    badge.close()
    await interaction.response.send_message("Your badge is now " +
                                            thing_to_say,
                                            ephemeral=True)
    print(badge)
  elif (interaction.user.name == "Friendly Guys"):
    badge = open("frguy.txt", "w")
    badge.write(thing_to_say)
    badge.close()
    await interaction.response.send_message("Your badge is now " +
                                            thing_to_say,
                                            ephemeral=True)
    print(badge)
  elif (interaction.user.name == "Red"):
    badge = open("red.txt", "w")
    badge.write(thing_to_say)
    badge.close()
    await interaction.response.send_message("Your badge is now " +
                                            thing_to_say,
                                            ephemeral=True)
    print(badge)


@bot.tree.command(name="playerstats")
@app_commands.describe(thing_to_say="Enter player name")
async def say(interaction: discord.Interaction, thing_to_say: str):
  if thing_to_say.lower() == "friendly guys":
    embed = discord.Embed(title="Player Stats", description="", color=0x00FF00)
    badge = open("frguy.txt", "r")
    embed.add_field(name="Badge", value=badge.read(100), inline=True)
    embed.set_author(name="Friendly guys")
    embed.set_footer(text="Shows list of commands")
    await interaction.response.send_message(embed=embed)
  elif thing_to_say.lower() == "oshibez":
    embed = discord.Embed(title="Player Stats", description="", color=0x00FF00)
    badge = open("oshibez.txt", "r")
    embed.add_field(name="Badge", value=badge.read(100), inline=True)
    embed.set_author(name="Oshibez")
    embed.set_footer(text="Shows list of commands")
    await interaction.response.send_message(embed=embed)
  elif thing_to_say.lower() == "red":
    embed = discord.Embed(title="Player Stats", description="", color=0x00FF00)
    badge = open("red.txt", "r")
    embed.add_field(name="Badge", value=badge.read(100), inline=True)
    embed.set_author(name="Red")
    embed.set_footer(text="Shows list of commands")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="event")
@app_commands.describe(thing_to_say="text")
async def say(interaction: discord.Interaction, thing_to_say: str):
  if interaction.user.name == "Oshibez" or "Friendly Guys":
    await interaction.response.send_message("@everyone " + thing_to_say)
  else:
    await interaction.response.send_message(
      "Your not allowed to use this command", ephemeral=True)


@bot.tree.command(name="state")
@app_commands.describe(thing_to_say="text")
async def say(interaction: discord.Interaction, thing_to_say: str):
  if interaction.user.name == "Oshibez" or "Friendly Guys":
    await interaction.response.send_message(thing_to_say + interaction.user)
  else:
    print(interaction.user.name + " tried to use this command.")
    await interaction.response.send_message(
      "Your not allowed to use this command", ephemeral=True)


#-------------------------Commands---------------------------------
@bot.event
async def on_member_join(member):
  await member.create_dm()
  if member.name == Whitelisted:
    await member.dm_channel.send(
      f'Hi {member.name}, welcome to the discord sever for the clan TEAM')
    await member.dm_channel.send(
      f'Before you join {member.name} please send an image of you in tameing.io at max level in #pfp. This will be your profile picture'
    )
  else:
    mean_text = random.choice([
      "Sorry but if you want to join you need to be whitelisted",
    ])
    await member.dm_channel.send(mean_text)
    await member.ban(reason="Banned by Phantom | Reason: Not whitelisted",
                     delete_message_days=7)
    channel = bot.get_channel(1072759806743556157)
    await channel.send(message)
    print(f"Banned {member.display_name}!")


@bot.event
async def on_message(message):
  print(message.content)


ping()

bot.run(os.getenv("TOKEN"))
