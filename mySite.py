from flask import Flask, render_template
from bitfinexApi import BitfinexApi

app = Flask(__name__)


btx = BitfinexApi()
# response = btx.getTicker('btcusd')
# print(response['mid'])


@app.route('/')
def home():
    symbols = btx.getSymbols()
    return render_template("home.html", symbols = symbols)

if __name__ == '__main__':
    app.run(debug=True, port=3001)