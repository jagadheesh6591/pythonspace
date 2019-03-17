import time
import json
import base64
from flask import Flask,request
import api_index as indexing
import search_api as search

app = Flask(__name__)

@app.route("/api/search",methods=['GET'])
def apiSearch():
  print('started api search ...')
  searchKey = request.args.get('key')
  searchResult = search.searchAPI(searchKey)
  print('#######')
  #print(result)
  data = request.json
  print(data)
  #response = json.dumps({'encodedImage':'hey jaga','searchKey':searchKey})
  return searchResult
  
@app.route("/api/startIndex",methods=['GET'])
def apiIndex():
  indexing.createSearchableData()
  response = json.dumps({'status':'success','description':'indexing successful'})
  return response


if __name__ == '__main__':
  #run_simple('localhost', 9000, app)
  indexing.createSearchableData()
  app.run(debug=True, use_reloader=True)

	




