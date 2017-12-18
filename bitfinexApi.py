import requests
import json

class BitfinexApi():
    def __init__(self):
        self.apiUrl = 'https://api.bitfinex.com/v1'

    def getTicker(self, symbol):
        url = self.apiUrl + '/pubticker/' + symbol
        response = requests.get(url)
        return json.loads(response.text)

    def getSymbols(self):
        url = self.apiUrl + '/symbols'
        response = requests.get(url)
        return json.loads(response.text)

