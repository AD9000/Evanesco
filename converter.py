#!/usr/bin/python3

def convertToBrainfuck(text):
    brainfucked = ''
    # Move pointer to byte 1
    brainfucked += '>'
    for letter in text:
        brainfucked += ord(letter) * '+'
        brainfucked += '.'
        # This is me being lazy and abusing memory hahahahahaha
        brainfucked += '>'
    
    return brainfucked

def brainfuckToWhitespace(brainfucked):
    pass

text = input()
convertToBrainfuck(text)