# generate code to convert roman numerals to integers   

def roman_to_int(roman):
    roman = roman.upper()
    roman = roman.replace("IV", "IIII")
    roman = roman.replace("IX", "VIIII")
    roman = roman.replace("XL", "XXXX")
    roman = roman.replace("XC", "LXXXX")
    roman = roman.replace("CD", "CCCC")
    roman = roman.replace("CM", "DCCCC")
    total = 0
    for char in roman:
        if char == "I":
            total += 1
        elif char == "V":
            total += 5
        elif char == "X":
            total += 10
        elif char == "L":
            total += 50
        elif char == "C":
            total += 100
        elif char == "D":
            total += 500
        elif char == "M":
            total += 1000
    return total    

print("Roman Numeral Converter")    
print("Enter a roman numeral to convert to an integer")
print("Enter 'exit' to quit")
while True:
    roman = input("Enter a roman numeral: ")
    if roman == "exit":
        break
    else:
        print("The integer value is", roman_to_int(roman))
print("Goodbye")