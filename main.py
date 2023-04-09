#!/usr/bin/env python3

from sys import argv
from os import environ

def main ():
    target = environ.get("TARGET", "world")
    if len(argv) > 1:
        target = " ".join(argv[1:])
        
    print(f"hello, {target}!")
    
main()
