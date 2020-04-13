import datetime, db, random

jobs = [
    {
        'name': 'Janitor',
        'minXP': 0,
        "salary": 2,
        "xpPerWork": 1,
        "customEvents": ["You cleaned dog's poop today.", "You had fun.", "You used extra bleach today.", "You spent entire day binge-watching Bleach anime.", "You cleaned your boss's shoes.", "You had to clean up all the popped balloons from the party.", "The day was boring as heck."]
    },
    {
        'name': 'Cookie Factory Worker',
        'minXP': 5,
        'salary': 4,
        'xpPerWork': 2,
        "customEvents": ["You slipped on the floor.", "You ate a cookie without anyone noticing.", "You stole a bunch of cookies for your starving family.", "You banged your co-worker at the metro station bathroom.", "You came home very tired."]
    },
    {
        'name': "Train Conductor",
        'minXP': 15,
        'salary': 6,
        'xpPerWork': 3,
        'customEvents': ["You were offered a balloon in exchange for not fining a ticketless boy.", "You had a boring day.", "Nothing interesting happened."]
    },
    {
        'name': 'Balloon Vendor',
        'minXP': 35,
        'salary': 8,
        'xpPerWork': 4,
        'customEvents': ["You exchanged a popped balloon for a new one, but then you noticed a pattern.", "You had a blast... popping all the balloons at the end of the shift.", "What a boring day..."]
    },
    {
        'name': 'Traveling Balloon Merchant',
        'minXP': 50,
        'salary': 10,
        'xpPerWork': 5,
        'customEvents': ["You traveled to five cities today to bring joy to all the children.", "You were arrested by the gang of children and had to pay a fine of 15 balloons you were supposed to sell today."]
    }
]

def workedToday(discordID):
    discordID = '\'' + str(discordID) + '\''
    lastWorked = datetime.datetime.strftime(db.getData('lastWorked', 'users', 'WHERE discordid=' + discordID)[0], '%Y-%m-%d')
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    return True if (lastWorked == now) else False


def goToWork(discordID):
    discordID = '\'' + str(discordID) + '\''
    jobID = int(db.getData('jobid', 'users', 'WHERE discordid=' + discordID)[0])
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

# Get how many dollars you have, in a full string.
def getDollars(discordID):
    discordID = '\'' + str(discordID) + '\''
    result = str(db.getData("dollars", "users", "WHERE discordid=" + discordID)[0])
    if result == "No Results":
        return "You have no account set up. Type !xp to begin."
    else:
        return f'You have {result} dollars in your pocket.'

# Apply to a job. Returns a string whether it's successful or not.
def applyToJob(discordID, job):
    discordID = '\'' + str(discordID) + '\''
    jobID = getJobID(job)
    currentJobID = int(db.getData('jobid', 'users', 'WHERE discordid=' + discordID)[0])
    currentXP = db.getData('experience', 'users', 'WHERE discordid=' + discordID)[0]
    try: 
        neededXP = jobs[jobID]['minXP']
    except:
        return "What are you even applying to, dumbass? Check !jobs, if you're such a smartass."
    if (jobID == currentJobID):
        return f"You are already employed as {job}."
    else:
        if (currentXP < neededXP):
            return f"You don't have enough experience to apply to a position of {job}. Get lost, loser."
        else:
            #Succeed at job application
            db.setData("users", f"jobid={jobID}", f"discordid={discordID}")
            return f"You have been accepted to the position of {job}. Congratulations!"
    

def getJobID(jobStr):
    for i in range(0, len(jobs)):
        if jobs[i]['name'] == jobStr:
            return i
    return "N/A"


def getCurrentJob(discordID):
    discordID = '\'' + str(discordID) + '\''
    jobid = db.getData("jobid", "users", "WHERE discordid=" + discordID)[0]
    if jobid == "No Results":
        return "You have no account set up. Type !xp to begin."
    else:
        return f'Your current job is {jobs[jobid]["name"]}.'