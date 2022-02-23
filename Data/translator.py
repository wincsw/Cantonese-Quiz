import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "87b67b4542ea4e749cd9549e09a2c324"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "eastasia"

path = "/translate"
constructed_url = endpoint + path


def translate(string_lst, from_lang, to_lang_lst):
    params = {
        "api-version": "3.0",
        "from": from_lang,
        "to": to_lang_lst,
    }  # "from": "en", "to": ["yue", "zh-Hans"]}
    constructed_url = endpoint + path

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Ocp-Apim-Subscription-Region": location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    # You can pass more than one object in body.
    # body = [{"text": string}]
    body = []
    for s in string_lst:
        body.append({"text": s})

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    """
    print(
        json.dumps(
            response,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
            separators=(",", ": "),
        )
    )
    """
    result = []
    for i in range(len(string_lst)):
        word = []
        for j in range(len(to_lang_lst)):
            # print(i, j)
            # print(response[0]["translations"][i]["text"])
            word.append(response[i]["translations"][j]["text"])
        result.append(word)

    return result

