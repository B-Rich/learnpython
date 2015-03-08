## BROWSER
# create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80
# - the normal http port
s.connect(("www.mcmillan-inc.com", 80))


## SERVER
# create INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host,
#  and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)

