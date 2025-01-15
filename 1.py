import chromadb
chromaClient=chromadb.Client()
collection=chromaClient.get_or_create_collection('test_collection')

documents=[
    {"id":"doc1",
     "text":"hello world"},
    {"id":"doc2",
     "text":"how are you today"},
    {"id":"doc 3",
     "text":"goodbye see you later"}
]

for i in documents:
    collection.upsert(ids=i['id'],documents=i['text'])

query='hello'
results=collection.query(
    query_texts=[query],
    n_results=2
)

print(results)