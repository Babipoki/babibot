import wand.image
import io, db
import xml.etree.ElementTree as ET
import datetime

nations = [
    {
        'name': "Babilandia", #id 0
        'color': "#009245", #green
        'joinable': True,
        'defaultProvince': 1,
        'deJureProvinces': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    {
        'name': "Republic of Boys", #id 1
        'color': "#FF0000", #red
        'joinable': True,
        'defaultProvince': 13,
        'deJureProvinces': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    },
    {
        'name': "Balloon Kingdom", #id 2
        'color': "#0071bc", #blue
        'joinable': True,
        'defaultProvince': 25,
        'deJureProvinces': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    },
    {
        'name': "Unowned", #id 3
        'color': "#666", #grey
        'joinable': False,
        'defaultProvince': -2,
        'deJureProvinces': []
    }
]

path = "/usr/bin/"





def makeMap():
    ''' Create the map and post it on the channel. '''
    ET.register_namespace('', "http://www.w3.org/2000/svg")
    owners = getProvinceOwnerships()
    print (str(owners))
    dom = ET.parse(path+"Babi Island.svg")
    root = dom.getroot()


    for i in range(1, len(owners) - 1):
        g = root.find(".//{http://www.w3.org/2000/svg}g[@id='Prov-" +str(i) +"']")
        if g != None:
            if g.find(".//{http://www.w3.org/2000/svg}polygon") != None:
                g.find(".//{http://www.w3.org/2000/svg}polygon").set('style', f"fill: {nations[owners[i]]['color']};fill-opacity: 0.75;stroke: #000;stroke-miterlimit: 10;stroke-width: 2px")
    dom.write(path+"babi.svg")
    svg_file = open(path + "babi.svg", "rb")
    print (svg_file)
    with wand.image.Image(blob =svg_file.read(), format="svg") as image:
        png_image = image.make_blob("png")
    with open(path + "Babi_Island.png", "wb") as out:
        out.write(png_image)
    

def getProvinceOwnerships():
    owners = [-1]
    allOwners = db.getData("owner", "provinces", "", True)
    for i in range(0, len(allOwners)):
        allOwners[i] = allOwners[i][0]
    owners = owners + allOwners
    return owners


def getProvinceName(provinceID):
    return db.getData("provinceName", "provinces", f"WHERE provinceID={provinceID}")[0]

def joinNation(discordID, nationID):
    nationID = int(nationID)
    if nationID not in range(0, 3):
        return [False, "Invalid nation ID."]
    nationality = db.getData("nationality", "users", f"WHERE discordid='{str(discordID)}'")[0]
    lastSwitchedNations = datetime.datetime.strftime(db.getData('lastNationSwitch', 'users', f"WHERE discordid='{str(discordID)}'")[0]
    , '%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    if (lastSwitchedNations == today):
        return [False, ">>> You've already switched nations today."]
    else:
        if (int(nationality) != nationID):
            provinceID = nations[nationID]['defaultProvince']
            provinceName = getProvinceName(provinceID)
            if db.setData("users", f"province='{str(provinceID)}'", f"discordid='{str(discordID)}'"): 
                db.setData("users", f'lastNationSwitch=\'{datetime.datetime.now().strftime("%Y-%m-%d")}\'', f"discordid='{str(discordID)}'")
                db.setData("users", f'nationality={nationID}', f"discordid='{str(discordID)}'")
                return [True, f">>> You have been accepted to be a citizen of {nations[nationID]['name']} and moved to the province of {provinceName}."]
            else:
                return [False, ">>> There was an error. Did you set up your account with !xp command?"]
            
        else:
            return [False, f">>> You're already a citizen of {nations[nationID]['name']}."]

def getPlayerNation(discordID):
    nationality = db.getData("nationality", "users", f"WHERE discordid='{str(discordID)}'")[0]
    try:
       return f"You are aligned with the nation of **{nations[int(nationality)]['name']}**."
    except:
        return "Error. Are you signed up?"

def getPlayerProvince(discordID):
    try:
        provinceID = db.getData("province", "users", f"WHERE discordid='{str(discordID)}'")[0]
        return [True, getProvinceName(provinceID)]
    except:
        return [False, "Error."]