twicide
=======

A utility to help you start fresh, purges follow/friend lists.

This software is strictly alpha, it may or may not work - and the primary function of this app is of destructive nature, you are responsible for the (ab)use of this script to erase parts of your account on twitter.

### THIS APP RUNS DESTRUCTIVE OPERATIONS. There are no backups, no way to turn it back.

Future plans: to destroy all your tweets or selected tweets for certain days/hours (within twitter's artificial limits for going back)

Usage:

Install requirements in virtual environment:

    virtualenvironment --distribute --no-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the application:

    python twicide.py

You will need your own application consumer-key and consumer-secret that you can get from [http://dev.twitter.com/](http://dev.twitter.com/)
