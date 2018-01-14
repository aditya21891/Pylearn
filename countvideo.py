# A PYTHON SCRIPT WHICH IS USED TO COUNT THE VIEWS  in youtube .

import csv
import json
import re
import time
import urllib2
 
 
def get_view_count(start,end,writer):
 
    with open('dubbed_videos.csv', 'rb') as f:
                reader = csv.reader(f, delimiter=',')
                for count,row in enumerate(reader):
                    if count > start and count <= end:
                        print count
 
                        try:
                            string = 'http://gdata.youtube.com/feeds/api/videos/'+ row[2]+'?v=2&alt=json'
                            response        = urllib2.urlopen(string).read()
                        except urllib2.HTTPError as e:
                            if e.code == 403:
                                sleep_time = 60 * 4 # 4 minutes
                                print "Hit the limit; sleeping for %s seconds" % sleep_time
                                time.sleep(sleep_time)
 
                        data            = json.loads(unicode(response, 'utf-8'))
 
                        view_count      = data.get("entry").get("yt$statistics", {}).get("viewCount")
                        fav_count       = data.get("entry").get("yt$statistics", {}).get("favoriteCount")
                        video_title     = data.get("entry").get("title", {}).get("$t")
                        author_name     = data.get("entry").get("author")[0].get("name", {}).get("$t")
                        user_id         = data.get("entry").get("author")[0].get("yt$userId", {}).get("$t")
                        upload_date     = data.get("entry").get("media$group", {}).get("yt$uploaded", {}).get("$t")
                        rating_likes    = data.get("entry").get("yt$rating", {}).get("numLikes")
                        rating_dislikes = data.get("entry").get("yt$rating", {}).get("numDislikes")
                        average_rating  = data.get("entry").get("gd$rating", {}).get("average")
                        print "View Count " + str(view_count)
                        print "Favorite Count " + str(fav_count)
                        print "Video Title " + video_title
                        print "Author Name " + str(author_name)
                        print "User ID " + str(user_id)
                        print "Upload Date " + str(upload_date)
                        print "Rating Likes " + str(rating_likes)
                        print "Rating Dislikes " + str(rating_dislikes)
                        print "Average Rating " + str(average_rating)
                        row = [row[2],
                               view_count,
                               fav_count,
                               video_title,
                               author_name,
                               user_id,
                               upload_date,
                               rating_likes,
                               rating_dislikes,
                               average_rating]
                        writer.writerow([unicode(l).encode('utf-8') for l in row])
 
 
def begin(start,end):
 
    if start == 0:
        with open('updated.csv', 'wb') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerow(["YouTube ID" ,
                             "View Count",
                             "Favorite Count",
                             "Video Title",
                             "Author Name",
                             "User ID",
                             "Upload Date",
                             "Rating Likes",
                             "Rating Dislikes",
                             "Average Rating"])
            get_view_count(start,end,writer)
    else:
        with open('updated.csv', 'wb') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            get_view_count(start,end,writer)
 
 
if __name__ == '__main__':
    begin(0,21350)