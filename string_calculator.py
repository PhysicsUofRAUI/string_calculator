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
    negative_nums = []
    for num in nums :
        try :
            int_num = int(num)
        except :
            continue
        
        if int_num < 0 :
            negative_nums.append(int_num)
        
        result = result + int_num
    
    if negative_nums == [] :
        return result
    else :
        negative_string = ''
        for num in negative_nums :
            negative_string = negative_string + ", " + str(num)
            
        raise Exception("Negatives not allowed. The numbers that caused this error were" + negative_string)
    

print(add('1,2,5'))
