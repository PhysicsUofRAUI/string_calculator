import re

def custom_split(str_nums) :
    if str_nums[0:2] == "//" :
        if len(str_nums) > 4 :
            nums = str_nums[4:].split(str_nums[2])
        else :
            nums = []
    else :
        nums = re.split(',|\n',str_nums)
    
    return nums

def add(str_nums) :
    if len(str_nums) == 0 :
        return 0
    
    nums = custom_split(str_nums)
    
    result = 0
    for num in nums :
        try :
            int_num = int(num)
        except :
            continue
        
        result = result + int_num
    
    return result
    
    

print(add('1,2,5'))
