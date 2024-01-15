#Q1: Given a number n, return all numbers less than n that are even
#ex: isEven(10) -> [0,2,4,6,8]

#def isEven(n:int) -> List[int]

list = [2, 4, 6, 10, 22, 48, 50]

for num in list:
    if num % 2 == 0:
        print(num)
        

#Q2: Given a list of numbers, return all non-repeating numbers, if all are repeating, return 0
#Expected output is a list
#E.g. [1,1,2,2,3] -> [3]
#[1,2,2] -> [0]

def returnSingleNumber(l:List[int]) -> List[int]


#Q3: Given an arbitrary length credit card number, mask all characters but the last four digits with *
#Can assume the string is only represented by digits
#E.g. 1234567890 -> ******7890

def mask_cc_numbers(cc_string:str) -> str:
