def find_divisors(num: int): #num>0
    x=round(num**0.5)
    ans=[]
    while x:
        if num%x==0:
            ans.append((x,num//x))
        x-=1
    return ans

def main():
    try:
        num=int(input('Enter number: '))
        print(find_divisors(num))
    except Exception as e:
        print(e)
        
if __name__=='__main__':
    while True:
        main()
