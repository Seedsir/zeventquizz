from constants import CONNEXION_URL, ACCESS_TOKEN, CLIENT_ID
import requests
import random
import string

class User:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.profile_image = None

    def connect_user(self):
        state = self.generate_random_string()
        nonce = self.generate_random_string()
        url = f"{CONNEXION_URL}&state={state}&nonce={nonce}"
        return url

    def get_user(self):
        data = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Client-Id": CLIENT_ID
        }
        req = requests.get("https://api.twitch.tv/helix/users", headers=data)
        if req.status_code == 200:
            self.user_id = req.json()["data"][0].get("id")
            self.username = req.json()["data"][0].get("display_name")
            self.profile_image = req.json()["data"][0].get("profile_image_url")
            if self.profile_image is None:
                # TODO trouver une url de logo par default
                pass

    def generate_random_string(self):
        length = random.randint(10, 15)
        choises = string.ascii_lowercase + string.digits
        return ''.join(random.choice(choises) for i in range(length))


class Player(User):

    def __init__(self):
        super(Player, self).__init__()


class Streamer(User):

    def __init__(self):
        super(Streamer, self).__init__()
