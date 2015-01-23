# DiasporaTwitterLinkage
Python script to post a single user's Twitter posts to Diaspora, designed to be run as a cron script


# Installation

    Install python, python-requests
        sudo apt-get install python python-pip python-dev ipython
        sudo pip install requests
    Install diaspy from Github (version in pip didn't work for me)
        git clone https://github.com/marekjm/diaspy
        sudo python setup.py install
    Installpython-twitter
        sudo pip install python-twitter
    Install the python script I wrote
        Copy to right directory
        Customize config for your logins
            Create an OAuth login for your app at https://apps.twitter.com/app/new
                Then go to "Keys and Access Tokens" tab
                "Create Access Token"
                Copy into config
            Set the pathDBfn to the name of a good location and filename for the SQLite database that will prevent duplication of posts being copied
        Test it
            python DTLconfig.py
    Set up cron to run the script once a day
        sudo crontab -e
        Then insert the following into your crontab: 
            ## Diaspora-Twitter Linkage - Every 5 minutes
            5,10,15,20,25,30,35,40,45,50,55 * * * *         python /path/to/DTL/source/DiasporaTwitter.py

