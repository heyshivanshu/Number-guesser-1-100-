#no of guesses 10 , print number of guesses left each time , game over when gueses end
import random
a = random.randint(1,100)
c=10
print("Welcome to number guesser game rules are as follows\n","1) guess a number from 1-100\n","2) you have only 10 guesses")
while(c>0):
    print("you have",c,"guesses left")
    #print(a)
    i=int(input("enter number\n"))
    z=abs(i-a)
    c=c-1
    if i==a:
        print("congratulation you have won \n,""you took",c,"guesses")
        break
    if z>50:
        print("far off")
    if z<50 and z>25:
        print("close but not quiet it")
    if z<25 and z>10:
        print("close")
    if z<10 and z>5:
        print("very close")
    if z<5:
        print("almost there")
if c==0:
    print("But game over")