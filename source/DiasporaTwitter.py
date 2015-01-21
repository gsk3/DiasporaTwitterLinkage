# Link diaspora to twitter

import diaspy
import twitter

# --- Configuraiton --- #

# Import connection info/logins

from DTLconfig import *

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

# -- Read posts -- #

statuses = twtCon.GetUserTimeline(twtUser)
# Display them
print [s.text for s in statuses]

# - Store posts into internal database - #

# - Deduplicate - #

# -- Post new posts to Diaspora -- #


#diasStream.post('Testing the diaspy linkage')


