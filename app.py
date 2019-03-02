#!/usr/bin/env python
"""
[WHEN TO USE THIS FILE]
[INSTRUCTIONS FOR USING THIS FILE]

Project name: [MISSING]
Author: Micah Parks

This lives on the web at: [MISSING URL]
Target environment: python 3.7
"""

# Start standard library imports.
# End standard library imports.

# Start third party imports.
from flask import Flask, render_template
# End third party imports.

# Start project imports.
# End project imports.


FLASK_OBJ = Flask(__name__, template_folder='./templates')


@FLASK_OBJ.route('/home')
def home():
    """
    Display the home page.
    """
    return render_template('home.html')


if __name__ == '__main__':
    FLASK_OBJ.run()
