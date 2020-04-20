import db, random


items = [
    {
        "name": "balloon",
        "plural": "balloons",
        "sellPrice": 3,
        "sellable": True,
        "tradable": True,
        "spawnRate": 13.5,
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
        "spawnRate": 12.15,
        "spawnMin": 1,
        "spawnMax": 2,
        "craft": {
            "bucket of latex":{
                "result": "balloon",
                "resultQuantity": 1,
                "inputQuantity": [1, 1]
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
                "inputQuantity": [1, 0]
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
                "inputQuantity": [0, 1]
            }
        }
    },
    {
        "name": "iron ore",
        "plural": "ores of iron",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 11.25,
        "spawnMin": 1,
        "spawnMax": 4,
        "craft": {
            "furnace": {
                "result": "iron ingot",
                "resultQuantity": 1,
                "inputQuantity": [2, 0]
            }
        }
    },
    {
        "name": "furnace",
        "plural": "furnaces",
        "sellPrice": 14,
        "sellable": True,
        "tradable": True,
        "spawnRate": 1.25,
        "spawnMin": 1,
        "spawnMax": 1,
        "craft": {
            "iron ore": {
                "result": "iron ingot",
                "resultQuantity": 1,
                "inputQuantity": [0, 2]
            }
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
    },
    {
        "name": "iron ingot",
        "plural": "iron ingots",
        "sellPrice": 3,
        "sellable": True,
        "tradable": True,
        "spawnRate": 7.15,
        "spawnMin": 1,
        "spawnMax": 3,
        "craft": {

        }
    },
    {
        "name": "popped balloon",
        "plural": "popped balloons",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 2.15,
        "spawnMin": 1,
        "spawnMax": 13,
        "craft": {
            "furnace": {
                "result": "bucket of latex",
                "resultQuantity": 1,
                "inputQuantity": [4, 0]
            }
        }
    },
    {
        "name": "needle",
        "plural": "needles",
        "sellPrice": 1,
        "sellable": True,
        "tradable": True,
        "spawnRate": 4.95,
        "spawnMin": 1,
        "spawnMax": 2,
        "craft": {
            "balloon": {
                "result": "popped balloon",
                "resultQuantity": 1,
                "inputQuantity": [0, 1]
            }
        }
    },
    {
        "name": "XP bottle",
        "plural": "XP bottles",
        "sellPrice": 15,
        "sellable": True,
        "tradable": True,
        "spawnRate": 1.05,
        "spawnMin": 1,
        "spawnMax": 2,
        "craft": {

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
        if (items[i]['plural'] == item) or (items[i]['name'] == item):
            return items[i]['name']
    return item

def removeFromInventory(discordID, item, quantity = "all"):
    inv = getInventory(discordID)
    try:
        pos = getItemExistsPosition(discordID, getSingular(item))
    except:
        raise Exception("No item found.")
        return "No item found."
    if (quantity == "all") or (quantity >= int(inv[pos][1])):
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
    item = getSingular(item)
    for i in range(0, len(items)):
        if (items[i]['name'] == item):
            itemid = i
    if (itemid != -1):
        return items[itemid]['sellPrice']
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
            removeFromInventory(dID, getSingular(item), int(quantity))
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

def payDollars (fromDiscordID:int, toDiscordID, quantity):
    giverDollars = 0
    if (toDiscordID == fromDiscordID):
        return ">>> You're trying to pay to yourself. That's not even how Patreon works."
    if fromDiscordID != -1:
        giverDollars = int(db.getData("dollars", "users", f"WHERE discordid='{str(fromDiscordID)}'")[0])
    else:
        giverDollars = 9999999
    recipientDollars = int(db.getData("dollars", "users", f"WHERE discordid='{str(toDiscordID)}'")[0])
    if (giverDollars >= int(quantity)):
        if fromDiscordID != -1:
            db.setData("users", f"dollars={str(giverDollars - int(quantity))}", f"discordid='{str(fromDiscordID)}'")
        db.setData("users", f"dollars={str(recipientDollars + int(quantity))}", f"discordid='{str(toDiscordID)}'")
        return True
    else:
        return ">>> You don't have enough dollars to pay. Have you tried contacting Babibank?"
    return "Error. Get help."
            

def getItemID(item):
    for i in range(len(items)):
        if (items[i]['name'] == item):
            return i
    return -1

# CRAFTING

def combine(discordID, item1, item2):
    inv = getInventory(discordID)
    item1 = getSingular(item1)
    item2 = getSingular(item2)
    item1slot = getItemExistsPosition(discordID, item1)
    item2slot = getItemExistsPosition(discordID, item1)
    item1ID = getItemID(item1)
    item2ID = getItemID(item2)
    freeSlot = getFreeInventorySlot(discordID)
    if (item1slot != -1 and item2slot != -1):
        if (freeSlot != -1):
            if item2 in items[item1ID]['craft']:
                craft = items[item1ID]['craft'][item2]
                resultItem = craft['result']
                resultQuantity = craft['resultQuantity']
                inputQuantity = craft['inputQuantity']
                #check if you have enough of input items
                # combine quantity if two items are the same
                if (item1 == item2):
                    newInputQuantity = [inputQuantity[0]+inputQuantity[1], 0]
                else:
                    newInputQuantity = inputQuantity
                hasEnoughItems = True if (int(inv[item1slot][1]) >= newInputQuantity[0] and int(inv[item2slot][1]) >= newInputQuantity[1]) else False

                if hasEnoughItems:
                    removeFromInventory(discordID, item1, inputQuantity[0])
                    removeFromInventory(discordID, item2, inputQuantity[1])
                    addToInventory(discordID, resultItem, resultQuantity)
                    return [True, "CRAFT_SUCCESSFUL", inputQuantity, resultQuantity, resultItem]
                return [False, "You don't have enough of the items to make the combination."]
            return [False, "Combination not found."]
        return [False, "No free slot found. Free up some space."]
    return [False, "Items you're combining are not found."]


def useItem(discordID, item):
    item = getSingular(item)
    if (getItemExistsPosition(discordID, item) != -1):
        # BALLOON
        if (item == "balloon"):
            luck = random.randint(0, 100)
            if 0 <= luck <= 4:
                removeFromInventory(discordID, item, 1)
                addToInventory(discordID, "popped balloon", 1)
                return [True, "You tried to play with the balloon, but a bully came over and popped it."]
            elif 5 <= luck <= 45:
                removeFromInventory(discordID, item, 1)
                addToInventory(discordID, "popped balloon", 1)
                return [True, "You were playing with your balloon, but suddenly it hit the grass and popped."]
            elif 46 <= luck <= 100:
                return [True, "Yay! You had fun playing with your balloon!"]
        # XP bottle
        if (item == "XP bottle"):
            randomXP = random.randint(1, 6)
            playerXP = db.getData("experience", "users", f"discordid='{str(discordID)}'")[0]
            removeFromInventory(discordID, item, 1)
            db.setData("users", f"experience={playerXP+randomXP}", f"discordid='{str(discordID)}'")
            return [True, f"You drank the XP potion and gained {randomXP} XP from it."]
        return [True, f"Nothing interesting happened from using your {item}."]
    return [False, "You don't have such an item to use it."]