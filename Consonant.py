def solve(substring):
    def get_consonant_value(c):
        return ord(c) - ord('a') + 1
    #Function that is used to get the position of a letter in the alphabet by subtracting their integer representation from that of letter a
    max_value = 0
    current_value = 0
    
    for char in substring:
        if char in "aeiou":
            maximum_value = max(max_value, current_value)
            current_value = 0
            #when a vowel is identified, the new maximum value is set and current value reset to  0 
        else:
            current_value += get_consonant_value(char)
    # When all characters have been iterated, the maximum consonant value is established

    highest_value = max(maximum_value, current_value)
    return highest_value

print(solve("jumbo")) 
 
