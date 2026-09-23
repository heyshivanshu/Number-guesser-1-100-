#no of guesses 10 , print number of guesses left each time , game over when gueses end
import random
a = random.randint(1,50)
c=10
print("Welcome to number guesser game rules are as follows\n","1) guess a number from 1-50\n","2) you have only 10 guesses")
while(c>0):
    print("you have",c,"guesses left")
    #print(a)
    i=int(input("enter number\n"))
    z=abs(i-a)
    y=(a-i)
    c=c-1
    if i==a:
        print(f"Congratulation you have won \n you took {10-c} guesses")
        break
    if z>=25:
        print("far off")
    elif z<25 and z>=15:
        print("close but not quiet it")
    elif z<15 and z>=10:
        print("close")
    elif z<10 and z>=5:
        print("very close")
    elif z<5:
        print("almost there")
    if y<0:
        print("Go lower")
    else:
        print("Go higher")
if c==0:
    print(f"But game over random number was {a}")
