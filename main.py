#!/usr/bin/env python3

from sys import argv


def main ():
    target="world" if len(argv) == 1 else " ".join(argv[1:])
        
    print(f"hello, {target}!")
    
main()
