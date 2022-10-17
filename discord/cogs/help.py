import discord
from discord.ext import commands

commands_list = {}

# Example
# commands_list['testy'] = ['Description',
#                           '<arg1> <arg2>',
#                           'usage_arg1 usage_arg2']

commands_list['mg_set_channel'] = ['Set MediaGrabber channel.',
                                    '',
                                    '']

commands_list['clear_browser'] = ['Clear the browser source.',
                                    '',
                                    '']

commands_list['img'] = ['Display an image on screen. (Requires attached image)',
                                    '<time>',
                                    '15']                                         

class Help(commands.Cog, name='Help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help loaded.")

    @commands.command()
    async def help(self, ctx, *command):
        # List all commands
        if len(command) <= 0:
            output = '```\n'
            output += 'Use \'.help <command>\' for specific usage for a particular command.\n----------\n'
            for key in commands_list:
                curr_line = '.' + key + '   ' + commands_list[key][0] + '\n'
                output += curr_line
            output += '\n```'
            await ctx.message.channel.send(output)
            await ctx.message.delete()
        # Print out specifics for a single command
        elif len(command) == 1:
            for key in commands_list:
                if ''.join(command) in key or key in ''.join(command):
                    output = '```\n'
                    curr_line = '.' + key + '   ' + commands_list[key][0] + '\n'
                    curr_line += '\n Usage: .' + key + ' ' + commands_list[key][1]
                    curr_line += '\n Ex: .' + key + ' ' + commands_list[key][2]
                    output += curr_line
                    output += '\n```'
                    await ctx.message.channel.send(output)
            await ctx.message.delete()
        else:
            ctx.message.author.send('[Error] Help page for specified command not found.')
            await ctx.message.delete()