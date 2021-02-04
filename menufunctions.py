import mathfun
import time

#global variables
frontdoorkey = 0
jbkey = 0
look1 = 0
look2 = 0
look3 = 0
look4 = 0
look5 = 0
look6 = 0
steak = 0
eat = 0
lion = 0
jewels = 0

def reset():
    global frontdoorkey
    global jbkey
    global look1
    global look2
    global look3
    global look4
    global look5
    global look6
    global steak
    global eat
    global lion
    global jewels

    frontdoorkey = 0
    jbkey = 0
    look1 = 0
    look2 = 0
    look3 = 0
    look4 = 0
    look5 = 0
    look6 = 0
    steak = 0
    eat = 0
    lion = 0
    jewels = 0



#load images and dynamicly assign variables
picfile = {}
picfile[0] = open("frontdoor.txt", "r")
picfile[1] = open("title.txt", "r")
picfile[2] = open("kitchen.txt", "r")
picfile[3] = open("lion.txt", "r")
picfile[4] = open("bedroom.txt", "r")
picfile[5] = open("livingroomlion.txt", "r")
picfile[6] = open("indoor.txt", "r")
picfile[7] = open("landryroom.txt", "r")
picfile[8] = open("livingroom.txt", "r")
picfile[9] = open("gameover.txt", "r")
picfile[10] = open("win.txt", "r")

pics = {}
#for loop example
for count in range(11):
    pics[count] = picfile[count].read()
    picfile[count].close()

#load strings and dynamicly assign variables
line = {}
infile = open("lines.txt", "r")
for count in range(25):
    line[count] = infile.readline()
infile.close





def menu1():
    loop = 0
    global frontdoorkey
    global look1


#while loop example    
    while loop == 0:
#if/else example
        if jewels == 1:
            print(pics[10])
            print(line[22])
            loop = 1
        else:
            print("------------------------------------------------")
            print("enter 1 to look around")
#simple if example
            if look1 == 1:
                if frontdoorkey == 0:
                    print("enter 2 open door")
                if frontdoorkey == 1:
                    print("enter 2 to unlock door with front door key")
                if frontdoorkey == 0:
                    print("enter 3 to search strange rock")
            print("------------------------------------------------")
    
            menu = int(input("enter a menu item "))
            print("\n")
            print(pics[0])
#if/elif/else example
#nested if/else example
            if menu == 1:
                print(line[0])
                look1 = 1
            elif menu == 2:
                if frontdoorkey == 1:
                    print(pics[6])
                    print(line[3])
                    loop = 1
                    menu2()
                else:
                    print(line[1])   
            elif menu == 3 and frontdoorkey == 0:
                print(line[2])
                frontdoorkey = 1

            else:
                print("invalid menu item ")



def menu2():
    loop = 0
    global look2
    while loop == 0:
        print("------------------------------------------------")
        print("enter 1 to look around")
        if look2 == 1:
            print("enter 2 to check out clock")
            print("enter 3 to enter the door to the left")
            print("enter 4 to enter the door stright ahead")
            print("enter 5 to go up the stairs")
            print("enter 6 to go back outside")
        print("------------------------------------------------")
    
        menu = int(input("enter a menu item "))
        print("\n")
        print(pics[6])

        if menu == 1:
            print(line[4])
            look2 = 1
        elif menu == 2:
            print(line[5],time.strftime("%I:%M"))
        elif menu == 3:
            print(pics[2])
            loop = 1
            menu3()
        elif menu == 4:
            if lion == 0:
                print(pics[5])
            else:
                print(pics[8])
            loop = 1
            menu4()
        elif menu == 5:
            print(pics[4])
            loop = 1
            menu6()
        elif menu == 6:
            print(pics[0])
            loop = 1
            menu1()
        else:
            print("invalid menu item ")



def menu3():
    loop = 0
    global eat
    global look3
    global steak
    while loop == 0:
        print("------------------------------------------------")
        print("enter 1 to look around")
        if look3 == 1:
            print("enter 2 to check refrigerator")
            print("enter 3 to use the oven")
            print("enter 4 to use the sink")
            print("enter 5 to exit room")
        print("------------------------------------------------")
    
        menu = int(input("enter a menu item "))
        print("\n")
        print(pics[2])

        if menu == 1:
            print(line[6])
            look3 = 1
        elif menu == 2:
            if steak == 0:
                print(line[7])
                steak = 1
            else:
                print(line[11])
        elif menu == 3:
            if steak == 0:
                print(line[8])
            else:
                print(line[9])
                print("------------------------------------------------")
                print("enter 1 to cook")
                print("enter 2 to not use the oven")
                print("------------------------------------------------")
                eat = int(input("enter menu item "))
                print("")
                print(pics[2])
                if eat == 1:
                    print(line[10])
                    steak = 3
        elif menu == 4: 
            
            print("------------------------------------------------")
            timestowash = int(input("How many times do you want to wash the dishes? "))
            print("------------------------------------------------")
            dishestowash = int(input("How many dishes do you want to wash? "))
            print("------------------------------------------------")
#parameter being passed example
            print(line[12], mathfun.dishes(timestowash, dishestowash),"seconds")
        elif menu == 5:
            print(pics[6])
            loop = 1
            menu2()
                
        else:
            print("invalid menu item ")

def menu4():
    loop = 0
    global look4
    global lion
    global steak
    while loop == 0:
        print("------------------------------------------------")
        print("enter 1 to look around")
        if look4 == 1:
            if lion == 0:
                print("enter 2 to walk past the lion")
            else:
                print("enter 2 to enter doorway")
            if steak == 1 and lion == 0:
                print("enter 3 to feed the steak to the lion")
                print("enter 4 to go back to the foyer")
            else:
                print("enter 3 to go back to the foyer")
            
        print("------------------------------------------------")
    
        menu = int(input("enter a menu item "))
        print("\n")
        if lion == 0:
            print(pics[5])
        else:
            print(pics[8])

        if menu == 1:
            if lion == 0:
                print(line[13])
                look4 = 1
            else:
                print(line[16])
                look4 = 1
        elif menu == 2:
            if lion == 0:
                print(pics[3])
                print(line[14])
                print(pics[9])
                loop = 1
            else:
                print(pics[7])
                loop = 1
                menu5()       
        elif menu == 3:
            if steak == 1:
                print(pics[8])
                print(line[15])
                lion = 1
                steak = 0
            else:
                print(pics[6])
                loop = 1
                menu2()
        elif menu == 4:
            print(pics[6])
            loop = 1
            menu2()
                
        else:
            print("invalid menu item ")

def menu5():
    loop = 0
    global look5
    global jbkey
    while loop == 0:
        print("------------------------------------------------")
        print("enter 1 to look around")
        if look5 == 1:
            print("enter 2 to check the washer and dryer")
            print("enter 3 to exit room")
        print("------------------------------------------------")
    
        menu = int(input("enter a menu item "))
        print("\n")
        print(pics[7])

        if menu == 1:
            print(line[17])
            look5 = 1
        elif menu == 2:
            print(line[18])
            jbkey = 1
        elif menu == 3:
            print(pics[8])
            loop = 1
            menu4()
        else:
            print("invalid menu item ")

def menu6():
    loop = 0
    global look6
    global jewels
    while loop == 0:
        print("------------------------------------------------")
        print("enter 1 to look around")
        if look6 == 1:
            print("enter 2 to open jewelry box")
            print("enter 3 to go back downstairs")
        print("------------------------------------------------")
    
        menu = int(input("enter a menu item "))
        print("\n")
        print(pics[4])

        if menu == 1:
            print(line[19])
            look6 = 1
        elif menu == 2:
            if jbkey == 1:
                print(line[20])
                jewels = 1
            else:
                print(line[21])
        elif menu == 3:
            print(pics[6])
            loop = 1
            menu2()
        else:
            print("invalid menu item ")

