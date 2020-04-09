import discord, random, string, mysql.connector, sys, asyncio, datetime, logging, os, time
from mysql.connector import errorcode
from systemd.journal import JournalHandler

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

"""
cnx = mysql.connector.connect(
            host='localhost',
            database='babibot',
            user='babipoki',
            password=dbpwd
        )


cursor = cnx.cursor()
"""
query = ("")
xp = 0


TOKEN = token

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'whats up fagggot, {0.author.mention}'.format(message)
        #await client.send_message(message.channel, msg)
        await message.channel.send(msg)

    if (message.content.startswith('!newnickname') or message.content.startswith('!nn')):
        nicknames1 = ["Cockflipper", "Succotash", "Fucking", "Derpy", "Alcoholic", "Intolerant", "Appealing", "Indonesian", "Seaside", "Thrifty", "Unenjoyable", "Stupid", "Naked", "Orchestrated", "Unidentified", "Stupid", "Unused", "Untitled", "Boring"]
        nicknames2 = ["Charmander", "Bumbaloo", "Crocodile Hunter", "Puppy", "Radio Show Host", "Echidna", "Nut", "Dick", "Palm Tree", "Gangster", "Balloon", "Condomface", "Whippersnapper", "FUUUUUUUUUCK", "NPC", "side-quest NPC", "Lifeguard", "Donut", "Officer of Justice"]
        oneWordNicknames = ["Dorito", "Rex", "Ahhhhhhhhhh", "?XD", "Ponies :D", "♥ Anal ♥", "♥ S E B A S T I A N ♥", "fucking" + randomString(10), "xXxUnTiTlEdAnGeLxXx", "PUSSY!!!!!!!!", "Belend", "UNLICENSED ASS KICKER/KISSER", "Wuwu & Nillump"]
        insults = ["sucker", "boomer", "asshole", "cuck", "pipsqueak", "dickwad"]
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
        


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    await client.get_channel(397817169951588354).send('Bot ready. Restart/startup successful.')
    await client.get_channel(397817169951588354).send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Monster prep every 10 minutes
    '''while True:
        await client.get_channel(397817169951588354).send('The monster is growing in size... He\'ll kill us all!')
        time.sleep(600)'''
    await monsterGrow()

async def monsterGrow():
    await client.get_channel(397817169951588354).send('The monster is growing in size... He\'ll kill us all!')
    await asyncio.sleep(600)
    await monsterGrow()

def getDBdata(dbSelect, dbFrom, conditons = ''):
    query = f'SELECT {dbSelect} FROM {dbFrom} {conditons}'
    cnx = mysql.connector.connect(
            host='localhost',
            database='babibot',
            user='babipoki',
            password=dbpwd
        )
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount == 0:
        return 'No Results'
    else:
        return cursor.fetchall()[0]

client.run(TOKEN)
    
