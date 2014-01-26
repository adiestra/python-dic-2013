#!/usr/bin/env python

import os

print "Status: 200 OK"
print "Content-Type: text/html; charset=UTF-8"
print 
print 
print "<html>"
print "<head>"
print "<title>Mostrar IP</title>"
print "</head>"
print "<body>"
print "<h1>Mostrar IP</h1>"
print "<p>Tu IP es: %s</p>" % os.environ['REMOTE_ADDR']
print "</body>"
print "<html>"
