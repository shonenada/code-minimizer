# Code Minimizer

## Introduce

 This is a python tool to help you minimizer your javascript and css code before you deploy your website.

 It uses [rjsmin](http://opensource.perlig.de/rjsmin/) to compress javascript codes, and uses [rcssmin](http://opensource.perlig.de/rcssmin) to compress your css codes.

## Usage

  * Single file compression
    `Python min-py -j script,s -c style.css`

  * Directory compression
    `Python minimize.py ./static/ `

__Important__ : If you are going to compress your codes using the second method, your folder structure looks like:

    ++ staitc

       -- ++ scripts

           -- ++ js_folders

              -- js_files

       -- ++ styles

           -- ++ css_folders

               -- css_files
