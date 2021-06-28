import requests
from flask import Flask
import json

# function to use requests.post to make an API call to the subgraph url
def run_query(q):

    # endpoint where you are making the request
    response = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
                            '',
                            json={'query': q})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))

def prepareQuery(pair):
    #The Graph query - get liquidity per pair
    LIQUIDITY_QUERY = """{pair(id: "replacebypairaddress"){token0{id symbol} token1 {id symbol} reserve0 reserve1 reserveUSD token0Price token1Price }}"""
    fixed_query = LIQUIDITY_QUERY.replace("replacebypairaddress", pair)
    return fixed_query

app = Flask(__name__)
@app.route('/v2/pair/<address>', methods=['GET'])
def index(address):
    query = prepareQuery(address)
    result = run_query(query)
    return result["data"]
app.run()