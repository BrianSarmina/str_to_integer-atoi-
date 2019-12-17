
class Solution:
    def myAtoi(self, str: str) -> int:
        
        valid_numbers = ['-', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   # List of posible valid "numbers".
        numbers = []   # List of debugged numbers.
        final_number = 0   # Final number sum.
        sign_event = 1   # Check if there is a "-" sign in the string.
        counter = 1   # Counter for decreasing the "power" of integer multiplication.
        find_number = str   # We change the variable name, for better compehension.
        
        if not find_number[0] in valid_numbers:   # Condition for "letters" as first element in string, causing an invalid string
            return 0                              # with return "0".
        
        for i in range(len(find_number)):   # For loop for debugging not integer elements in the string.
            num_let = find_number[i]
            if num_let == '-':    # In case we have a "-" sign, it's stored in "sign_event" as "-1".
                sign_event = -1
            try:
                numbers.append(int(num_let))   # List of debugged integers.
            except:
                continue
                
        for j in range(len(numbers)):   # For loop to get the final integer value.
            x = len(numbers) - counter   # Integer element power.
            new_number = numbers[j] * (10 ** x)   # Every "new_number" has a power, that is related with the place of the integer
            final_number += new_number            # in the final value.
            if x == 0:
                break
            counter += 1 
        
        final_number = final_number * sign_event   # Multiplication with the "sign_event", only if sign_event == -1, the final
                                                   # number will be presented as a negative string.
        if final_number >= 2147483647:   # Special case (1): if the number in greater or equal than (2^31 - 1).
                return 2147483647   
        if final_number <= -2147483648:   # Special case (2): if the number is less or equal than (2^31).
                return -2147483648
        
        return final_number    # Return final integer value, END OF THE PROGRAM.
