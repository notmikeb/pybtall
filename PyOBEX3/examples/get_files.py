#!/usr/bin/env python

import bluetooth, os, sys
from xml.etree import ElementTree
from PyOBEX import client, responses

# register signal handler 
import signal
def handler(sig, frame):
    print('Got signal: ', sig)
    raise Exception("error handling" + repr(sig))
    import sys
    sys.exit(-1)

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)
	
signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGABRT, handler)
original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == "__main__":

    if len(sys.argv) != 3:
    
        sys.stderr.write("Usage: %s <device address> <directory>\n" % sys.argv[0])
        sys.exit(1)
    
    device_address = sys.argv[1]
    path = sys.argv[2]
    
    services = bluetooth.find_service(uuid="1106", address=device_address)
    port = -1
    if services:
        port = services[0]["port"]
    if port == -1:
        raise Exception("failed to get port by uuid from remote sdp .")
    else:
        print("found ftp servie at port:{}".format(port))
    c = client.BrowserClient(device_address, port)
    
    response = c.connect()
    if not isinstance(response, responses.ConnectSuccess):
        sys.stderr.write("Failed to connect.\n")
        sys.exit(1)
    
    pieces = path.split("/")
    
    for piece in pieces:
    
        response = c.setpath(piece)
        if isinstance(response, responses.FailureResponse):
            sys.stderr.write("Failed to enter directory.\n")
            sys.exit(1)
    
    sys.stdout.write("Entered directory: %s\n" % path)
    
    response = c.listdir()
    
    if isinstance(response, responses.FailureResponse):
        sys.stderr.write("Failed to list directory.\n")
        sys.exit(1)
    
    headers, data = response
    tree = ElementTree.fromstring(data)
    for element in tree.findall("file"):
    
        name = element.attrib["name"]
        
        if os.path.exists(name):
            sys.stderr.write("File already exists: %s\n" % name)
            continue
        
        sys.stdout.write("Fetching file: %s\n" % name)
        
        response = c.get(name)
        
        if isinstance(response, responses.FailureResponse):
            sys.stderr.write("Failed to get file: %s\n" % name)
        else:
            sys.stdout.write("Writing file: %s\n" % name)
            headers, data = response
            try:
                open(name, "wb").write(data)
            except IOError:
                sys.stderr.write("Failed to write file: %s\n" % name)
    
    c.disconnect()
    sys.exit()
