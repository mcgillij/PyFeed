#!/bin/bash
# builds the program on windows
cxfreeze --target-dir=dist MainApp.py --include-modules sip
cp settings.dat dist/
