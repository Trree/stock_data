import json

from flask import Flask

from pe import get_stock_pe
from query_type import QueryType
from sz50 import get_top_code

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/sz50')
def hello_world():
    result = get_top_code(QueryType.SZ50)
    pe = get_stock_pe(result)
    return json.dumps(pe)

@app.route('/hs300')
def hello_world():
    result = get_top_code(QueryType.HS300)
    pe = get_stock_pe(result)
    return json.dumps(pe)

if __name__ == '__main__':
    app.run()
