#!/usr/bin/env python3

import discord
import random, os, subprocess, shutil, sys

from asyncio import sleep
from discord.ext import commands

# User loads their laundry first, then washes and dries it
# After drying, they should be billed a lot of money

prefix = '.'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
      print('Laundry Services bot is ready.')


class Machine:
    def __init__(self, user, occupied):
        self.user = None
        self.occupied = False

class Access:
    def __init__(self, users):
        self.users = []

# Dry users list is empty at first
dry_access = Access([])
dry_users = dry_access.users

# Preset status to all machines unoccupied with no users
wash1 = Machine(None, False)
wash2 = Machine(None, False)
wash3 = Machine(None, False)
dry1 = Machine(None, False)
dry2 = Machine(None, False)
dry3 = Machine(None, False)

# Load laundry
@commands.command()
async def load(ctx, machine):

    if machine == "wash1":
        if wash1.user == None:
            wash1.user = ctx.author.mention
            await ctx.send(f'{wash1.user}, your laundry has been loaded into Wash 1. Use .wash wash1 to wash it.')
        else:
            await ctx.send('Please choose an available washing machine. If none are available, please wait.')

    elif machine == "wash2":
        if wash2.user == None:
            wash2.user = ctx.author.mention
            await ctx.send(f'{wash1.user}, your laundry has been loaded into Wash 2. Use .wash wash2 to wash it.')
        else:
            await ctx.send('Please choose an available washing machine. If none are available, please wait.')

    elif machine == "wash3":
        if wash3.user == None:
            wash3.user = ctx.author.mention
            await ctx.send(f'{wash3.user}, your laundry has been loaded into Wash 3. Use .wash wash3 to wash it.')
        else:
            await ctx.send('Please choose an available washing machine. If none are available, please wait.')

    else:
        await ctx.send('That machine does not exist!')

# Unload laundry
@commands.command()
async def unload(ctx, machine):

    if machine == "wash1":
        if ctx.author.mention == wash1.user:
            wash1.user = None
            await ctx.send('Wash 1 is now available.')
        else:
            await ctx.send('That is not your machine.')

    elif machine == "wash2":
        if ctx.author.mention == wash2.user:
            wash2.user = None
            await ctx.send('Wash 2 is now available.')
        else:
            await ctx.send('That is not your machine.')

    elif machine == "wash3":
        if ctx.author.mention == wash2.user:
            wash13.user = None
            await ctx.send('Wash 3 is now available.')
        else:
            await ctx.send('That is not your machine.')

    else:
        await ctx.send('That machine does not exist!')

    if is_admin(ctx.author):
        if machine == "wash1":
            wash1.user = None
            await ctx.send('The washing machine is now available. By order of the admins.')

        elif machine == "wash2":
            wash2.user = None
            await ctx.send('The washing machine is now available. By order of the admins.')

        elif machine == "wash3":
            wash3.user = None
            await ctx.send('The washing machine is now available. By order of the admins.')

    else:
        pass


# Wash laundry 
@commands.command()
async def wash(ctx, machine):

    if machine == "wash1":
        if wash1.user == ctx.author.mention:
            if wash1.occupied == True:

                await ctx.send('You have already washed these clothes. Stop wasting water.')

            else:
                await ctx.send('Starting wash cycle, please wait 3 seconds ...')
                await sleep(3)
                await ctx.send(f'{wash1.user}, your laundry has been washed. Use .dry (machine) to dry it.')

                wash1.occupied = True
                dry_users.append(wash1.user)

        elif wash1.user == None:
            await ctx.send('You must load your clothes into the machine (wash1) first!')

        else:
            await ctx.send(f'{wash1.user}\'s wash cycle is in progress, please wait...')

    elif machine == "wash2":
        if wash2.user == ctx.author.mention:
            if wash2.occupied == True:

                await ctx.send('You have already washed these clothes. Stop wasting water.')

            else:
                await ctx.send('Starting wash cycle, please wait 3 seconds ...')
                await sleep(3)
                await ctx.send(f'{wash2.user}, your laundry has been washed. Use .dry (machine) to dry it.')

                wash2.occupied = True
                dry_users.append(wash2.user)

        elif wash2.user == None:
            await ctx.send('You must load your clothes into the machine (wash2) first!')

        else:
            await ctx.send(f'{wash2.user}\'s wash cycle is in progress, please wait...')

    elif machine == "wash3":
        if wash3.user == ctx.author.mention:
            if wash3.occupied == True:

                await ctx.send('You have already washed these clothes. Stop wasting water.')

            else:
                await ctx.send('Starting wash cycle, please wait 3 seconds ...')
                await sleep(3)
                await ctx.send(f'{wash3.user}, your laundry has been washed. Use .dry (machine) to dry it.')

                wash3.occupied = True
                dry_users.append(wash3.user)

        elif wash3.user == None:
            await ctx.send('You must load your clothes into the machine (wash3) first!')

        else:
            await ctx.send(f'{wash3.user}\'s wash cycle is in progress, please wait...')

    else:
        await ctx.send('That machine does not exist.')


# Dry laundry
@commands.command()
async def dry(ctx, machine):

    if machine == "dry1":
        if ctx.author.mention in dry_users:
            if dry1.occupied == True:
                await ctx.send(f'{dry1.user}\'s dry cycle in progress. Please wait or use a different machine.')

            elif dry1.occupied == False:
                dry1.user = ctx.author.mention
                dry1.occupied = True

                total = random.randint(100, 15000)

                await ctx.send('Starting dry cycle, please wait 3 seconds...')
                await sleep(3)
                await ctx.send(f'{dry1.user}, your laundry has been dried.\nYour total is ${total}.')

                dry_users.remove(dry1.user)
                dry1.user = None
                dry1.occupied = False

        elif ctx.author.mention not in dry_users:
            await ctx.send('You must wash your clothes before drying them!')

    elif machine == "dry2":
        if ctx.author.mention in dry_users:
            if dry2.occupied == True:

                await ctx.send(f'{dry2.user}\'s dry cycle in progress. Please wait or use a different machine.')

            elif dry2.occupied == False:
                dry2.user = ctx.author.mention
                dry2.occupied = True

                total = random.randint(100, 15000)

                await ctx.send('Starting dry cycle, please wait 3 seconds...')
                await sleep(3)
                await ctx.send(f'{dry2.user}, your laundry has been dried.\nYour total is ${total}.')

                dry_users.remove(dry2.user)
                dry2.user = None
                dry2.occupied = False

        elif ctx.author.mention not in dry_users:
            await ctx.send('You must wash your clothes before drying them!')

    elif machine == "dry3":
        if ctx.author.mention in dry_users:
            if dry3.occupied == True:

                await ctx.send(f'{dry3.user}\'s dry cycle in progress. Please wait or use a different machine.')

            elif dry3.occupied == False:
                dry3.user = ctx.author.mention
                dry3.occupied = True

                total = random.randint(100, 15000)

                await ctx.send('Starting dry cycle, please wait 3 seconds...')
                await sleep(3)
                await ctx.send(f'{dry3.user}, your laundry has been dried.\nYour total is ${total}.')

                dry_users.remove(dry3.user)
                dry3.user = None
                dry3.occupied = False

        elif ctx.author.mention not in dry_users:
            await ctx.send('You must wash your clothes before drying them!')

    else:
        await ctx.send('That machine does not exist.')


# Checks if user is an administrator
def is_admin(user): 
    return user.guild_permissions.administrator


# Calls git commands from terminal
def git(*args):
    return subprocess.check_call(['git'] + list(args))

@commands.command()
async def update(ctx):

    if is_admin(ctx.message.author):

        await ctx.send('Updating Laundry Bot...')

        if os.path.exists('bot.py'): # remove the old source file
            os.remove('bot.py')
        if os.path.exists('Laundry-Bot'): # remove old cloned directory
            shutil.rmtree('Laundry-Bot')

        git('clone', 'https://github.com/helloMusa/Laundry-Bot.git') # Clones repo
        if os.path.exists('Laundry-Bot/bot.py'): # move file to working directory
            os.replace('Laundry-Bot/bot.py', '../Laundry-Bot/bot.py')
            import stat # set execute permissions
            st = os.stat('bot.py')
            os.chmod('bot.py', st.st_mode | stat.S_IEXEC)

        if os.path.exists('Laundry-Bot'): # cleanup
            shutil.rmtree('Laundry-Bot')

        await ctx.send('Laundry Bot is done updating.')

    else:
        await ctx.send('You are not authorized to use this command.')


# Restarts the bot
@commands.command()
async def reset(ctx):

    if is_admin(ctx.message.author):
        # Restart the bot
        await ctx.send('Restarting Laundry Bot...')
        os.execv('/home/ubuntu/laundry_services_bot/Laundry-Bot/bot.py', sys.argv)
    else:
        await ctx.send('You are not authorized to use this command.')


def main():

    if len(sys.argv) < 2:
        print(f'ERROR 0: No Client Token Provided')
        sys.exit

    client.add_command(load)
    client.add_command(unload)
    client.add_command(wash)
    client.add_command(dry)
    client.add_command(reset)
    client.add_command(update)

    bot_token = sys.argv[1]
    client.run(bot_token)


if __name__ == '__main__':
    main()
