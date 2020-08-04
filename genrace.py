import random

vonvadiaRaces = { # World , Junjian, Feretti, Ekkionlor, Toras, Rotali, Eq (equal chance)
        "Human / Torri": [500000000, 37000000, 49000000, 21000000, 76000000, 23000000, 10],
        "Human / Junni": [125000000, 47000000, 13000000, 5000000, 7500000, 3500000, 10],
        "Human / Abbi": [175000000, 2000000, 7000000, 6500000, 28000000, 43000000, 10],
        "Human / Spersi": [85000000, 800000, 5500000, 6500000, 2000000, 2250000, 10],
        "Lafahl / Kosenfolk": [146000000, 500000, 1500000, 1800000, 2500000, 7000000, 10],
        "Lafahl / Rotalifolk": [395800000, 23000000, 28500000, 19000000, 22000000, 104000000, 10],
        "Akura / Paleskin": [76000000, 1500000, 1750000, 2000000, 750000, 550000, 10],
        "Akura / Brownskin": [57000000, 800000, 1250000, 1350000, 850000, 2500000, 10], 
        "Akura / Blueskin": [35000000, 500000, 15000, 5000, 1200000, 200000, 10],
        "Bangula / Redskin": [7500000, 50000, 5000, 3500, 25000, 3000, 10],
        "Bangula / Greenskin": [5400000, 27000, 2000, 1500, 17000, 15000, 10], 
        "Bangula / Blackskin": [3000000, 20000, 500, 20, 35000, 2500, 10],
        "Bangula / Yellowskin": [2200000, 12000, 50, 5, 5000, 100, 10],
        "Elvaan / Light Kin": [480000000, 24000000, 26500000, 29200000, 15000000, 2500000, 10],
        "Elvaan / Dark Kin": [315000000, 28000000, 18000000, 19500000, 7500000, 2000000, 10],
        "Burmecci / Greyfur": [9000000, 20000, 150000, 340000, 100000, 15000, 10],
        "Burmecci / Whitefur": [1000000, 1200, 3000, 50000, 15000, 25000, 10],
        "Mandirigorri / Greenleaf": [5000000, 45000, 95000, 30000, 75000, 25000, 10],
        "Mandirigorri / Goldleaf": [50000, 50, 175, 300, 500, 25, 10],
        "Numoi / Pink-nose": [400000, 100, 1000, 3400, 1500, 700, 10],
        "Numoi / Plain-nose": [340000, 350, 500, 3000, 3500, 3500, 10],
        "Paliccae / Blackfur": [4000000, 150000, 500000, 300000, 150000, 100000, 10],
        "Paliccae / Asatti": [2300000, 42000, 135000, 240000, 50000, 78500, 10],
        "Quvi / Redtongue": [400000, 5, 12, 25, 1000, 250, 10],
        "Quvi / Goldentongue": [20000, 1, 3, 7, 50, 5, 10],
        "Rogado / Of the Aether": [52000000, 1500000, 2750000, 3450000, 1500000, 750000, 10],
        "Rogado / Of the Void": [49000000, 1900000, 575000, 3050000, 500000, 25000, 10],
        "Seafarer / Chosen": [12000000, 50000, 15, 20, 150000, 120000, 10],
        "Seafarer / Unchosen": [35000000, 130000, 100, 150, 185000, 125000, 10],
        "Toniki / Dungeonkeeper": [400000, 1450, 13500, 8000, 5000, 145000, 10],
        "Toniki / Towerkeeper": [280000, 2400, 11850, 2500, 1500, 80000, 10],
        "Mithra / Aetherskin": [153000000, 1500000, 6500000, 4500000, 17000000, 3500000, 10],
        "Mithra / Voidskin": [142000000, 3400000, 3400000, 4500000, 3000000, 500000, 10],
        "Galiva / -": [2500000, 5000, 35000, 200,000, 15000, 2500, 10],
        "Youdel / Furskin": [45000000, 25000, 1750000, 42000000, 1000000, 580000, 10],
        "Youdel / Nakedbody": [15000000, 35000, 1500000, 10000000, 1200000, 950000, 10],
        "Dwarf / Mountain": [7500000, 4000, 350000, 220000, 100000, 25000, 10],
        "Dwarf / Wild": [12550000, 16000, 450000, 350000, 25000, 750000, 10],
        "Namazu / -": [5000000, 3500, 50, 5000, 750000, 25000, 10]
}


def getRace (location):
    race = ""
    raceCol = -1
    maxPop = 0
    locationName = ""
    if location == "world":
        raceCol = 0
        maxPop = 500000000
        locationName = "Vonvadia"
    elif location == "junjian":
        raceCol = 1
        maxPop = 47000000
        locationName = "Junjian Empire"
    elif location == "feretti":
        raceCol = 2
        maxPop = 49000000
        locationName = "Feretti Kingdom"
    elif location == "ekkionlor":
        raceCol = 3
        maxPop = 52000000
        locationName = "Ekkionlor"
    elif location == "toras":
        raceCol = 4
        maxPop = 113500000
        locationName = "Republic of Toras"
    elif location == "rotali":
        raceCol = 5
        maxPop = 111000000
        locationName = "Rotali Sultanate"
    elif location == "eq":
        raceCol = 6
        maxPop = 10
        locationName = "Equalchance"
    else:
        return [False, "The nation does not exist."]

    rNum = random.randint(0, maxPop)
    rRaceID = random.randint(0, len(list(vonvadiaRaces.keys()))-1)

    while (vonvadiaRaces[list(vonvadiaRaces.keys())[rRaceID]][raceCol] < rNum):
        rNum = random.randint(0, maxPop)
        rRaceID = random.randint(0, len(list(vonvadiaRaces.keys()))-1)

    if (vonvadiaRaces[list(vonvadiaRaces.keys())[rRaceID]][raceCol] > rNum):
        race = list(vonvadiaRaces.keys())[rRaceID]


    return [True, "Your generated character is **{race}**. Their population in {ln} is {mp}.".format(race=race, ln=locationName, mp=vonvadiaRaces[list(vonvadiaRaces.keys())[rRaceID]][raceCol]) ]
