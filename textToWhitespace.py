#!/usr/bin/python3

def endProgram():
    return '\n\n'

def pushOntoStack(letter):
    return '   ' + bin(ord(letter))[2:].replace('1', '\t').replace('0', ' ') + '\n'

def printLetter():
    return '\t\n  '

def textToWhitespace(text):
    program = ''
    for letter in text:
        program += pushOntoStack(letter)
        program += printLetter()
    
    program += endProgram()
    return program