import db, inventory, nations, work, ia, random



def gamble(discordID:int, amount:int):
    playerMoney = int(db.getData("dollars", "users", f"WHERE discordid='{discordID}'")[0])
    if playerMoney >= amount:
        victory = True if random.randint(0, 100) >= 51 else False
        if victory:
            if inventory.payDollars(-1, discordID, amount * 2):
                return f">>> The odds were in your favor. You won {amount * 2} dollars."
            else:
                return f">>> There was an error with payout you out."
        else:
            db.setData("users", f"dollars={playerMoney - amount}", f"discordid='{discordID}'")
            return f">>> You lost the gamble, losing {amount} dollars in the process."
    else:
        return ">>> You don't have enough to gamble."
    return ">>> Is your account set up? Try !xp"
