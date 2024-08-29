from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual CryptoCompare API key
API_KEY = 'abdaa96754e58d4a92b0d63c47ed61294ad6e63a065ca33105abcb20b1aa9064'

def get_multiple_crypto_prices(crypto_ids):
    symbols = ",".join(crypto_ids)
    url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={symbols}&tsyms=USD&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    cryptos = ['BTC', 'ETH', 'DOGE']
    prices = get_multiple_crypto_prices(cryptos)
    return render_template('index.html', prices=prices)

@app.route('/api/prices')
def api_prices():
    cryptos = ['BTC', 'ETH', 'DOGE']
    prices = get_multiple_crypto_prices(cryptos)
    return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
