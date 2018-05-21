import pymongo


conn = pymongo.MongoClient('127.0.0.1', 27017)
db = conn.loversdb
lovers = db.lover
beloved = db.beloved
loverelation = db.loverelation
