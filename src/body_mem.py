
def ok(s):
    return s == "resident" or s == "virtual" or s == "mapped"

def doData():
    for k,v in getServerStatus()["mem"].iteritems():
        if ok(k):
            print( str(k) + ".value " + str(v) )

def doConfig():

    print "graph_title MongoDB memory usage"
    print "graph_args --base 1000"
    print "graph_vlabel mb ${graph_period}"
    print "graph_category MongoDB"

    for k in getServerStatus()["mem"]:
        if ok( k ):
            print k + ".label " + k
            print k + ".type GAUGE"
            print k + ".draw AREA"





