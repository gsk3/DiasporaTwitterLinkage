# Link diaspora to twitter

import diaspy
import twitter

import sqlite3

# --- Configuraiton --- #

# Import connection info/logins

from DTLconfig import *

# Database filename/location
postDBfn = ':memory:'

# --- Code --- #

# -- Establish connections -- #

# - Diaspora - #

diasCon = diaspy.connection.Connection(pod=diasPod,username=diasUsername,password=diasPassword)


diasCon.login()


diasStream = diaspy.streams.Stream(diasCon)


# - Twitter - #
twtCon = twitter.Api(
    consumer_key=twtConsumer_key,
    consumer_secret=twtConsumer_secret, 
    access_token_key=twtAccess_token_key, 
    access_token_secret=twtAccess_token_secret
) 
print twtCon.VerifyCredentials()  #confirm working

# - Post database/cache - #

dbCon = sqlite3.connect( postDBfn )
dbCur = dbCon.cursor()


# -- Read posts -- #

statuses = twtCon.GetUserTimeline(twtUser)
# Display them
print [s.text for s in statuses]
# Store a test instance
s = statuses[0]
r = ( s.created_at_in_seconds, s.text )

# -- Store posts into internal database -- #

# - Create database if it doesn't exist - #

# Does table exist?

tableExistsRes = dbCur.execute("""
     SELECT name FROM sqlite_master WHERE type='table' AND name='posts'
""")
tableExists = len( tableExistsRes.fetchall() ) > 0

# If not, create
if not tableExists:
    dbCur.execute("""CREATE TABLE posts
       (created_at_in_seconds INTEGER PRIMARY KEY, 
       text VARCHAR(200) )  
    """)

# - Loop over elements. For each element:

for s in statuses:
    r = ( s.created_at_in_seconds, s.text )

    # 1) Confirm element doesn't already exist in DB 

    # Pull all posts that occurred that second
    textTimeMatches = dbCur.execute(
        "SELECT text FROM posts WHERE created_at_in_seconds=?",
        [ r[0] ]
    ).fetchall()

    # If there were any matches based on time, check for matches based on text
    if len( textTimeMatches ) > 0:
        textTimeMatches[0][0] == r[1] #! Fix this
    else: # If not a duplicate
        # 2) Store to DB if unique
        dbCur.execute("Insert INTO posts VALUES (?,?)",r) 
        dbCur.commit()
        # 3) Post to Diaspora if unique
        diasStream.post(s.text)


