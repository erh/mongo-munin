
import urllib2
import sys
import os

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus():
    host = os.environ.get("host", "127.0.0.1")
    port = 28017
    raw = urllib2.urlopen( "http://%s:%d/_status" % (host, port) ).read()
    return json.loads( raw )["serverStatus"]
