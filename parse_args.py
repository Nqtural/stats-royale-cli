def leaderboard_range(value):
    ivalue = int(value)
    if ivalue <= 1 or ivalue > 2147483647:
        print("'-l' must be between 0 and 2147483647.")
        exit()
    return ivalue


def parse_args() -> dict:
    import argparse

    parser = argparse.ArgumentParser(
        prog = "Stats Royale CLI",
        description = "Fetches statistics about Clash Royale from the terminal"
    )

    type_of_request = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument(
        "-k", "--key",
        help = "Clash Royale API token (https://developer.clashroyale.com/#/getting-started)"
    )

    type_of_request.add_argument(
        "-t", "--tag",
        help = "Player tag"
    )

    type_of_request.add_argument(
        "-l", "--leaderboard",
        nargs = "?",
        const = 10,
        type = leaderboard_range,
        help = "Display last seasons Path of Legends leaderboard (default amount of spots: 10)"
    )

    args = parser.parse_args()

    if args.tag:
        args.tag = args.tag.upper()
        if "#" not in args.tag:
            args.tag = "#" + args.tag

    return {
        "api_key": args.key,
        "player_tag": args.tag,
        "leaderboard": args.leaderboard
    }
