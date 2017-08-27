
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "294669373-lSOQcSVqIhQNZJdVG5sqQcGwxYLzEVtS3475pPSK"
access_token_secret = "uSvQN9rSHz0UaTXo0mwqjx9E9ZDcbvKRZ2Y9UTlux1Y7Y"
consumer_key = "WJrH0h02HptNuIQiDEt9ttbCC"
consumer_secret = "VYeve6Vv9BGUa6Ujdo2vXbx1MFxtkI3s8P4s7lMTTpkFLBb3zO"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
