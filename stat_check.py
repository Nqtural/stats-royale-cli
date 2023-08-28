def get_player_info(args: dict) -> dict:
    from request import make_request

    return sort_stats(
        make_request(
            f"https://api.clashroyale.com/v1/players/{args['player_tag'].replace('#', '%23')}",
            args["api_key"]
        ),
        args["player_tag"]
    )


def get_deck(stats: dict):
    from decks import match_deck
    return match_deck([card["name"] for card in stats["currentDeck"]])


def get_league(league: int, rank: int) -> str:
    league_name = [
        "None",
        "Challanger I",
        "Challanger II",
        "Challanger III",
        "Master I",
        "Master II",
        "Master III",
        "Champion",
        "Grand Champion",
        "Royal Champion",
        "Ultimate Champion"
    ][league]
    return league_name if league_name != "Ultimate Champion" else league_name + f": {rank}"


def format_clan_role(role: str) -> str:
    return {
        "coLeader": " (Co-leader)",
        "elder": " (Elder)",
        "leader": " (Leader)",
        "member": " (Member)"
    }[role]


def get_clan(stats: dict) -> str:
    try:
        return stats["clan"]["name"] + format_clan_role(stats["role"])
    except KeyError:
        return "No Clan"


def sort_stats(stats: dict, tag: str) -> dict:
    return {
        "name": stats["name"],
        "wins": stats["wins"] + stats["threeCrownWins"],
        "losses": stats["losses"],
        "clan": get_clan(stats),
        "trophies": stats["trophies"],
        "best_trophies": stats["bestTrophies"],
        "deck": get_deck(stats),
        "league": get_league(
            stats["currentPathOfLegendSeasonResult"]["leagueNumber"],
            stats["currentPathOfLegendSeasonResult"]["rank"]
        ),
        "best_league": get_league(
            stats["bestPathOfLegendSeasonResult"]["leagueNumber"],
            stats["bestPathOfLegendSeasonResult"]["rank"]
        )
    }
