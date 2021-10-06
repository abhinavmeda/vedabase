#!/usr/bin/python3

import webbrowser
import sys

def main(*args):
    arguments = sys.argv[1:]
    
    if len(arguments) == 1 and arguments[0].isalpha:
        raise ScriptureLookUpError

    elif len(arguments) == 1 and not arguments[0].isalpha:
        raise TextLookupMissingError

    if arguments[0] == 'sb' or arguments[0] == 'SB':
        text = arguments[1].replace('.', '/')
        webbrowser.open('https://vedabase.io/en/library/sb/' + text)

    elif arguments[0] == 'bg' or arguments[0] == 'BG':
        text = arguments[1].replace('.', '/')
        webbrowser.open('https://vedabase.io/en/library/bg/' + text)

    else:
        raise UnknownBookError(arguments[0])

class ScriptureLookUpError(Exception):
    def __str__(self) -> str:
        return "Didn't provide a scripture to lookup"

class TextLookupMissingError(Exception):
    def __str__(self) -> str:
        return "Didn't provide a text to lookup"

class UnknownBookError(Exception):
    def __init__(self, book) -> None:
        self.book = book
    def __str__(self) -> str:
        return "I don't know what book '{}' is.".format(self.book)

main(sys.argv)