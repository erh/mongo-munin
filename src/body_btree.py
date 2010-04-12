
def get():
    return getServerStatus()["indexCounters"]["btree"]

def doData():
    for k,v in get().iteritems():
        print( str(k) + ".value " + str(int(v)) )

def doConfig():

    print "graph_title MongoDB btree stats"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel mb ${graph_period}"
    print "graph_category MongoDB"

    for k in get():
        print k + ".label " + k
        print k + ".min 0"
        print k + ".type COUNTER"
        print k + ".max 500000"
        print k + ".draw LINE1"





