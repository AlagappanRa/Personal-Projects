def get_century(year):
    century = year//100 + 1
    ordinal = get_ordinal(century)
    return f"The year {year} falls in the {century}{ordinal} century."

def get_ordinal(century):
    last_digit = century % 10
    if last_digit == 1 and century != 11:
        return "st"
    elif last_digit == 2 and century != 12:
        return "nd"
    elif last_digit == 3 and century != 13:
        return "rd"
    else:
        return "th"

print(get_century(78))
print(get_century(1900))
print(get_century(4112))
print(get_century(1109))
print(get_century(20000))

# Define helper functions here:
def has_must_have_digit(must_have_digit, number):
    return str(must_have_digit) in str(number)
    
def has_factor_digit(factor_digit, number):
    return not(number % factor_digit)

def winners(factor_digit, must_have_digit, num_of_participants):
    count = 0
    for number in range(1, num_of_participants + 1):
        if has_factor_digit(factor_digit, number) and has_must_have_digit(must_have_digit, number):
            count += 1
    return count

print(winners(3, 5, 100) == 6)
print(winners(9, 1, 15) == 0)
print(winners(7, 7, 200) == 5)