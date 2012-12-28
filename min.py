import sys, getopt, os
from rcssmin import rcssmin
from rjsmin import rjsmin
opts, agrs = getopt.getopt(sys.argv[1:], "hj:c:o:")
js_file = ""
css_file = ""

for op, value in opts:
    if op == "-j":
        js_file = open(value)
        js_name = value[ : len( value ) - 3 ]
        js_min = rjsmin.jsmin( js_file.read() )
        js_min_file = open( js_name + ".min.js", 'w' )
        js_min_file.write( js_min )
        print "Finished saving Js file"
    elif op == "-c":
        css_file = open(value)
        css_name = value[ : len( value ) - 4 ]
        css_min = rcssmin.cssmin( css_file.read() )
        css_min_file = open( cs_name + ".min.css", 'w' )
        css_min_file.write( js_min )
        print "Finished saving Css file"
