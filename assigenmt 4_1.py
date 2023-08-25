import random
pc_number = random.randint(0,20)
count=0
for i in range (10) :
    user_number = int(input("enter your num : "))
    count+=1

    if user_number == pc_number :
        print("you win ," , "you try it:",count )
        break
    if user_number < pc_number :
        print ("bro balatar")    
    if user_number > pc_number :
        print ("bro paintar")