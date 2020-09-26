import requests
from time import sleep


BOT_URL = "https://api.telegram.org/bot1365153079:AAHbSwyixHD38PfbRxpuuYKKNfUQuZCYhts/"


old_ids = []

while True:
    updates = requests.get(BOT_URL + "getUpdates").json()["result"]
    new_updates = []
    for i_update in range(len(updates)):
        if updates[i_update]["update_id"] in old_ids:
            continue
        old_ids.append(updates[i_update]["update_id"])
        new_updates.append(updates[i_update])

    for event in new_updates:
        message = event["message"]
        username = message["from"]["id"]
        answer = message["text"][::-1]
        body = {"text": answer, "chat_id": username}
        requests.post(BOT_URL + "sendMessage", data=body)
    sleep(1)

