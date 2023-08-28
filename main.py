def main() -> ():
    from parse_args import parse_args
    args: dict = parse_args()

    try:
        if args["api_key"]:
            with open("api_key.txt", "w") as keyfile:
                keyfile.writelines(args["api_key"])
        else:
            with open("api_key.txt", "r") as keyfile:
                args["api_key"] = keyfile.readlines()[0]

    except FileNotFoundError:
        print("Error: Please provide an API key using '-k' or '--key'")
        exit()

    if args["player_tag"]:
        from stat_check import get_player_info
        player_info: dict = get_player_info(args = args)

        print(f"\n\033[1;33m       .           \033[1;37m{player_info['name']}")
        print(f"\033[1;33m+-----´ `-----+    \033[0;37m-------")
        print(f"\033[1;33m|  .   .   .  |    \033[1;34mClan     \033[1;37m:\033[0m {player_info['clan']}")
        print(f"\033[1;33m|  |\_/ \_/|  |    \033[1;34mWins     \033[1;37m:\033[0m {player_info['wins']}")
        print(f"\033[1;33m|  |       |  |    \033[1;34mLosses   \033[1;37m:\033[0m {player_info['losses']}")
        print(f"\033[1;33m|   \.---./   |    \033[1;34mDeck     \033[1;37m:\033[0m {player_info['deck']}")
        print(f"\033[1;33m `-.       .-´     \033[1;34mTrophies \033[1;37m:\033[0m {player_info['trophies']} ({player_info['best_trophies']})")
        print(f"\033[1;33m    `-._.-´        \033[1;34mLeague   \033[1;37m:\033[0m {player_info['league']} ({player_info['best_league']})\n")

    elif args["leaderboard"]:
        from leaderboard import get_leaderboard
        leaderboard = get_leaderboard(args["api_key"], args["leaderboard"])
        for player in leaderboard:
            print(f"\n{str(player['rank']) + '.': <3} {player['name']} ({player['tag']})")
            try:
                print(f"    {player['clan']['name']}")
            except KeyError:
                print("    No Clan")
        print("")


if __name__ == "__main__":
    main()
