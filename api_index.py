import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys
 
def createSearchableData():   
 
    print('Indexing started...')
    schema = Schema(title=TEXT(stored=True),path=ID(stored=True),\
              content=TEXT,textdata=TEXT(stored=True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
 
    # Creating a index writer to add document as per schema
    ix = create_in("indexdir",schema)
    writer = ix.writer()
 
    filepaths = [os.path.join('swagger',i) for i in os.listdir('swagger')]
    for path in filepaths:
        fp = open(path,'r')
        print(path)
        text = fp.read()
        writer.add_document(title=path.split("/")[1], path=path,\
          content=text,textdata=text)
        fp.close()
    writer.commit()
 