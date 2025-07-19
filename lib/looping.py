#!/usr/bin/env python3

def happy_new_year():
    counter=10
    while counter> 0:
        print(counter)
        counter-=1
    print("Happy New Year!")
    

def square_integers(int_list):
    int_list_final=[]
    for i in range(len(int_list)):
       int_lists = int_list[i]**2
       int_list_final.append(int_lists)
    return int_list_final
       
    
def fizzbuzz():
    num=1
    while num <= 100:        
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
        num += 1

    
