def make_request(url: str, api_key: str) -> dict:
    import requests
    from check_response import check_response

    try:
        response = requests.get(
            url,
            headers = {"Authorization": f"Bearer {api_key}"}
        )

        if check_response(response.status_code):
            return response.json()

    except requests.ConnectionError:
        print("Error: No internet connection.")

    exit()
