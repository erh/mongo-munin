
name = "locked"

def doData():
    print name + ".value " + str( 100 * getServerStatus()["globalLock"]["ratio"] )

def doConfig():

    print "graph_title MongoDB write lock percentage"
    print "graph_vlabel percentage ${graph_period}"
    print "graph_category MongoDB"

    print name + ".label " + name
    print name + ".type GAUGE"
    print name + ".draw AREA"
    print name + ".min 0"
    print name + ".max 100"





