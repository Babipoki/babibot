import discord, random, string, mysql.connector, sys, asyncio, datetime, logging, os, time, battler, db, work, helpCmds, inventory, ia, nations, re
from mysql.connector import errorcode
from systemd.journal import JournalHandler
from discord.ext import commands

bot = commands.Bot(command_prefix='$$')

path = '/usr/bin/'
token_file = os.path.join(path, "token.txt")
pwd_file = os.path.join(path, "dbpw.txt")

with open(token_file, 'r') as f:
    token = f.read().replace('\n', '')
with open(pwd_file, 'r') as f:
    dbpwd = f.read().replace('\n', '')

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

client = discord.Client()
log = logging.getLogger('demo')
log.addHandler(JournalHandler())
log.setLevel(logging.INFO)
log.debug("Logger started.")

query = ("")
xp = 0

currentDrop = "N/A"
currentDropQuantity = 0
dropChannelID = 563429049767165974 # #spam

TOKEN = token

async def dm_user(userid, message=None):
    user = client.get_user(int(userid))
    await discord.abc.Messageable.send(user, message)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if isinstance(message.channel, discord.DMChannel):
        await client.get_channel(397817169951588354).send('Message received from['+ str(message.author) +']: ' + message.content)
    
    if message.content.startswith('hello'):
        msg = 'whats up fagggot, {0.author.mention}'.format(message)
        await message.channel.send(msg)
    
    if message.content.startswith('!dm') and message.author.id == 149887314254888960:
        await dm_user(message.content.split(' ')[1], ' '.join(message.content.split(' ')[2:]))

    if (message.content.startswith('!newnickname') or message.content.startswith('!nn')):
        nicknames1 = ["Cockflipper", "Succotash", "Fucking", "Derpy", "Alcoholic", "Intolerant", "Appealing", "Indonesian", "Seaside", "Thrifty", "Unenjoyable", "Stupid", "Naked", "Orchestrated", "Unidentified", "Stupid", "Unused", "Untitled", "Boring", "Cricketsniffing", "Disposable", "Deplorable", "Soviet", "Triggered", "Republican", "Cute", "Limitless", "Sobbing"]
        nicknames2 = ["Charmander", "Bumbaloo", "Crocodile Hunter", "Puppy", "Radio Show Host", "Echidna", "Nut", "Dick", "Palm Tree", "Gangster", "Balloon", "Condomface", "Whippersnapper", "FUUUUUUUUUCK", "NPC", "side-quest NPC", "Lifeguard", "Donut", "Officer of Justice", "Buttsniffer", "Tree Branch", "Bunny Balloon", "Door Frame", "Screwdriver", "Mouse Balloon", "Cockroach", "Gorilla", "Sandshrew", "Scorbunny", "Pikachu", "Sobble"]
        oneWordNicknames = ["Dorito", "Rex", "Ahhhhhhhhhh", "?XD", "Ponies :D", "♥ Anal ♥", "♥ S E B A S T I A N ♥", "fucking" + randomString(10), "xXxUnTiTlEdAnGeLxXx", "PUSSY!!!!!!!!", "Belend", "UNLICENSED ASS KICKER/KISSER", "Wuwu & Nillump", "actually belend", "fart XDDDDDDDDDDDDDDDDDD", "xXxUnfisted FisterxXx", 'xXxXgLoRiOuSpRiNcEoFdArKnEsSXxXx', "Sexmaster Extraordinaire", "Fucky Sucky", "Gender Gap", "D R A G O N  O F  J U S T I C E"]
        insults = ["sucker", "boomer", "asshole", "cuck", "pipsqueak", "dickwad", "edgelord", "Mr Crangis McBasketball"]
        nickname = ""
        if random.randint(0, 1) == 1:
            nickname = random.choice(oneWordNicknames)
        else:
            nickname = random.choice(nicknames1) + ' ' + random.choice(nicknames2)
        msg = '{0.author.mention}, your new nickname is '.format(message) + nickname +'. Enjoy, ' + random.choice(insults) +'.'
        await message.channel.send(msg)
        await message.author.edit(nick = nickname)
    if (message.content.startswith('!xp')):
        xp = 0
        cnx = mysql.connector.connect(
            host='localhost',
            database='babibot',
            user='babipoki',
            password=dbpwd
        )
        cursor = cnx.cursor(buffered=True)
        log.info("Setting up query...")
        xpQuery = 'SELECT experience FROM users WHERE discordid = %(did)s LIMIT 0,1'
        log.info("Executing the query...")
        cursor.execute(xpQuery, {'did': str(message.author.id)})
        
        if cursor.rowcount:
            result = cursor.fetchone()[0]
            xp = result
            await message.channel.send("You have " + str(xp) + " XP.")
            log.info(cursor.statement)
            log.info("Rowcount: " + str(cursor.rowcount))
            log.info(str(result))
        else:
            await message.channel.send("There's no entry for your user. Your ID is: " + str(message.author.id))
            createEntryQuery = 'INSERT INTO users (id, experience, discordid) VALUES (%(id)s,0, %(did)s)'
            await message.channel.send("Creating entry...")
            cursor.execute(createEntryQuery, {'id': random.randint(1, 10000000),
                'did': str(message.author.id)})
            cnx.commit()
            xpQuery = 'SELECT experience FROM users WHERE discordid = %(did)s LIMIT 0,1'
            log.info("Executing the query...")
            cursor.execute(xpQuery, {'did': str(message.author.id)})
            if (cursor.rowcount):
                await message.channel.send("New entry has been created.")
                result = cursor.fetchone()[0]
                xp = result
                await message.channel.send("You have " + str(xp) + " XP.")
            else:
                await message.channel.send("There was an error creating your entry.")
        if (cnx.is_connected()):
            cnx.close()
            cursor.close()
    if message.content.startswith("!work"):
        print ("You typed !work")
        if work.workedToday(message.author.id):
            print(work.workedToday(message.author.id))
            await message.channel.send("You have already worked today.")
        else:
            print(work.workedToday(message.author.id))
            reply = "Penis"
            reply = work.goToWork(message.author.id)
            print (reply)
            await message.channel.send(reply)
    if message.content.startswith("!dollars"):
        reply = work.getDollars(message.author.id)
        await message.channel.send(reply)
    if message.content.startswith("!jobs"):
        reply = ">>> "
        for i in range(0, len(work.jobs)):
            reply += "**" + work.jobs[i]['name'] + "** | Salary: " + str(work.jobs[i]['salary']) + " | Min XP: " + str(work.jobs[i]['minXP']) + "\n"
        await message.channel.send(reply)
    if message.content.startswith("!apply"):
        reply = ""
        reply = work.applyToJob(message.author.id, ' '.join(message.content.split(' ')[1:]))
        await message.channel.send(reply)
    if message.content == "!job" or message.content == "!myjob":
        await message.channel.send(work.getCurrentJob(message.author.id))
    if message.content == "!help":
        reply = ">>> "
        for i in range(0, len(helpCmds.generalCommands)):
            reply += f"**{helpCmds.generalCommands[i][0]}** - {helpCmds.generalCommands[i][1]}\n"
        await message.channel.send(reply)
    if message.content == "!inventory" or message.content == "!i" or message.content == "!inv":
        try:
            reply = inventory.listInventory(message.author.id)
        except:
            reply = "You don't have an account set up. Type !xp to begin."
        await message.channel.send(reply)
    if message.content == "!sell":
        await message.channel.send("Please use the following format: ``!sell [quantity] [item]``")
    elif message.content.startswith("!sell"):
        try:
            quantity = int(message.content.split(' ')[1])
            item = inventory.getSingular(' '.join(message.content.split(' ')[2:]))
            itemPrice = inventory.getItemPrice(item) * int(quantity)
            result = inventory.sellItem(message.author.id, item, quantity)
            if (result == True):
                numerator = f"{ia.indefinite_article(item)} {item}" if quantity == 1 else f"{quantity} {inventory.getPlural(item)}"
                dollarTag = "dollar" if itemPrice == 1 else "dollars"
                await message.channel.send(f'>>> Successfully sold {numerator} for {str(itemPrice)} {dollarTag}.')
            else:
                numerator = f"{ia.indefinite_article(item)} {item}" if quantity == 1 else f"{quantity} {inventory.getPlural(item)}"
                await message.channel.send(f">>> Error. Couldn't sell {numerator}.")
        except ValueError as e:
            await message.channel.send("Invalid syntax. Please use the following format: ``!sell [quantity] [item]``")
            print (e)
    if message.content == "!pickup" or message.content == "!p" or message.content == "!pick" or message.content == "!grab":
        if message.channel.id == dropChannelID:
            await pickDropUp(message.author.id)
        else:
            await message.channel.send("You can only pick up items in the drops channel.")
    if message.content.startswith("!give"):
        if message.content == "!give":
            await message.channel.send("The syntax is !give [mention] [quantity] [item].")
        else:
            quantity = int(message.content.split(" ")[2])
            item = " ".join(message.content.split(" ")[3:])
            reply = inventory.giveItem(message.author.id, message.mentions[0].id, str(quantity), item)
            if (reply == True):
                numerator = f"{ia.indefinite_article(item)} {inventory.getSingular(item)}" if quantity == 1 else f"{quantity} {inventory.getPlural(item)}"
                await message.channel.send(f">>> Successfully given {numerator} to {message.mentions[0].mention}.")
            else:
                await message.channel.send(reply)
    if message.content.startswith("!pay"):
        if message.content == "!pay":
            await message.channel.send("The syntax is !pay [mention] [amount].")
        else:
            quantity = int(message.content.split(" ")[2])
            reply = inventory.payDollars(message.author.id, message.mentions[0].id, str(quantity))
            if (reply == True):
                numerator = f"a dollar" if quantity == 1 else f"{quantity} dollars"
                await message.channel.send(f">>> You have paid {message.mentions[0].mention} a hefty sum of {numerator}.")
            else:
                await message.channel.send(reply)
    if message.content == "!map":
        nations.makeMap()
        #e = discord.Embed()
        #e.set_image(url="https://babipoki.com/characters/Babi%20Island.svg")
        file = discord.File(path+"Babi_Island.png", filename="island.png")
        #await message.channel.send(embed=e)
        await message.channel.send(file=file)
    if message.content.startswith("!combine"):
        regex = r"!combine (.*) with (.*)"
        m = re.search(regex, message.content)
        item1 = m.group(1)
        item2 = m.group(2)
        reply = inventory.combine(message.author.id, item1, item2)
        if reply[0] == True:
            if item1 == item2:
                combinationText = f"{str(int(reply[2][0] + reply[2][1]))} {inventory.getPlural(item1)}"
            else:
                combinationText = f"{reply[2][0]} {inventory.getSingular(item1) if reply[2][0] == 1 else inventory.getPlural(item1)} and {reply[2][1]} {inventory.getSingular(item2) if reply[2][1] == 1 else inventory.getPlural(item2)}"
            if reply[3] == 1:
                creation = f"{ia.indefinite_article(reply[4])} {inventory.getSingular(reply[4])}"
            else:
                creation = f"{reply[3]} {inventory.getPlural(reply[4])}"
            newReply = f">>> Successfully combined {combinationText} to create **{creation}**."
            await message.channel.send(newReply)
        if (message.content == "!use"):
                await message.channel.send(">>> Invalid syntax. Please use !combine <item name> with <second item name>.")
        elif (reply[0] == False):
            await message.channel.send(">>>" + reply[1])
    if message.content.startswith("!use"):
        regex = r"!use (.*)"
        m = re.search(regex, message.content)
        item = m.group(1)
        reply = inventory.useItem(message.author.id, item)
        if (reply[0] == True):
            # Space in here in case I add something later.
            await message.channel.send(">>> " + reply[1])
        else:
            await message.channel.send(">>> " + reply[1])
        if (message.content == "!use"):
            await message.channel.send(">>> Invalid syntax. Please use !use <item name>.")
    if message.content.startswith("!join"):
        if message.content == "!join":
            file = discord.File(path+"welcome.jpg", filename="welcome.jpg")
            await message.channel.send(file=file)
        else:
            nationID = int(message.content.split(" ")[1])
            reply = nations.joinNation(message.author.id, nationID)
            await message.channel.send(reply[1])
    if message.content == "!nation":
        reply = nations.getPlayerNation(message.author.id)
        await message.channel.send(reply)
    if message.content == "!location" or message.content == "!province":
        prov = nations.getPlayerProvince(message.author.id)
        if prov[0] == True:
            await message.channel.send(f">>> You are currently located in **{prov[1]}**.")
        else:
            await message.channel.send(f">>> There was an error somewhere. Are you signed up properly?")





        


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


    
    await client.get_channel(397817169951588354).send('Bot ready. Restart/startup successful.')
    await client.get_channel(397817169951588354).send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #await monsterGrow()
    await dropEnumerator()

'''
async def monsterGrow():
    await client.get_channel(397817169951588354).send('The monster is growing in size... He\'ll kill us all!')
    await asyncio.sleep(600)
    await monsterGrow()
''' 




def getNextDropItem():
    dropping = [-1, -1]
    dropItem = -1
    while dropItem == -1:
        randomChance = random.random() * 100
        randItemID = random.randint(0, len(inventory.items) - 1)
        spawnRate = inventory.items[randItemID]['spawnRate']
        if (randomChance <= spawnRate):
            dropItem = randItemID
    dropQuantity = random.randint(inventory.items[dropItem]['spawnMin'], inventory.items[dropItem]['spawnMax'])
    dropping = [dropItem, dropQuantity]
    return dropping
                

async def dropItem():
    global currentDrop
    global currentDropQuantity
    drop = getNextDropItem()
    currentDrop = inventory.items[drop[0]]['name']
    currentDropQuantity = drop[1]
    if currentDropQuantity == 1:
        await client.get_channel(dropChannelID).send(f">>> A **{currentDrop}** has dropped on the ground. Type !pickup to pick it up.")
    else:
        await client.get_channel(dropChannelID).send(f">>> {str(currentDropQuantity)} **{inventory.getPlural(currentDrop)}** dropped on the ground. Type !pickup to pick them up.")

async def pickDropUp(discordID):
    global currentDrop, currentDropQuantity
    if currentDrop != "N/A":
        try:
            inventory.addToInventory(discordID, currentDrop, currentDropQuantity)
            if currentDropQuantity == 1:
                await client.get_channel(dropChannelID).send(f">>> You picked up a {currentDrop}.")
                currentDrop = "N/A"
                currentDropQuantity = 0
            else:
                await client.get_channel(dropChannelID).send(f">>> You picked up {str(currentDropQuantity)} {inventory.getPlural(currentDrop)}.")
                currentDrop = "N/A"
                currentDropQuantity = 0
        except ValueError as e:
            print (e)
            print (currentDrop)
            print (currentDropQuantity)
            await client.get_channel(dropChannelID).send(f">>> There's no space in your inventory.")
    else:
        await client.get_channel(dropChannelID).send(f">>> There's nothing to pick up.")

async def dropEnumerator():
    global currentDrop
    while True:
        await asyncio.sleep(random.randint(35, 450))
        if (currentDrop == "N/A"):
            await dropItem()

client.run(TOKEN)
    
