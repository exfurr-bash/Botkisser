import json
import os
import logging

karma_db = "karma.json"

if not os.path.exists(karma_db):
    with open(karma_db, "w") as f:
        json.dump({}, f)
        logging.info("Criado karma.json vazio.")

def alterar_karma(user_id, delta):
    with open(karma_db, "r") as f:
        data = json.load(f)
    data[str(user_id)] = data.get(str(user_id), 0) + delta
    with open(karma_db, "w") as f:
        json.dump(data, f)
    logging.info(f"Karma de {user_id} agora é {data[str(user_id)]}")
    return data[str(user_id)]

def meowify(text):
    logging.debug(f"Meowificando texto: {text}")
    return text.replace("r", "w").replace("l", "w") + " nya~"
