from flask import Flask
import json
from data import get_all_pe_info
from sz50 import get_top_50_code

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = get_top_50_code()
    pe = get_all_pe_info(result)
    # headers = ["Code", "PE", "PE_TTM", "PB"]
    # x = tabulate(pe, headers=headers, tablefmt="pretty")
    pe.sort(key=lambda x: x[1])
    return json.dumps(pe)


if __name__ == '__main__':
    app.run()
