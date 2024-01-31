import requests

API_KEY = "your api key"


class GetWords:
    def __init__(self):
        self.endpoint = "https://api.api-ninjas.com/v1/randomword"
        self.headers = {"X-Api-Key": API_KEY}
        self.text = ""

    def get_a_word(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()["word"]

    def get_200_words(self):
        count = 0
        while True:
            word = self.get_a_word()
            count += len(word)
            word = word.lower().ljust(len(word) + 1, " ")
            self.text += word
            if count >= 200:
                break
