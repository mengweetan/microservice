
import requests
import json, csv
import pymongo
import urllib

'''
CLIENT  = pymongo.MongoClient("mongodb://admin:password!@cluster0-shard-00-00-5u88h.gcp.mongodb.net:27017,cluster0-shard-00-01-5u88h.gcp.mongodb.net:27017,cluster0-shard-00-02-5u88h.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority", connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)



db  = CLIENT.vv
'''

mongo_uri = "mongodb+srv://dbuser:" + urllib.parse.quote("xyzabc") + "@cluster0.pibqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

db = client.psp

l  = [{'name': 'kevin', 'gender':  'male', 'ID': 1},{'name': 'mengwee', 'gender':  'male', 'ID': 2}]
l1 = {'name': 'fiona', 'gender':  'female', 'ID': 2}
#f = db.members.insert_many(l)
f = db.members.insert_one(l1)
print (f)
