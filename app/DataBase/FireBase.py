import os
import datetime
import firebase_admin
from firebase_admin import credentials, firestore

sep = os.sep

cred = credentials.Certificate("app" + sep + "DataBase" + sep + "vkConnectionsAppKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# global variables to post data to FireBase every hour
requests = []


# post user at first entrance to the app
def postUserToDb(id, fullName, deviceModel, androidVersion):
    # user = User(id, fullName, getTimeForRequests(), deviceModel, androidVersion)
    # user = user.__dict__
    # usersRef = db.collection(u'Data').document(u'Users')
    # usersRef.set({str(id): user})
    return True


# all requests post to global list of requests
def postRequestToStorage(owner, method, fromId, toId, friends, content, time):
    request = Request(owner, method, fromId, toId, friends, content, time)
    request = request.__dict__
    requests.append(request)


# updates all the info from global variable requests to FireBase
def postRequestsToDb():
    global requests
    requestsRef = db.collection(u'Data').document(u'Requests')
    requestsRef.set({str(getTimeForRequests()): requests})


def getTimeForRequests():
    time = str(datetime.datetime.now()).split('-')
    date = time[2].split(' ')[0] + '.' + time[1] + '.' + time[0]
    time = time[2].split(' ')[1].split('.')[0]
    return date + ' ' + time


class User:
    def __init__(self, id, fullName, joinTime, deviceModel, androidVersion):
        self.Id = id
        self.FullName = fullName
        self.JoinTime = joinTime
        self.DeviceModel = deviceModel
        self.AndroidVersion = androidVersion


class Request:
    def __init__(self, owner, method, fromId, toId, friends, content, time):
        self.Owner = owner
        self.Method = method
        self.FromId = fromId
        self.ToId = toId
        self.Friends = friends
        self.Content = content
        self.Time = time
