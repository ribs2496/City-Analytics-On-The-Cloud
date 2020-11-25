#Team 58, Nitika Malhotra (1037082), Anupama Mampage(1102749), Ribhav Shridhar (1037144), Ronak Arvindkumar (1043591)


import couchdb

def storeInDB(tweets):
    couch = couchdb.Server()
    #db = couch.create('tweetsdata')
    db = couch['tweets']
    for tweet in tweets:
        print(tweet.text)
        doc = {'tweet':tweet.text}
        db.save(doc)