def get_weather(api_address, api_key, lat, lon):
    
    import json
    import requests

    #Prepear request
    req = f"{api_address}?lat={lat}&lon={lon}"

    #Send and write request
    ans = requests.get(req, headers={'X-Yandex-API-Key': api_key})
    
    #Parse answer
    ans_full = json.loads(ans.text)
    return ans_full["fact"]["icon"]
