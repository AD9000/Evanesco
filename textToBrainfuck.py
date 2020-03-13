#!/usr/bin/python3

def textToBrainfuck(text):
    brainfucked = ''
    # Move pointer to byte 1
    brainfucked += '>'
    for letter in text:
        brainfucked += ord(letter) * '+'
        brainfucked += '.'
        # This is me being lazy and abusing memory hahahahahaha
        brainfucked += '>'
    
    return brainfucked[:-1]

print (textToBrainfuck(input()))