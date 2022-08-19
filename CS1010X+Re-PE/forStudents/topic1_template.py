
plain = [ ['0','1','2','3','4','5'],
           ['6','7','8','9','A','B'],
           ['C','D','E','F','G','H'],
           ['I','J','K','L','M','N'],
           ['O','P','Q','R','S','T'],
           ['U','V','W','X','Y','Z'] ]

message = "HELLO 1 2 3"
# Q1
def encrypt(message, plain, c1, c2):
    d = {}
    for row in plain:
        for index,element in enumerate(row):
            d[element] = c2[index]

    for column in list(map(list, zip(*plain))):
        for index, element in enumerate(column):
            value_inside = d[element]
            d[element] = c1[index] + value_inside

    final = ""
    for i in message:
        if i == " ":
            final += i
        else:
            final += d[i]
    return final
            

secret = encrypt(message, plain, '062849', 'abcdef')
print(secret)

# Q2
def decrypt(secret, plain, c1, c2):
    d = {}
    for row in plain:
        for index,element in enumerate(row):
            d[element] = c2[index]

    for column in list(map(list, zip(*plain))):
        for index, element in enumerate(column):
            value_inside = d[element]
            d[element] = c1[index] + value_inside
            
    init = ""
    d_items = list(d.items())
    secret_list = secret.split()
    for element in secret_list:
        for i in range(2, len(element) + 2, 2):
            snip = element[(i-2):i]
            for key, value in d_items:
                if value == snip:
                    init += key
                    break
        init += " "
        
    return init[:-1]

print( decrypt(secret, plain, '062849', 'abcdef'))

# Q3
def index(tree, x):
    lst = []
    init_tree = tree
    def helper(tree, x, idx_list):
        for index, item in enumerate(tree):
            if x is item:
                lst.extend(idx_list + [index])
            
            elif type(item) == list:
                helper(item, x, idx_list + [index])
            
    helper(tree, x, [])
    string = ""
    if not lst:
        return None
    else:
        for i in lst:
            string += f"{i}-"
            
    return string[:-1]



lst = [0,[1,2,3,4],[5,6,[7,[8,9]]]]
for i in range(11):
    print("index of", i, "in", lst, "is:", index(lst, i))

