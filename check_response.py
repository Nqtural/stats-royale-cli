def check_response(status_code: int) -> bool:
    if status_code == 200:
        return True
    elif status_code == 400:
        print("Error: Client provided incorrect parameters for the request.")
    elif status_code == 403:
        print("Error: Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.")
    elif status_code == 404:
        print("Error: Resource was not found.")
    elif status_code == 429:
        print("Error: Request was throttled, because amount of requests was above the threshold defined for the used API token.")
    elif status_code == 500:
        print("Error: Unknown error happened when handling the request.")
    elif status_code == 503:
        print("Error: Service is temprorarily unavailable because of maintenance.")

    return False
