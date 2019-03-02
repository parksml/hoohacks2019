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
from flask import Flask
# End third party imports.

# Start project imports.
# End project imports.


FLASK_OBJ = Flask(__name__)


@FLASK_OBJ.route('templates/home.html')
def main() -> None:
    """
    The logic of the file.
    """
    pass


if __name__ == '__main__':
    main()
