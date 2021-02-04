import menufunctions

def main():
#function call example    
    num = 1
    while num == 1:
        print(menufunctions.pics[1])
        print("\n")
        var = input("press enter to start")
        print(menufunctions.pics[0])
        menufunctions.menu1()
        menufunctions.reset()
        print("------------------------------------------------")
        print("enter 1 if you would like to play again")
        print("enter 2 to quit")
        print("------------------------------------------------")
        num = int(input(""))
         
        
main()

