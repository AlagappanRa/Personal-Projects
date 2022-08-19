def add_binary(a,b):
    def convert_to_binary(num):
        '''(str)'''
        base = 2
        output = ''
        if not num:
            return '0'
        
        while num:
            remainder = num % base 
            num = num // base
            output += str(remainder)
            
        return output[::-1]

    def convert_to_decimal(num):
        '''(str)'''
        base = 2
        number_old = 0
        for digit in num:
            remainder = int(digit)
            number_old = number_old * base + remainder
        
        return number_old
    
    def addition(num1, num2):
        '''(str, str)'''
        def helper(num1, num2, output):
            if len(num1)> len(num2):
                bigger_num, smaller_num = num1, num2
            else:
                bigger_num, smaller_num = num2, num1
                
            carry_over = 0
            for i in range(-1,-len(smaller_num)-1,-1):
                total = carry_over + int(num1[i])+ int(num2[i])
                if total == 2:
                    carry_over = 1
                    output = '0' + output
                elif total == 3:
                    carry_over = 1
                    output = '1' + output
                else:
                    carry_over = 0
                    output = str(total) + output
            
            num1, num2 = carry_over, bigger_num[:len(bigger_num) - len(smaller_num)]
            while num1:
                return helper(str(num1), num2, output)
            else:
                output = num2 + output
            return output
                                          
        return helper(num1, num2, "")
                                                                                
    bin_A, bin_B = convert_to_binary(a), convert_to_binary(b)
    bin_result = addition(bin_A, bin_B)
    return convert_to_decimal(bin_result)

print(add_binary(5506, 5004))

def make_readable(seconds):
    hours = seconds//3600
    remainder = seconds % 3600
    minutes = remainder //60
    seconds = remainder % 60
    return "{0:02.0f}:{1:02.0f}:{2:02.0f}".format(hours, minutes, seconds)
