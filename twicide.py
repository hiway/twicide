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
import time
import tweepy
import twhelper
import readline

def show_stats(api):
    """Takes an authenticated tweepy API object and displays user's
    stats/ information."""
    user = api.me()
    print "Your username:", user.screen_name
    print "Friends:", user.friends_count
    print "Followers:", user.followers_count

def purge_friends(api):
    """Unfollows all friends."""
    print "="*80
    print "WARNING: CONTINUING WILL UNFOLLOW ALL PEOPLE YOU FOLLOW."
    print "="*80
    response = raw_input("Type 'unfollow all' to continue: ")
    if not response == 'unfollow all':
        print "Cancelling..."
        return None

    user = api.me()
    friends = user.friends()
    print "Mass unfollowing: ",

    for f in friends:
        print f.screen_name,
        f.unfollow()
        print "+",

    print "... done."


if __name__ == '__main__':
    api = twhelper.get_api()
    show_stats(api)
    purge_friends(api)
