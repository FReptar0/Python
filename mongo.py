from pymongo import MongoClient

uri = "mongodb://localhost:27017"  # Connection string to the database

client = MongoClient(uri)  # Connect to the database
db = client['test-database']  # Database

collection = db['test-collection']  # Collection

obejeto = {"name": "Khan Doe", "age": 30, "address": "123 Main Street"}

collection.insert_one(obejeto)  # Insert a document


for document in collection.find():
    print(document)


""" Actualizar un documento """

collection.update_one({"name": "John Hoe"}, {"$set": {"age": 31}})

""" Imprimir todos los documentos de la colección """

for document in collection.find():
    print(document)

""" Eliminar un documento """

collection.delete_many({"name": "John Hoe"})

for document in collection.find():
    print(document)

