import time
global gold
apples=0
gold = 0

def start():
    print "hello and welcome!"
    name = raw_input("whats you name:")
    print "welcome, ",name,"!"
    print "The objective of this game is to collect apples."
    print "AFter collecting the apples you can sell them."
    choice = raw_input("Do you want to play Y/N?")
    if choice == "Y":
        begin()
    if choice == "N":
        print "See you soon"

def begin():
    global apples
    global gold
    print "let's get started!"
    if gold > 99:
        print "You've won the gold"
        play = raw_input("Do you want to play again?")
        if play == "Y":
            begin()
        if play == "N":
            print "Congrats again!"
    pick = raw_input("Do you want to pick an apple Y/N?")
    if pick == "Y":
        time.sleep(1)
        print "You pick an apple."
        apples += 1
        print "You currently have ",apples," apples"
        begin()
    if pick == "N":
        sell = raw_input("Do you want to sell your apples Y/N?")
        if sell == "Y":
            global gold
            global apples
            print "YOu currently have, ",apples," apples"
            print "YOu've sold your apples"
            gold = apples *10
            apples = 0
            print "Your gold is now:",gold
            begin()
start()
