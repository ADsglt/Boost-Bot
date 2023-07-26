from discord.ext import commands
import discord, os, json, hashlib, fade
from boosting import *
from auto import *
if os.name == 'nt':
    import ctypes
from datetime import datetime
from colorama import Fore

config = json.load(open("config.json", encoding="utf-8"))

def clear(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')
    
    

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Boost Bot")
else:
    pass


TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
bot = discord.Bot(intents = discord.Intents.all())
capmonster_key = config.get("capmonster_key")
# sellapp = config.get("sellappchannel")
# sellix = config.get("sellixchannel")

if capmonster_key != " ":
    from colorama import Fore
    Key = f"{Fore.LIGHTGREEN_EX}Enable{Fore.RESET}"
else :
    from colorama import Fore
    Key = f"{Fore.LIGHTRED_EX}Disabled{Fore.RESET}"
# if sellapp != " ":
#     Sellapp = f"{Fore.LIGHTGREEN_EX}Enable{Fore.RESET}"
# else :
#     Sellapp = f"{Fore.LIGHTRED_EX}Disabled{Fore.RESET}"
# if sellix != " ":
#     Sellix = f"{Fore.LIGHTGREEN_EX}Enable{Fore.RESET}"
# else :
#     Sellix = f"{Fore.LIGHTRED_EX}Disabled{Fore.RESET}"

@bot.event
async def on_ready():
    from colorama import Fore
    BoostBot = f"""
                            _____________________________________   _______________________
                            ___  __ )_  __ \_  __ \_  ___/__  __/   ___  __ )_  __ \__  __/
                            __  __  |  / / /  / / /____ \__  /      __  __  |  / / /_  /   
                            _  /_/ // /_/ // /_/ /____/ /_  /       _  /_/ // /_/ /_  /    
                            /_____/ \____/ \____/ /____/ /_/        /_____/ \____/ /_/"""
                                
    Account =f"""                                   🦑  {Fore.WHITE}ACCOUNT CONNECTED  -  {bot.user}  🦑"""
    menu = f"""
                                          {Fore.LIGHTMAGENTA_EX}[ {Fore.WHITE}Capmonster Key  {Fore.LIGHTMAGENTA_EX}] {Fore.WHITE}> {Key}
                                          {Fore.LIGHTMAGENTA_EX}[ {Fore.WHITE}Sellapp Channel {Fore.LIGHTMAGENTA_EX}] {Fore.WHITE}> {Fore.LIGHTGREEN_EX}Enable
                                          {Fore.LIGHTMAGENTA_EX}[ {Fore.WHITE}Sellix Channel  {Fore.LIGHTMAGENTA_EX}] {Fore.WHITE}> {Fore.LIGHTGREEN_EX}Enable{Fore.RESET}"""
    fade_text = fade.pinkred(BoostBot)
    print(fade_text + '\n' + Account + '\n' + menu + '\n')
    
# HELP COMMAND
@bot.slash_command(name="help", description="Helps you understand how the commands work.")
async def help(ctx: discord.ApplicationContext):
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTYELLOW_EX}[ ~ ] {Fore.WHITE}{ctx.author} use the command help.")
    embed = discord.Embed(title=f"<:ADscript:1085672769611628665> | **BOT COMMANDS**", color=0x2F3136) 
    embed.add_field(name="Find all my commands below :", value=f"""
    \n`/help` - View all commands
`/activity` - Change the activity of the bot
`/ping` - Show the latency of the bot
`/boost` - Allows you to boost servers with tokens
`/stock` -  Shows you your current tokens and boosts stock
`/restock` - Allows to add tokens (https://paste.ee)
`/clearstock` - Will delete everything from your stock
`/givetokens` - Allows you to give tokens to a user
`/buy` - ***Soon***""")
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    await ctx.respond(embed=embed)

# ACTIVITY COMMAND
@bot.slash_command(name="activity", description="Changes the activity of the bot.") 
async def activity(ctx, activity=discord.Option(str, "activity", required=True)):
    if ctx.author.id not in config["ownerID"] and ctx.author.id not in config['adminID']:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permission**", description = "You must be an owner or an administrator to use this command!", color = 0xf35454))
    await bot.change_presence(activity=discord.Streaming(type=discord.ActivityType.streaming, name=activity, url="https://www.twitch.tv/discordshopfr"))
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTYELLOW_EX}[ ~ ] {Fore.WHITE}Activity changed to {Fore.LIGHTBLACK_EX}{activity}")
    embed = discord.Embed(title="<:ADglobe:1085672771717173339> | **ACTIVITY**", description=f"**Activity has been changed to** `{activity}`.\n*Changed by* <@{ctx.author.id}>", color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    return await ctx.respond(embed=embed)

# LATENCY COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="ping", description="Check the bot's latency.")
async def ping(ctx):
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTYELLOW_EX}[ ~ ] {Fore.WHITE}{ctx.author} has check my latency {Fore.LIGHTBLACK_EX}[{Fore.WHITE}{round(bot.latency * 1000)} ms{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    await ctx.respond(embed = discord.Embed(title = " ", description = f"<:ADsetting2:1085671134307037325> **{round(bot.latency * 1000)} ms**", color = 0x2c2f33))

# GIVE TOKEN COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="givetokens", description="Gives X amount of tokens to a specified user")
async def give_tokens(ctx: discord.ApplicationContext, amount: discord.Option(int, "Amount of tokens.", required=True),
                      user: discord.Option(discord.User, "User you want to send tokens to.", required=True),
                      type: discord.Option(int, "Type of tokens you are giving, 3 months or 1 month", required=True)):
    if ctx.author.id not in config["ownerID"] and ctx.author.id not in config['adminID']:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permission**", description = "You must be an owner or an administrator to use this command!", color = 0xf35454))
    else :
        if type != 1 and type != 3 and type != 0:
            return await ctx.respond(embed = discord.Embed(title = "**Invalid Input**", description = "Type can either be 3 (months), 1 (month) or empty", color = 0xf35454))
        if type == 1:
            file = "input/1m_tokens.txt"
            month = "1 mois"
        elif type == 3:
            file = "input/3m_tokens.txt"
            month = "3 mois"
        temp_tokens = open(file, encoding="UTF-8").read().splitlines()
        if len(temp_tokens) < amount:
            return await ctx.respond("You do not have enough tokens in stock.")

        tokens_to_give = temp_tokens[0:amount]
        temp_tokens = temp_tokens[amount:]

        f = open(f"tokens.txt", "w", encoding="UTF-8")
        for tk in tokens_to_give:
            f.write(tk + "\n")
        f.close()

        f = open(file, "w", encoding="UTF-8")
        for tk in temp_tokens:
            f.write(tk + "\n")
        f.close()
        embed = discord.Embed(title=f"<:ADgift:1085655148212269226> | **TOKENS SENT**",
                              description=f"x{amount} tokens {month} have been sent to **{user}**.",
                              color=0x2F3136)
        embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
        await ctx.respond(embed=embed,ephemeral=True, file=discord.File("tokens.txt"))
        await user.send(f"{ctx.author} has sent you `{amount}` Nitro Tokens  {month}\nFormat : `email:pass:token`.", file=discord.File("tokens.txt"))
        await ctx.respond(embed=embed)
        os.remove("tokens.txt")
        from colorama import Fore
        TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        print(f" {TimeNow} {Fore.LIGHTGREEN_EX}[ + ] {Fore.WHITE}{ctx.author} has sent {amount} Nitro Tokens {month} to {user}")

# RESTOCK COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="restock", description="Allows one to restock 1 month or 3 month nitro tokens.")
async def restock(ctx, code: discord.Option(str, "Paste.ee link", required = True),type: discord.Option(int, "Type of tokens you are restocking, 3 months or 1 month", required=True)):
    if ctx.author.id not in config["ownerID"] and ctx.author.id not in config['adminID']:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permission**", description = "You must be an owner or an administrator to use this command!", color = 0xf35454))
    if type != 1 and type != 3 and type != 0:
        return await ctx.respond(embed = discord.Embed(title = "**Invalid Input**", description = "Type can either be 3 (months), 1 (month) or empty", color = 0xf35454))
    if type == 1:
        file = "input/1m_tokens.txt"
    elif type == 3:
        file = "input/3m_tokens.txt"
        
    code = code.replace("https://paste.ee/p/", "")
    temp_stock = requests.get(f"https://paste.ee/d/{code}", headers={ "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}).text
    
    f = open(file, "a", encoding="utf-8")
    f.write(f"{temp_stock}\n")
    f.close()
    lst = temp_stock.split("\n")
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTGREEN_EX}[ + ] {Fore.WHITE}{ctx.author} Restock {len(lst)} tokens to `{file}`")
    embed = discord.Embed(title=f"<:ADlink:1085655152544993360> | **TOKENS RESTOCK**",
                              description=f"**Restock {len(lst)} tokens to** `{file}`",
                              color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    await ctx.respond(embed=embed)

# ADD OWNER COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="addowner", description="Adds an owner.")
async def addowner(ctx, member: discord.Option(discord.Member, "Member who has add to be added as an owner.", required = True)):
    if ctx.author.id not in config["ownerID"]:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permissionn**", description = "You must be an owner to use this command!", color = 0xf35454))
    
    config["ownerID"].append(member.id)
    with open('config.json', 'w') as f:
        json.dump(config, f, indent = 4)
    
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTGREEN_EX}[ + ] {Fore.WHITE}{ctx.author} added {member} as an owner")
    embed = discord.Embed(title=f"<:ADadmin:1085655167971635290> | **ADDED OWNER**",
        description=f"<@{ctx.author.id}> **added** {member} ({member.id}) **as an owner**",
        color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    await ctx.respond(embed=embed)

# ADD ADMIN COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="addadmin", description="Adds an admin.")
async def addadmin(ctx, member: discord.Option(discord.Member, "Member who has add to be added as an admin.", required = True)):
    if ctx.author.id not in config["ownerID"]:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permissionn**", description = "You must be an owner to use this command!", color = 0xf35454))
    
    config["adminID"].append(member.id)
    with open('config.json', 'w') as f:
        json.dump(config, f, indent = 4)
        
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTGREEN_EX}[ + ] {Fore.WHITE}{ctx.author} added {member} as an admin")
    embed = discord.Embed(title=f"<:ADadmin:1085655167971635290> | **ADDED ADMIN**",
        description=f"<@{ctx.author.id}> **added** {member} ({member.id}) **as an admin**",
        color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    await ctx.respond(embed=embed)

# INFO STOCK COMMAND
@bot.slash_command(guild_ids=[config["guildID"]], name="stock", description="Allows you to see the current stock.")
async def stock(ctx):
    three = len(open("input/3m_tokens.txt", "r").readlines())
    one = len(open("input/1m_tokens.txt", "r").readlines())
    embed = discord.Embed(title=f"<:ADboost:1085655158823854121> | **INFO STOCK**",
        description=f"""> **1 Month Nitro Tokens :** `{one}`
        > **3 Months Nitro Tokens :** `{three}`\n
        > **1 Month Server Boosts :** `{one*2}`
        > **3 Months Server Boosts :** `{three*2}`""",
        color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    await ctx.respond(embed=embed)


# CLEAR STOCK COMMAND
@bot.slash_command(name="clearstock", description="Deletes your whole stock.")
async def help(ctx: discord.ApplicationContext, type: discord.Option(int, "Type of tokens you are restocking, 3 months or 1 month", required=True)):
    if ctx.author.id not in config["ownerID"] and ctx.author.id not in config['adminID']:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permission**", description = "You must be an owner or an administrator to use this command!", color = 0xf35454))
    if type != 1 and type != 3 and type != 0:
        return await ctx.respond(embed = discord.Embed(title = "**Invalid Input**", description = "Type can either be 3 (months), 1 (month) or empty", color = 0xf35454))
    if type == 1:
        file = "input/1m_tokens.txt"
        month = "1 month"
    elif type == 3:
        file = "input/3m_tokens.txt"
        month = "3 month"

    embed = discord.Embed(title=f"<:ADverif:1085655156105941082> | **STOCK CLEARED**",
                          color=0x2F3136)
    embed.set_thumbnail(url="https://i.imgur.com/UAzE93w.png")
    fileVariable = open(file, 'r+')
    fileVariable.truncate(0)
    fileVariable.close()
    await ctx.respond(embed=embed)
    from colorama import Fore
    TimeNow = datetime.now().strftime(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}%H{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%M{Fore.LIGHTBLACK_EX}:{Fore.WHITE}%S{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    print(f" {TimeNow} {Fore.LIGHTRED_EX}[ - ] {Fore.WHITE}{ctx.author} has clear his stock {month}")

    
@bot.slash_command(guild_ids=[config["guildID"]], name="boost", description="Boosts a discord server.")
async def boost(ctx, invite: discord.Option(str, "Invite link to the server you want to boost.", required = True), amount: discord.Option(int, "Number of times you want to boost the sever.", required = True), months: discord.Option(int, "Number of months you want to boost the server for 1 or 3.", required = True),nick: discord.Option(str, "Nickname you want to set for the boosting account.", required = False) = config['server_nick']):
    if ctx.author.id not in config["ownerID"] and ctx.author.id not in config['adminID']:
        return await ctx.respond(embed = discord.Embed(title = "**Missing Permission**", description = "<a:ADanno1:1085653934644920361> **You must be an owner or an administrator to use this command <a:ADanno1:1085653934644920361>", color = 0xf46868))
    if months != 1 and months != 3:
        return await ctx.respond(embed = discord.Embed(title = "**Invalid Input**", description = "<a:ADanno1:1085653934644920361> **Months can either be 3 (months) or 1 (month)** <a:ADanno1:1085653934644920361>", color = 0xf46868))
    if amount % 2 != 0:
        return await ctx.respond(embed = discord.Embed(title = "**Invalid Input**", description = "<a:ADanno1:1085653934644920361> **Amount needs to be even** <a:ADanno1:1085653934644920361>", color = 0xf46868))
    if months == 1:
        filename = "input/1m_tokens.txt"
    if months == 3:
        filename = "input/3m_tokens.txt"
    
    if checkEmpty(filename):
        return await ctx.respond(embed = discord.Embed(title = "**Stock Error**", description = "<a:ADanno1:1085653934644920361> **There is currently no stock in the files. Please use `/restock` to add nitro tokens in the stock files** <a:ADanno1:1085653934644920361>", color = 0xf46868))
    if len(open(filename, "r").readlines()) < amount / 2:
        return await ctx.respond(embed = discord.Embed(title = "**Stock Error**", description = "<a:ADanno1:1085653934644920361> **There is currently not enough stock in the files. Please use `/restock` to add nitro tokens in the stock files** <a:ADanno1:1085653934644920361>", color = 0xf46868))
    
    invite = getinviteCode(invite)
    
    if validateInvite(invite) == False:
        return await ctx.respond(embed = discord.Embed(title = "**Invite Error**", description = "<a:ADanno1:1085653934644920361> **The invite submitted is invalid. Please sumbit a valid invite link** <a:ADanno1:1085653934644920361>", color = 0xf46868))
    
    await ctx.respond(embed = discord.Embed(title = "<a:ADloading:1085672775026483310> **Boosts Started**", description = f"**Invite Link: **https://discord.gg/{invite}\n**Amount: **{amount} Boosts\n**Months: **{months} Months", color = 0x2c2f33))
    print()
    sprint(f"Boosting https://discord.gg/{invite}, {amount} times for {months} months", True)
    start = time.time()
    boosted = thread_boost(invite, amount, months, nick)
    end = time.time()
    time_taken = round(end - start, 2)
    
    if boosted == False:
        with open('success.txt', 'w') as f:
            for line in variables.success_tokens:
                f.write(f"{line}\n")
        
        with open('failed.txt', 'w') as g:
            for line in variables.failed_tokens:
                g.write(f"{line}\n")
    
    
        embed2 = DiscordEmbed(title = "<a:ADanno1:1085653934644920361> **Boosts Unsuccessful**", description = f"**Boost Type: **Manual\n**Order ID: **N/A\n**Product Name: **{amount} Server Boosts [{months} Months]\n**Customer Email: **N/A\n\n**Invite Link: **https://discord.gg/{invite}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n\n**Time Taken: **{time_taken} seconds\n**Successful Tokens: **{len(variables.success_tokens)}\n**Successful Boosts: **{len(variables.success_tokens)*2}\n\n**Failed Tokens: **{len(variables.failed_tokens)}\n**Failed Boosts: **{len(variables.failed_tokens)*2}", color = 0xf35454)
        embed2.set_timestamp()
        webhook = DiscordWebhook(url=config["boost_failed_log_webhook"])
        webhook.add_embed(embed2)
        webhook.execute()
        print()
        sprint(f"Failed to Boost https://discord.gg/{invite}, {amount} times for {months} months. Operation took {time_taken} seconds", False)
        print()
        
        webhook = DiscordWebhook(url=config["boost_failed_log_webhook"])
        with open("success.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='success.txt')
        with open("failed.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='failed.txt')
        webhook.execute()
        
        os.remove("success.txt")
        os.remove("failed.txt")
        
        return await ctx.respond(embed = discord.Embed(title = "<a:ADanno1:1085653934644920361> **Boosts Unsuccessful**", description = f"**Boost Type: **Manual\n**Order ID: **N/A\n**Product Name: **{amount} Server Boosts [{months} Months]\n**Customer Email: **N/A\n\n**Invite Link: **https://discord.gg/{invite}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n\n**Time Taken: **{time_taken} seconds\n**Successful Tokens: **{len(variables.success_tokens)}\n**Successful Boosts: **{len(variables.success_tokens)*2}\n\n**Failed Tokens: **{len(variables.failed_tokens)}\n**Failed Boosts: **{len(variables.failed_tokens)*2}", color = 0xf35454))
    
    elif boosted:
        with open('success.txt', 'w') as f:
            for line in variables.success_tokens:
                f.write(f"{line}\n")
        
        with open('failed.txt', 'w') as g:
            for line in variables.failed_tokens:
                g.write(f"{line}\n")
                
        embed3 = DiscordEmbed(title = "<a:ADanyes1:1085653776905551962> **Boosts Successful**", description = f"**Boost Type: **Manual\n**Order ID: **N/A\n**Product Name: **{amount} Server Boosts [{months} Months]\n**Customer Email: **N/A\n\n**Invite Link: **https://discord.gg/{invite}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n\n**Time Taken: **{time_taken} seconds\n**Successful Tokens: **{len(variables.success_tokens)}\n**Successful Boosts: **{len(variables.success_tokens)*2}\n\n**Failed Tokens: **{len(variables.failed_tokens)}\n**Failed Boosts: **{len(variables.failed_tokens)*2}", color = 0x62f354)
        embed3.set_timestamp()
        webhook = DiscordWebhook(url=config["boost_log_webhook"])
        webhook.add_embed(embed3)
        webhook.execute()
        print()
        sprint(f"Boosted https://discord.gg/{invite}, {amount} times for {months} months. Operation took {time_taken} seconds", True)
        print()
        
        webhook = DiscordWebhook(url=config["boost_log_webhook"])
        with open("success.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='success.txt')
        with open("failed.txt", "rb") as f:
            webhook.add_file(file=f.read(), filename='failed.txt')
        webhook.execute()
        
        os.remove("success.txt")
        os.remove("failed.txt")
        
        return await ctx.respond(embed = discord.Embed(title = "<a:ADanyes1:1085653776905551962> **Boosts Successful**", description = f"**Boost Type: **Manual\n**Order ID: **N/A\n**Product Name: **{amount} Server Boosts [{months} Months]\n**Customer Email: **N/A\n\n**Invite Link: **https://discord.gg/{invite}\n**Amount: **{amount} Boosts\n**Months: **{months} Months\n\n**Time Taken: **{time_taken} seconds\n**Successful Tokens: **{len(variables.success_tokens)}\n**Successful Boosts: **{len(variables.success_tokens)*2}\n\n**Failed Tokens: **{len(variables.failed_tokens)}\n**Failed Boosts: **{len(variables.failed_tokens)*2}", color = 0x62f354))
    
    
clear()
keep_alive()
bot.run(config['bot_token'])
