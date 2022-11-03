from pymongo import MongoClient
client = MongoClient('mongodb+srv://pablaw:1239282@studylog.xy5ijs9.mongodb.net/?retryWrites=true&w=majority')
db = client.pablaw

sel_movie = db.movies.find_one({'title':'가버나움'})

same_movies =list(db.movies.find({'star':sel_movie['star']},{'_id':False}))

# db.movies.update_one({'name':'가버나움'},{'$set':{'star':'0'}})
# db.movies.update_one({'name':'그린 북'},{'$set':{'star':'0'}})
for movie in same_movies:
    db.movies.update_one({'title': movie['title']}, {'$set': {'star': '0'}})

print(db.movies.find_one({'title':'가버나움'}), db.movies.find_one({'title':'그린 북'}))