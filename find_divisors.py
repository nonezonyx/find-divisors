def find_divisors(num: int) -> list[tuple[int,int]]:
    """find_divisors(num: int) -> list[tuple[int,int]]:
finds integer devisors of num and returns list of tuple of divisors

Example:
>>>find_divisors(10)
[(1,10)(2,5)]"""
    return [(i,num//i) for i in range(1,int(num**0.5)+1) if not num%i]

def main():
    try:
        num=int(input('Enter number: '))
        print(find_divisors(num))
    except Exception as e:
        print(e)
        
if __name__=='__main__':
    while True:
        main()
