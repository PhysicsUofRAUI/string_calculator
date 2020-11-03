import re

def add(str_nums) :
    if len(str_nums) == 0 :
        return 0
    
    nums = re.split(',|\n',str_nums)
    
    result = 0
    for num in nums :
        try :
            int_num = int(num)
        except :
            continue
        
        result = result + int_num
    
    return result
    
    

print(add('1,2,5'))
