def get_weather():

    import json
    from environs import Env
    import requests

    #Get configuration from .env
    config = Env()
    config.read_env()

    api_address = config.str("YA_ADDRESS")
    api_key = config.str("YA_API_KEY")

    lat = config.str("lat")
    lon = config.str("lon")

    #Prepear request
    req = f"{api_address}?lat={lat}&lon={lon}"

    #Send and write request
    # ans = requests.get(api_address, headers={'X-Yandex-API-Key': api_key})

    ###
    with open("./data/ans.txt", "r", encoding='UTF-8') as file:
        ans1 = file.read()
    print(ans1)
    ###

    #Parse answer
    ans_full = json.loads(ans1)

    return ans_full["fact"]["icon"]







