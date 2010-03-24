
import urllib2
import sys

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus():
    raw = urllib2.urlopen( "http://127.0.0.1:28017/_status" ).read()
    return json.loads( raw )["serverStatus"]
