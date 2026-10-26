class Codec:
    def __init__(self):
        self.urls = {}
        self.counter = 0

    def encode(self, longUrl):
        self.counter += 1
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        return self.urls[shortUrl]