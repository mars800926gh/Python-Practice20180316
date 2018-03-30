import random

rndbuf = []
rndget = []

print("Here will get 4 random numbers!")
#rndamnt = raw_input("please enter the amount of random number : ")
rndamnt= input("Please enter the amount of random number : ")
rndmax= input("Please enter the maxnum of random number : ")
rndamnt=int(rndamnt)
rndmax=int(rndmax)

while rndamnt>0:
    rndbuf.append(random.randint(0,rndmax))
    rndamnt-=1
print("Total random numbers : ",rndbuf)

while len(rndbuf)>4:
    rndbuf.pop(random.randint(0,len(rndbuf)-1))
print("Get 4 random numbers : ",rndbuf)
