import random 
class Codec:
    def __init__(self):
        self.d = {} 
        self.counter = 0 
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = str(self.counter + 1)
        self.d[shortUrl] = longUrl
        return shortUrl
 
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))