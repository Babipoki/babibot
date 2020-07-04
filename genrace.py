import random

vonvadiaRaces = { # World , Junjian, Feretti
        "Human / Torri": [500000000, 37000000, 49000000],
        "Human / Junni": [125000000, 47000000, 13000000],
        "Human / Abbi": [175000000, 2000000, 7000000],
        "Human / Spersi": [85000000, 800000, 5500000],
        "Lafahl / Kosenfolk": [146000000, 500000, 1500000],
        "Lafahl / Rotalifolk": [395800000, 23000000, 28500000],
        "Akura / Paleskin": [76000000, 1500000, 1750000],
        "Akura / Brownskin": [57000000, 800000, 1250000], 
        "Akura / Blueskin": [35000000, 500000, 15000],
        "Bangula / Redskin": [7500000, 50000, 5000],
        "Bangula / Greenskin": [5400000, 27000, 2000], 
        "Bangula / Blackskin": [3000000, 20000, 500],
        "Bangula / Yellowskin": [2200000, 12000, 50],
        "Elvaan / Light Kin": [480000000, 24000000, 26500000],
        "Elvaan / Dark Kin": [315000000, 28000000, 18000000],
        "Burmecci / Greyfur": [9000000, 20000, 150000],
        "Burmecci / Whitefur": [1000000, 1200, 3000],
        "Mandirigorri / Greenleaf": [5000000, 45000, 95000],
        "Mandirigorri / Goldleaf": [50000, 50, 175],
        "Numoi / Pink-nose": [400000, 100, 1000],
        "Numoi / Plain-nose": [340000, 350, 500],
        "Paliccae / Blackfur": [4000000, 150000, 500000],
        "Paliccae / Asatti": [2300000, 42000, 135000],
        "Quvi / Redtongue": [400000, 5, 12],
        "Quvi / Goldentongue": [20000, 1, 3],
        "Rogado / Of the Aether": [52000000, 1500000, 2750000],
        "Rogado / Of the Void": [49000000, 1900000, 575000],
        "Seafarer / Chosen": [12000000, 50000, 15],
        "Seafarer / Unchosen": [35000000, 130000, 100],
        "Toniki / Dungeonkeeper": [400000, 1450, 13500],
        "Toniki / Towerkeeper": [280000, 2400, 11850],
        "Mithra / Aetherskin": [153000000, 1500000, 6500000],
        "Mithra / Voidskin": [142000000, 3400000, 3400000],
        "Galiva / -": [2500000, 5000, 35000],
        "Youdel / Furskin": [45000000, 25000, 1750000],
        "Youdel / Nakedbody": [15000000, 35000, 1500000],
        "Dwarf / Mountain": [7500000, 4000, 350000],
        "Dwarf / Wild": [12550000, 16000, 450000]
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
