#!/usr/bin/env python
import plivohelper
import sys


try:
    calluuid = sys.argv[1]
except IndexError:
    print "Need CallUUID"
    sys.exit(1)


# URL of the Plivo REST Service
REST_API_URL = 'http://127.0.0.1:8088'
API_VERSION = 'v0.1'

# Sid and AuthToken
SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a REST object
plivo = plivohelper.REST(REST_API_URL, SID, AUTH_TOKEN, API_VERSION)

call_params = {'CallUUID':calluuid}

try:
    print plivo.sound_touch_stop(call_params)
except Exception, e:
    print e
