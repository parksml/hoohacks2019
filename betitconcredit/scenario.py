#!/usr/bin/env python
"""
[WHEN TO USE THIS FILE]
[INSTRUCTIONS FOR USING THIS FILE]

Project name: [MISSING]
Author: Justin Miller

This lives on the web at: [MISSING URL]
Target environment: python 3.7
"""

# Start standard library imports.
from typing import Dict
# End standard library imports.

# Start third party imports.
# End third party imports.

# Start project imports.
# End project imports.

def load_scenarios() -> dict:
    with open("jsonfiles/scenarios.json") as inFile:
        scenariosDict = load(inFile)