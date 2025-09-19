'''
for number in range(2,10+1,2):
    print(number)
    '''
end=1
sum=0
for number in range(0,end):
    a=int(input('enter number to add:'))
    if a=='q':
        break
    else:
        end=end+1
        sum=int(sum+a)
        print(f'current sum is {sum}')
        
    


