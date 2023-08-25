import random 
n = int(input("how many numbers ?"))
def fill_list (n):
    main_list = list(range(1 , n+15))
    random.shuffle(main_list)
    new_list =main_list[:n]
    return new_list

result = fill_list(n)
print("your list: " , result) 