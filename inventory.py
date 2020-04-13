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
        "spawnMax": 8
    },
    {
        "name": "dollar",
        "plural": "dollars",
        "sellPrice": 1,
        "sellable": False,
        "tradable": True,
        "spawnRate": 14.5,
        "spawnMin": 1,
        "spawnMax": 20,
        "craft": {

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
    }
]

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
        inv[pos][1] += quantity
    else:
        if (getFreeInventorySlot(discordID) == -1):
            return "No Space"
        else:
            inv[getFreeInventorySlot(discordID)][0] = item
            inv[getFreeInventorySlot(discordID)][1] = quantity
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

def removeFromInventory(discordID, item, quantity = "all"):
    inv = getInventory(discordID)
    try:
        pos = getItemExistsPosition(item)
    except:
        return "No item found."
    if (quantity == "all") or (quantity >= inv[pos][1]):
        inv[pos][0] = "empty"
        inv[pos][1] = 0
    else:
        inv[pos][1] -= quantity
    db.setData("users", "inventory='"+convertToDBInventory(inv)+"'", 'discordid=\''+str(discordID)+"'")
    return "success"

def getItemExistsPosition (discordID, item):
    inv = getInventory(discordID)
    for i in range(0, len(int)):
        if (inv[i][0] == item):
            return i
    return -1

def getFreeInventorySlot (discordID):
    inv = getInventory(discordID)
    for i in range(0, len(inv)):
        if (inv[i][0] == "empty"):
            return i
    return -1

