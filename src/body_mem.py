
def ok(s):
    return s == "resident" or s == "virtual" or s == "mapped"

def doData():
    for k,v in getServerStatus()["mem"].iteritems():
        if ok(k):
            print( str(k) + ".value " + str(v * 1024 * 1024) )

def doConfig():

    print "graph_title MongoDB memory usage"
    print "graph_args --base 1024 -l 0 --vertical-label Bytes"
    print "graph_category MongoDB"

    for k in getServerStatus()["mem"]:
        if ok( k ):
            print k + ".label " + k
            print k + ".draw LINE1"






