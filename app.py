from flask import Flask, jsonify, render_template, request
from web3 import Web3

app = Flask(__name__)

# Connect to an Ethereum node (e.g., Infura)
infura_url = 'https://mainnet.infura.io/v3/INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Ethereum address of the logged-in user
logged_in_user = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/balance', methods=['GET'])
def get_balance():
    global logged_in_user
    if logged_in_user is None:
        return jsonify({'error': 'User not logged in'})
    
    # Get balance of the logged-in user's Ethereum address
    balance = web3.eth.get_balance(logged_in_user)
    
    # Convert balance from Wei to Ether
    balance_eth = web3.fromWei(balance, 'ether')
    
    return jsonify({'balance': balance_eth})

@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    global logged_in_user
    if logged_in_user is None:
        return jsonify({'error': 'User not logged in'})
    
    data = request.get_json()
    recipient = data['recipient']
    amount = float(data['amount'])
    
    #transaction logic
    
    return jsonify({'message': 'Transaction sent successfully'})

@app.route('/login', methods=['POST'])
def login():
    global logged_in_user
    data = request.get_json()
    eth_address = data.get('eth_address')
    if eth_address:
        logged_in_user = eth_address
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid Ethereum address'})

if __name__ == "__main__":
    app.run(debug=True)
