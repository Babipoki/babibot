import datetime, db, random

jobs = {
    '0': {
        'name': 'Janitor',
        'minXP': 0,
        "salary": 2,
        "xpPerWork": 1,
        "customEvents": ["You cleaned dog's poop today.", "You had fun."]
    },
    '1': {
        'name': 'Cookie Factory Worker',
        'minXP': 5,
        'salary': 4,
        'xpPerWork': 2,
        "customEvents": ["You slipped on the floor.", "You ate a cookie without anyone noticing."]
    }
}

def workedToday(discordID):
    discordID = '\'' + str(discordID) + '\''
    lastWorked = datetime.datetime.strftime(db.getData('lastWorked', 'users', 'WHERE discordid=' + discordID)[0], '%Y-%m-%d')
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    return True if (lastWorked == now) else False


def goToWork(discordID):
    discordID = '\'' + str(discordID) + '\''
    jobID = str(db.getData('jobid', 'users', 'WHERE discordid=' + discordID)[0])
    timesWorked = db.getData('timesWorked', 'users', 'WHERE discordid=' + discordID)[0]
    currentXP = db.getData('experience', 'users', 'WHERE discordid=' + discordID)[0]
    jobTitle = jobs[jobID]['name']
    jobSalary = jobs[jobID]['salary']
    customEvent = random.choice(jobs[jobID]["customEvents"])
    currentDollars = db.getData('dollars', 'users', 'WHERE discordid=' + discordID)[0]
    newDollars = currentDollars + jobSalary
    db.setData('users', 'dollars=' + str(newDollars), "discordid=" + discordID)
    db.setData('users', 'lastWorked=\'' + datetime.datetime.now().strftime("%Y-%m-%d") + "'", "discordid=" + discordID)
    db.setData('users', 'timesWorked=' + str(timesWorked + 1), "discordid=" + discordID)
    db.setData('users', 'experience=' + str(currentXP + jobs[jobID]['xpPerWork']), "discordid=" + discordID)
    return f"You have worked as a {jobTitle}. {customEvent} You earned {str(jobSalary)} dollars and {str(jobs[jobID]['xpPerWork'])} XP."

def getDollars(discordID):
    discordID = '\'' + str(discordID) + '\''
    result = str(db.getData("dollars", "users", "WHERE discordid=" + discordID)[0])
    if result == "No Results":
        return "You have no account set up. Type !xp to begin."
    else:
        return f'You have {result} dollars in your pocket.'