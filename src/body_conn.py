
name = "connections"


def doData():
    print name + ".value " + str( getServerStatus()["connections"]["current"] )

def doConfig():

    print "graph_title MongoDB current connections"
    print "graph_vlabel connections ${graph_period}"
    print "graph_category MongoDB"

    print name + ".label " + name
    print name + ".type GAUGE"
    print name + ".draw AREA"





