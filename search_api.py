from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from whoosh import scoring
from whoosh.index import open_dir
import json

def searchAPI(query_str):
	ix = open_dir("indexdir")
 
	# query_str is query string
	#query_str = sys.argv[1]
 
	with ix.searcher(weighting=scoring.Frequency) as searcher:
		query=MultifieldParser(["title","content"], ix.schema).parse(query_str)
		results = searcher.search(query)
		print(results[0]['title'])
		print(results[0]['textdata'])
		return json.dumps({'file':results[0]['title'],'data':results[0]['textdata']})