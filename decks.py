def match_deck(deck: list) -> str:
    if all(card in deck for card in [
        "Hog Rider", "Musketeer", "Ice Golem", "Skeletons",
        "Ice Spirit", "Cannon", "The Log", "Fireball"]):
        return "Hog 2.6"
    elif all(card in deck for card in [
        "Goblin Barrel", "Knight", "Princess", "Goblin Gang",
        "Ice Spirit", "Inferno Tower", "The Log", "Rocket"]):
        return "Classic Log Bait"
    elif all(card in deck for card in [
        "Goblin Barrel", "Knight", "Princess", "Goblin Gang",
        "Ice Spirit", "Inferno Tower", "The Log", "Fireball"]):
        return "Classic Log Bait Fireball"
    elif all(card in deck for card in [
        "Goblin Barrel", "Knight", "Princess", "Goblin Gang",
        "Ice Spirit", "Tesla", "The Log", "Rocket"]):
        return "Classic Log Bait Tesla"
    elif all(card in deck for card in [
        "Goblin Barrel", "Princess", "Goblin Gang", "Rascals"]):
        return "Log Bait Rascals"
    elif all(card in deck for card in [
        "Battle Ram", "P.E.K.K.A", "Magic Archer", "Bandit",
        "Royal Ghost"]):
        return "P.E.K.K.A Bridge Spam"
    elif all(card in deck for card in [
        "Battle Ram", "P.E.K.K.A", "Minions", "Bandit",
        "Royal Ghost"]):
        return "P.E.K.K.A Bridge Spam Minions"
    elif all(card in deck for card in [
        "Miner", "Wall Breakers", "Magic Archer", "Tornado"]):
        return "Miner Wall Breakers Magic Archer"
    elif all(card in deck for card in [
        "Giant", "Graveyard"]):
        return "Giant Graveyard"
    elif all(card in deck for card in [
        "Graveyard", "Poison"]):
        return "Graveyard Poison"
    elif all(card in deck for card in [
        "Hog Rider", "Earthquake"]):
        return "Hog EQ"
    elif all(card in deck for card in [
        "X-Bow", "Knight", "Archers", "Skeletons",
        "Ice Spirit", "Tesla", "The Log", "Fireball"]):
        return "3.0 X-Bow Cycle"
    elif all(card in deck for card in [
        "Goblin Barrel", "Skeleton Barrel"]):
        return "Double Barrel Log Bait"
    elif all(card in deck for card in [
        "Goblin Barrel", "Princess", "Rocket"]) and (
            "Goblin Gang" in deck or "Goblins" in deck or "Guards" in deck
        ):
        return "Log Bait"
    elif all(card in deck for card in [
        "Goblin Barrel", "Princess", "Lightning"]) and (
            "Goblin Gang" in deck or "Goblins" in deck or "Guards" in deck
        ):
        return "Log Bait Lightning"
    elif all(card in deck for card in [
        "Goblin Barrel"]) and (
            "Goblin Gang" in deck or "Goblins" in deck or "Guards" in deck
        ) and (
            "Princess" in deck or "Dart Goblin" in deck or "Fire Cracker" in deck):
        return "Log Bait"
    elif all(card in deck for card in [
        "Hog Rider", "The Log"]
        ) and (
            "Cannon" in deck or "Bomb Tower" in deck):
        return "Hog Cycle"
    elif all(card in deck for card in [
        "Hog Rider", "The Log", "Tesla"]):
        return "Hog Cycle Tesla"
    elif all(card in deck for card in [
        "X-Bow", "Ice Wizard", "Ice Golem", "The Log",
        "Mega Minion", "Rocket", "Skeletons", "Tornado"]):
        return "Ice X-Bow"
    elif all(card in deck for card in [
        "X-Bow", "Tornado", "The Log", "Knight",
        "Mega Minion"]):
        return "X-Bow Control"
    elif all(card in deck for card in [
        "Miner", "Mega Knight"]):
        return "Miner MK"
    elif all(card in deck for card in [
        "Balloon", "Lumberjack", "Freeze"]):
        return "LumberLoon Freeze"
    elif all(card in deck for card in [
        "Balloon", "Lumberjack"]):
        return "LumberLoon"
    elif all(card in deck for card in [
        "Elixir Golem", "Battle Healer", "Rage"]):
        return "E-Golem"
    elif all(card in deck for card in [
        "Miner", "Wall Breakers"]):
        return "Miner Wall Breakers"
    elif all(card in deck for card in [
        "Lava Hound", "Balloon"]):
        return "LavaLoon"
    elif all(card in deck for card in [
        "Miner", "Balloon"]):
        return "Balloon Cycle"
    elif all(card in deck for card in [
        "Hog Rider", "Executioner", "Tornado"]):
        return "Hog ExeNado"
    elif all(card in deck for card in [
        "Hog Rider", "Mega Knight"]):
        return "Hog MK"
    elif all(card in deck for card in [
        "Miner", "Mortar", "Minion Horde"]):
        return "Miner Mortar Horde"
    elif all(card in deck for card in [
        "Miner", "Mortar"]):
        return "Miner Mortar"
    elif all(card in deck for card in [
        "Royal Giant", "Mother Witch", "Skeleton King"]):
        return "RG Skelly King Mother Witch"
    elif all(card in deck for card in [
        "Royal Giant", "Mother Witch"]):
        return "RG Mother Witch"
    elif all(card in deck for card in [
        "Royal Giant", "Lightning", "Skeleton King"]):
        return "RG Skelly King Lightning"
    elif all(card in deck for card in [
        "Royal Giant", "Furnace"]):
        return "RG Control"
    elif all(card in deck for card in [
        "Royal Giant", "Lightning"]):
        return "RG Lightning"
    elif all(card in deck for card in [
        "Royal Giant", "Earthquake"]):
        return "RG EQ"
    elif all(card in deck for card in [
        "Royal Giant"]):
        return "RG"
    elif all(card in deck for card in [
        "Royal Hogs", "Royal Recruits"]):
        return "Hogs Recruits"
    elif all(card in deck for card in [
        "Royal Hogs", "Earthquake"]):
        return "Hogs EQ"
    elif all(card in deck for card in [
        "Three Musketeers", "Elixir Pump"]):
        return "3M"
    elif all(card in deck for card in [
        "X-Bow", "Elixir Pump"]):
        return "X-Bow Pump"
    elif all(card in deck for card in [
        "Royal Hogs"]):
        return "Royal Hogs"
    elif all(card in deck for card in [
        "Miner", "Executioner", "Tornado"]):
        return "Miner ExeNado"
    elif all(card in deck for card in [
        "Lava Hound", "Miner"]):
        return "LavaMiner"
    elif all(card in deck for card in [
        "Miner", "Poison"]):
        return "Miner Poison"
    elif all(card in deck for card in [
        "Sparky", "Goblin Giant"]):
        return "Sparky Goblin Giant"
    elif all(card in deck for card in [
        "Sparky"]):
        return "Sparky"
    elif all(card in deck for card in [
        "Goblin Drill"]):
        return "Goblin Drill"
    elif all(card in deck for card in [
        "Electro Giant", "Mirror"]):
        return "E-Giant Mirror"
    elif all(card in deck for card in [
        "Electro Giant"]):
        return "E-Giant"
    elif all(card in deck for card in [
        "Golem", "Night Whitch"]):
        return "Golem Beatdown"
    elif all(card in deck for card in [
        "Golem", "Lumberjack"]):
        return "Golem Lumberjack"
    elif all(card in deck for card in [
        "Golem", "Executioner"]):
        return "Golem Exe"
    elif all(card in deck for card in [
        "Golem"]):
        return "Golem"
    elif all(card in deck for card in [
        "Ram Rider", "Bandit"]):
        return "Ram Rider Bridge Spam"
    elif all(card in deck for card in [
        "Ram Rider", "Mega Knight"]):
        return "Ram Rider MK"
    #elif all(card in deck for card in [
    #    "", "", "", "",
    #    "", "", "", ""]):
    #    return ""
    else:
        return "Unknown"
