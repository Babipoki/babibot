import db


items = [
    {
        "name": "balloon",
        "plural": "balloons",
        "sellPrice": 3,
        "sellable": True,
        "tradable": True,
        "spawnRate": 40.5,
        "spawnMin": 1,
        "spawnMax": 8,
        "craft" : {

        }
    },
    {
        "name" : "bucket of latex",
        "plural" : "buckets of latex",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 32.15,
        "spawnMin": 1,
        "spawnMax": 2,
        "craft": {
            "bucket of latex":{
                "result": "balloon",
                "resultQuantity": 1,
                "inputQuantity": [1, 1],
                "itemsLost": ["bucket of latex", "bucket of latex"]
            }
        },
    },
    {
        "name": "oak log",
        "plural": "oak logs",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 11.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {
            "saw": {
                "result": "oak plank",
                "resultQuantity": 3,
                "inputQuantity": [1, 1],
                "itemsLost": ["oak log"]
            }
        }
    },
    {
        "name": "oak plank",
        "plural": "oak planks",
        "sellPrice": 2,
        "sellable": True,
        "tradable": True,
        "spawnRate": 2.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {

        }
    },
    {
        "name": "saw",
        "plural": "saws",
        "sellPrice": 2,
        "sellable": True,
        "tradable": True,
        "spawnRate": 0.45,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {
            "oak log": {
                "result": "oak plank",
                "resultQuantity": 3,
                "inputQuantity": [1, 1],
                "itemsLost": ["oak log"]
            }
        }
    },
    {
        "name": "iron ore",
        "plural": "ores of iron",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 13.25,
        "spawnMin": 1,
        "spawnMax": 4,
        "craft": {

        }
    },
    {
        "name": "furnace",
        "plural": "furnaces",
        "sellPrice": 14,
        "sellable": True,
        "tradable": True,
        "spawnRate": 0.05,
        "spawnMin": 1,
        "spawnMax": 1,
        "craft": {

        }
    },
    {
        "name": "teddy bear",
        "plural": "teddy bears",
        "sellPrice": 2,
        "sellable": True,
        "tradable": True,
        "spawnRate": 3.45,
        "spawnMin": 1,
        "spawnMax": 1,
        "craft":  {
            
        }
    }
]

'''
inventorySlots: [
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    },
    { 
        'item' : "",
        'quantity': 0
    } 
]
'''

# item1name::item1quantity||item2name...

def getInventory(discordID):
    discordID = '\'' + str(discordID) + '\''
    inv = db.getData("inventory", "users", "WHERE discordid=" + discordID)[0]
    slots = inv.split('||')
    for i in range(0, len(slots)):
        slots[i] = slots[i].split('::')
    return slots
    # slot[3][0] == name of the item // slot[3][1] == quiantityasy

def addToInventory(discordID, item, quantity):
    inv = getInventory(discordID)
    if (getItemExistsPosition(discordID, item) != -1):
        pos = getItemExistsPosition(discordID, item)
        inv[pos][1] = str(int(inv[pos][1]) + int(quantity))
    else:
        if (getFreeInventorySlot(discordID) == -1):
            return "No Space"
        else:
            inv[getFreeInventorySlot(discordID)][0] = item
            inv[getFreeInventorySlot(discordID)][1] = str(quantity)
    db.setData("users", "inventory='"+convertToDBInventory(inv)+"'", 'discordid=\''+str(discordID)+'\'')
    return "success"

def convertToDBInventory(arr):
    newArray = []
    for i in range(0, len(arr)):
        arr[i][1] = str(arr[i][1])
        newArray.append('::'.join(arr[i]))
    array2 = '||'.join(newArray)
    return array2

def listInventory(discordID):
    result = ">>> **INVENTORY**\n\n"
    inv = getInventory(discordID)
    for i in range(len(inv)):
        if (inv[i][0] != "empty"):
            result += f"**Slot {i}:** {inv[i][1]} x "
            if int(inv[i][1]) > 1:
                result += getPlural(inv[i][0])
            else:
                result += inv[i][0]
        else:
            result += f"**Slot {i}:** empty"
        result += "\n"
    return result
            

def getPlural(item):
    for i in range(0, len(items)):
        if (items[i]['name'] == item):
            return items[i]['plural']
    return item + "s"

def getSingular(item):
    for i in range(0, len(items)):
        if (items[i]['plural'] == item):
            return items[i]['name']
    return item

def removeFromInventory(discordID, item, quantity = "all"):
    inv = getInventory(discordID)
    try:
        pos = getItemExistsPosition(discordID, getSingular(item))
    except:
        raise Exception("No item found.")
        return "No item found."
    if (quantity == "all") or (quantity >= inv[pos][1]):
        inv[pos][0] = "empty"
        inv[pos][1] = str(0)
    else:
        inv[pos][1] = str(int(inv[pos][1]) - int(quantity))
    db.setData("users", "inventory='"+convertToDBInventory(inv)+"'", 'discordid=\''+str(discordID)+"'")
    return "success"

def getItemExistsPosition (discordID, item):
    inv = getInventory(discordID)
    for i in range(0, len(inv)):
        if (inv[i][0] == item) or (inv[i][0] == getPlural(item)) or (inv[i][0] == getSingular(item)):
            return i
    return -1

def getFreeInventorySlot (discordID):
    inv = getInventory(discordID)
    for i in range(0, len(inv)):
        if (inv[i][0] == "empty"):
            return i
    return -1

def getItemPrice (item):
    itemid = -1
    for i in range(0, len(items)):
        if (items[i]['name'] == item) or (items[i]['plural'] == item):
            itemid = i
    if (i != -1):
        return items[i]['sellPrice']
    else:
        raise Exception("Item price not found.")

def sellItem (discordID, item, quantity):
    dID = discordID
    discordID = "'" + str(discordID) + "'"
    currentMoney = db.getData("dollars", "users", f"WHERE discordid={discordID}")[0]
    itemPrice = getItemPrice(getSingular(item))
    if getItemExistsPosition(dID, getSingular(item)) == -1:
        return False
    if (itemPrice > 0):
        try:
            removeFromInventory(dID, getSingular(item), quantity)
        except:
            return False
        finally:
            profit = getItemPrice(item) * int(quantity)
            newMoney = currentMoney + profit
            db.setData("users", f"dollars={str(newMoney)}", f"discordid={discordID}")
        
        return True
    else:
        return False

def giveItem (fromDiscordID, toDiscordID, quantity, item):
    if (fromDiscordID == toDiscordID):
        return ">>> Like... literally how retarded are you? Do you have brain? Do you possess a single digit of IQ? What's your problem?"
    if (getItemExistsPosition(fromDiscordID, item) != -1):
        if (getFreeInventorySlot(toDiscordID) != -1):
            giverSlot = getItemExistsPosition(fromDiscordID, item)
            giverInventory = getInventory(fromDiscordID)
            if (giverInventory[giverSlot][1] >= quantity):
                removeFromInventory(fromDiscordID, item, quantity)
                addToInventory(toDiscordID, item, quantity)
                return True
            else:
                return f">>> You don't have that many {getPlural(item)}."
        else:
            return f">>> Target doesn't have enough inventory slots or doesn't have an account set up. Tell them to type !xp?"
    else:
        return f">>> You don't have that item, or you followed wrong syntax. Use !give [mention] [qt] [item]."
            