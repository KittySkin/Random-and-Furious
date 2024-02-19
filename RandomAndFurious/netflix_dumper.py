"""
Made using the API from https://apilayer.com/marketplace/unogs-api.
"""
import json
import requests
import api_keys


def main():
    url = "https://api.apilayer.com/unogs/search/titles?type=movie&order_by=title&limit=100000&country_list=21"
    """
    The API Key is stored on my end on a non uploaded non indexed script that provides a function that returns the key
    as a string. Is not the ideal way to handle it and should be encrypted, but this is a non-critical app.
    def api_key_get():
        return "your key here" 
    """
    payload = {}
    headers = {
        "apikey": f"{api_keys.api_key_get()}"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        json_result = json.loads(result)
        with open('result.json', 'w') as outfile:
            json.dump(json_result, outfile)
    else:
        print(status_code)


if __name__ == "__main__":
    main()
