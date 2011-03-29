#!/usr/bin/env python
try:
	import traceback, sys, os, cgi
	from session import Session
	# The following makes errors go to HTTP client's browser
	# instead of the server logs.
	sys.stderr = sys.stdout

	print 'Content-type: text/html\n'
	form = cgi.FieldStorage()
	username = str(form.getvalue("username"))
	password = str(form.getvalue("password"))
	usertype = str(form.getvalue("usertype"))

	#print standard header
	with open('header.html.pyt') as header:
		print header.read() % ("Login")

	u = Session(username, password, usertype)

	#print bottom of page
	with open('bottom.html.pyt') as bottom:
		print bottom.read()
        
except Exception, e:
        print 'Content-type: text/html\n'
        print
        print '&lt;html&gt;&lt;head&gt;&lt;title&gt;'
        print str(e)
        print '&lt;/title&gt;'
        print '&lt;/head&gt;&lt;body&gt;'
        print '&lt;h1&gt;TRACEBACK&lt;/h1&gt;'
        print '&lt;pre&gt;'
        traceback.print_exc()
        print '&lt;/pre&gt;'
        print '&lt;/body&gt;&lt;/html&gt;'

