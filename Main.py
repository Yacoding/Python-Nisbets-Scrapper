from views.MainView import MainView
from works.NisbetCat import NisbetCat
from works.NisbetProduct import NisbetProduct
#from works.Nisbets import Nisbets

#import oauth2 as oauth
#import httplib2
#import time, os
#
## Fill the keys and secrets you retrieved after registering your app
#consumer_key      =   'abcd123456'
#consumer_secret  =   'efgh987654'
#user_token           =   'abcd1234-efgh987-9988'
#user_secret          =   '9876abcd-123asdf-1122'
#
## Use your API key and secret to instantiate consumer object
#consumer = oauth.Consumer(consumer_key, consumer_secret)
#
## Use your developer token and secret to instantiate access token object
#access_token = oauth.Token(
#    key=user_token,
#    secret=user_secret)
#
#client = oauth.Client(consumer, access_token)
#
#
## Make call to LinkedIn to retrieve your own profile
#resp,content = client.request("http://api.linkedin.com/v1/people/~", "GET")
#
## By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
## resp,content = client.request(""http://api.linkedin.com/v1/people/~?format=json", "GET", {})
#
#print content
#

__author__ = 'Rabbi'


#def scrapNisbetInfo():
#    nisbet = Nisbets()
#    nisbet.scrapData()


def scrapNisbetCat():
    nisbetCat = NisbetCat()
    nisbetCat.scrapData()


def scrapNisbetProduct():
    nisbet = NisbetProduct()
    nisbet.scrapData()

if __name__ == "__main__":
    mainView = MainView()
    mainView.showMainView()
#    scrapNisbetInfo()
#    scrapNisbetCat()
#    scrapNisbetProduct()