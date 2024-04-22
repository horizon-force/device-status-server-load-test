import decimal
import random

import requests
import json

url = "http://localhost:8081/api/v0/device"

# parameters
max_lat = 41.7352477033675
min_lng = -123.26118133993271
min_lat = 39.605246914995405
max_lng = -120.71525031453376
percent_fire = 10
percent_disabled = 2

# TODO: execute on separate threads to simulate more realistic scenario
for i in range(50000):
    scale = 1000000
    lat = float(decimal.Decimal(random.randrange(int(min_lat * scale), int(max_lat * scale))) / scale)
    lng = float(decimal.Decimal(random.randrange(int(min_lng * scale), int(max_lng * scale))) / scale)
    is_fire = random.randint(0, 100) < percent_fire
    is_disabled = random.randint(0, 100) < percent_disabled
    payload = json.dumps({
        "id": f'device-load-test-{i}',
        "name": "north cal",
        "lat": lat,
        "lng": lng,
        "error": 53,
        "status_code": "Fire" if is_fire else "NoFire",
        "disabled": is_disabled
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
