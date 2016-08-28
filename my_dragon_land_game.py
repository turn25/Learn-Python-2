import random
import time
def gioithieu():
    print "Enter your name: "    
    name = raw_input()   
    print "A long time ago, in the MURDERdrAgonKingdom which is known as the land of dragon. "
    print ("You( "+name+" )-the player, must find a way to escape. There are two ways to escape")   
    print 'from the dragon: Go to the forest or go to the cave'       
    print "(Forest = 1 ; Cave = 2)"

def chooseforest():
    forest = ""
    while forest != "1" and forest != "2":
        print "Choose forest \n(1/2)"
        forest = raw_input()
    return forest

def chon():
    hang = ""
    while hang!= "1" and hang !="2":
        print "Choose cave \n(1/2)"
        hang = raw_input()
    return hang

def chonhang(so_hang):
    print "You go inside the cave ..."
    time.sleep(2)
    print ("...")
    a = random.randint(1, 2)
    if a == int(dachonhang):
        time.sleep(1)
        print "Luckily, the dragon couldn't go inside a cave because it too small."
        time.sleep(2)
        print "so you are ALIVE!"
    else:
        time.sleep(2)
        print "Unluckily, the dragon could go inside a cave ..."
        time.sleep(2)
        print "A few days later, ..."
        time.sleep(3)
        print 'You found dead...'

def chonrung(so_rung):
    print "You go into the forest..."
    time.sleep(2)
    print "..."
    b = random.randint(1, 2)
    if b == int(dachonrung):
        time.sleep(1)
        print "Luckily, the dragon had losed you"
        time.sleep(2)
        print "so you are ALIVE!"
    else:
        time.sleep(2)
        print "Unluckily..."
        time.sleep(2)
        print "A few days later, ..."
        time.sleep(3)
        print "You found dead..."

mang = "y"
while mang == 'y' or mang == 'yes':
    gioithieu()
    print 'Choose: '
    choose = raw_input()
    if choose == '2':
        dachonhang = chon()
        chonhang(dachonhang)
    elif choose == '1':
        dachonrung = chooseforest()
        chonrung(dachonrung)

    else:
        print '...'
        time.sleep(5)
        print "5 days later, you found dead."
    print "Do you want to play again?"
    mang = raw_input()
