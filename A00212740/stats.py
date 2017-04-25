from flask import Flask, abort, request
import json

from comandos import get_all_stats

app = Flask(__name__)
api_url= '/v1.0'

@app.route(api_url+'/stats', methods=['GET'])
def read_stats():
  list = {}
  list["RAM total:"] = get_all_stats()[0]
  list["RAM en uso:"] = get_all_stats()[1]
  return json.dumps(list),200




if __name__=="__main__":

  app.run(host='0.0.0.0', port=8080, debug='True')
