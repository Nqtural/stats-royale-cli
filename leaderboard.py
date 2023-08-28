def get_leaderboard(api_key: str) -> list:
    from request import make_request

    latest_season = make_request(
        "https://api.clashroyale.com/v1/locations/global/seasonsV2",
        api_key
    )["items"][-1]["uniqueId"]

    return make_request(
        f"https://api.clashroyale.com/v1/locations/global/pathoflegend/{latest_season}/rankings/players?limit=10",
        api_key
    )["items"]
