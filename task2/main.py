from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://serbakmarana671:RjVz1wRKmAfcMz20@cluster0.xydhvoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.ds_dz02
# Send a ping to confirm a successful connection
#виведення всіх записів із колекції
def read_all():
    result = db.cats.find({})
    return [el for el in result]

#виведення записів із колекції за ім'ям
def read_name(name):
    result = db.cats.find_one({"name": name})
    if result:
        return result
    else:
        return("information does not exist")
#оновити вік кота за ім'ям    
def update_age_by_name(name, age):
    if db.cats.find_one({"name": name}):
        db.cats.update_one({"name": name}, {"$set": {"age": int(age)}})
        return ("updated")
    else:
        return ("name does not exist")
#додати нову характеристику до списку features кота за ім'ям
def update_features_by_name(name, featur):
    if db.cats.find_one({"name": name}) and type(featur) is str:
        features = db.cats.find_one({"name": name})['features']
        features.append(featur)
        db.cats.update_one({"name": name}, {"$set": {"features": features}})
        return ("updated")
    else:
        return ("name does not exist")
#видалення запису з колекції за ім'ям тварини
def delete_by_name(name):
    if db.cats.find_one({"name": name}):
        db.cats.delete_one({"name": name})
        return ("deleted")
    else:
        return ("name does not exist")
#видалення всіх записів із колекції
def delete_all():
    db.cats.delete_many({})
    return ("deleted")
    

if __name__ == "__main__":

    try:
        db.cats.insert_many(
            [
                {
                    "name": "Lama",
                    "age": 2,
                    "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                },
                {
                    "name": "Liza",
                    "age": 4,
                    "features": ["ходить в лоток", "дає себе гладити", "білий"],
                },
                {
                    "name": "barsik",
                    "age": 3,
                    "features": ["ходить в капці", "дає себе гладити", "рудий"],
                },               
            ]
        )
        #print(read_all())
        #print(read_name('barsik'))
        #print(update_age_by_name('barsik', 6))
        #print(update_features_by_name('barsik', "ласкавий"))
        #print(delete_by_name('barsik'))
        #print(delete_all())

        print("success")
    except Exception as e:
        print(e)