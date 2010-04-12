

def doData():
    ss = getServerStatus()
    for k,v in ss["opcounters"].iteritems():
        print( str(k) + ".value " + str(v) )

def doConfig():

    print "graph_title MongoDB ops"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel ops / ${graph_period}"
    print "graph_category MongoDB"
    print "graph_total total"

    for k in getServerStatus()["opcounters"]:
        print k + ".label " + k
        print k + ".min 0"
        print k + ".type COUNTER"
        print k + ".max 500000"
        print k + ".draw LINE1"
