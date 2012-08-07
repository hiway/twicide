# Copyright (c) 2012, Harshad Sharma. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    - Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    - Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import tweepy
import webbrowser

try:
    from config import *
except:
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""


if CONSUMER_KEY == "" or CONSUMER_SECRET == "":
    print ("Error: \nYou need to create a twitter application on "
           "http://dev.twitter.com and get consumer-key and consumer-secret "
           "and paste it in twhelper.py before we can proceed.")
    sys.exit(1)


def get_twitter_auth():
    """Authenticates user and returns access credentials."""
    # Authenticate if information not found
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    # Get Auth URL
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print "Error: Failed to get request token."
        sys.exit(1)

    # Get Verifier
    print ("Visit this URL and confirm authentication by typing in the "
           "PIN given by Twitter.")
    webbrowser.open_new_tab(redirect_url)
    verifier = raw_input("Twitter Verification PIN: ")

    # Get token
    try:
        token = auth.get_access_token(verifier=verifier)
    except tweepy.TweepError:
        print ("Error: Unable to get access tokens from verifier, "
               "please try again.")

    return token.to_string()


def save_token(token_string):
    """Saves the token string into a file for later retrieval."""
    try:
        ofile = open('access.cfg', 'w')
        ofile.write(token_string)
        ofile.close()
    except IOError:
        print ("Error: Unable to save credentials, continuing."
               "However, you will have to re-authenticate next time.")


def load_token():
    """Loads token_string from file and returns a token."""
    try:
        ifile = open('access.cfg', 'r')
        token_string = ifile.read()
        ifile.close()
        return tweepy.oauth.OAuthToken.from_string(token_string)

    except IOError:
        print ("Error: Unable to load credentials, please authenticate.")
        return None

    except tweepy.TweepError:
        print ("Error: Unable to parse credentials, please remove access.cfg "
               "file and try running app again.")


def get_api():
    """Returns an authenticated tweepy API object. Does all legwork to get the
    auth credentials. Usually, you will need to call only this one function."""
    # Load auth information.
    token = load_token()

    if token is None:
        token_string = get_twitter_auth()
        save_token(token_string)
        token = tweepy.oauth.OAuthToken.from_string(token_string)

    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(token.key, token.secret)

        api = tweepy.API(auth)
    except tweepy.TweepError:
        print ("Error: Unable to get tweepy API, please try again.")
        sys.exit(1)

    return api


if __name__ == '__main__':
    # Runs if this file is directly executed instead of using as module.
    api = get_api()
    me = api.me()
    print "You are:", me.screen_name
    print "Followers:", me.followers_count
    print "Friends:", me.friends_count
