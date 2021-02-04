#example of nested for loop below
#example of return statement below
#example of parmeters
def dishes(times, dishes):
    total = 0
    total2 = 0
    nums = {}
    totals = {}


    for count in range(times):
        if count == 0:
            sufix2 = "st"
        elif count == 1:
            sufix2 = "nd"
        elif count == 2:
            sufix2 = "rd"
        else:
            sufix2 = "th"
        for count2 in range(dishes):
            if count2 == 0:
                sufix = "st"
            elif count2 == 1:
                sufix = "nd"
            elif count2 == 2:
                sufix = "rd"
            else:
                sufix = "th"
            this = count2+1
            this2 = count+1
            print("How many seconds would you like to wash each dish? ")
            print("enter your",this,sufix,"number of seconds to wash",this,sufix,"dish for the",this2,sufix2,"time") 
            nums[count2] = int(input(""))
            print("------------------------------------------------")
            total = nums[count2] + total
    return total
    
