def odd(numbers):
     odds=[]
     for nums in numbers:
        if nums % 2 !=0:
            odds.append(nums)
     return odds
def is_neg(numbers):
    neg=[]
    for num in numbers:
        if num<0:
            neg.append(num)   
    return neg
def report_odd_ngative(numbers):
    odds = odd(numbers)     
    neg_odd= is_neg(odds)  
    return neg_odd
numbers=[-1,2,-3,-4,5,8,11,-67]
print(report_odd_ngative(numbers)) 
            
