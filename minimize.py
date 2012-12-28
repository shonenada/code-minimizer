#!/usr/bin/env python

import sys, getopt, os
from rcssmin import rcssmin
from rjsmin import rjsmin

def minimizeJs( file_path ):
    print "Opening " + file_path
    js_suffix = file_path[len( file_path ) - 2 : ]
    if not js_suffix == 'js':
        print file_path + " is not a js file"
        return None
    js_file = open(file_path).read()
    js_name = file_path[ : len( file_path ) - 3 ]
    js_minimized = rjsmin.jsmin(js_file)
    js_save_name = js_name + ".min.js"
    js_min_file = open( js_save_name, "w" )
    js_min_file.write( js_minimized )
    print "Finished saving Js file " + js_save_name 

def minimizeCSS( file_path ):
    print "Opening " + file_path
    css_suffix = file_path[len( file_path ) - 3 : ]
    if not css_suffix == 'css':
        print file_path + " is not a css file"
        return None
    css_file = open( file_path ).read()
    css_name = file_path[ : len( file_path ) - 4]
    css_minimized = rcssmin.cssmin( css_file )
    css_save_name = css_name + ".min.css"
    css_min_file = open( css_save_name , "w")
    css_min_file.write( css_minimized )
    print "Finished saving Css file " + css_save_name

def JsFolder( folder ):
    folder = folder + "/"
    js_files = os.listdir( folder )
    for x in js_files:
        if os.path.isfile( folder + x ):
            minimizeJs(  folder + x  )
        if os.path.isdir(  folder + x  ):
            JsFolder(  folder + x  )

def CssFolder( folder ):
    folder = folder + "/"
    Css_files = os.listdir( folder )
    for x in Css_files:
        if os.path.isfile( folder + x ):
            minimizeCSS( folder + x )
        if os.path.isdir( folder + x ):
            CssFolder( folder + x )

def minimize( folder ):
    js_folder = os.path.abspath( folder + "scripts/" )
    css_folder = os.path.abspath( folder + "styles/" )
    JsFolder(js_folder)
    CssFolder(css_folder)

if __name__ == "__main__":
    folder = sys.argv[1] + "/static/"
    minimize( folder )