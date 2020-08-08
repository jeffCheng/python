
def say(msg):
    print(msg)

say("Hello")

def add_num(n1, n2):
    n1+n2
    return 

def calculate(min,max):
    sum=0
    for x in range(min,max+1):
        sum=sum+x
    print(sum)

min=input("請輸入數字1:")
min=int(min)
max=input("請輸入數字2:")
max=int(max)
calculate(min,max)