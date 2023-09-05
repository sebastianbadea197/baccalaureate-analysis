def roman_to_int(s: str) -> int:
    """
    Convert Roman numeral to integer.
    """
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            # If the current numeral is larger than the previous one, 
            # subtract twice the value of the previous numeral (because we added it once already)
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
        
    return total

# Test the function
test_romans = ["I", "IV", "IX", "XII", "XV", "XL", "XC", "C", "D", "M", "LX", "XCIV"]
{roman: roman_to_int(roman) for roman in test_romans}
