def compute_percentile(verbal, maths, writing):
    total = verbal + maths + writing
    if total >= 2200:
        return 99
    elif total >= 2000:
        return 95
    elif total >= 1500:
        return 50
    else:
        return 10

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

def compute_iq_score(verbal, maths, writing):
    IQ = (0.095 * maths) + (0.003 * verbal) + 50.241
    return eval(str(IQ//1)[:-2] + str(IQ%1)[1:4])

def ten_ten_as(number):
    num_list = list(map(lambda x: eval(x[1])*2 if x[0] % 2 != 0 else eval(x[1]) , enumerate(list(str(number))[::-1])))
    return sum(list(map(int,list(accumulate(lambda x,y: str(x) + str(y), "", num_list)))))


print(ten_ten_as(323456789))
print(ten_ten_as(55010011))
print(ten_ten_as(54123656))
print(ten_ten_as(45223))

def valid(number):
    check_no = ten_ten_as(number)
    if not check_no % 7:
        return True
    return False

def issuer(number):
    if not valid(number):
        return "Invalid"
    digits = int(str(number)[:2])
    if 31 <= digits <= 35:
        return "East"
    if 51 <= digits <= 55:
        return "West"
    else:
        return "Central"
