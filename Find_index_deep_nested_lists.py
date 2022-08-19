from random import randint
def output_processor(lst, init_tree):
    if lst == []:
        return None
    str_out = str(init_tree)
    for i in lst[0]:
        str_out += str([i])
    return str_out

def find_x(x, tree):
    lst = []
    init_tree = tree
    def helper(tree, x, idx_list):
        for index, item in enumerate(tree):
            if x is item:
                lst.append(idx_list + [index])
            
            elif type(item) == list:
                helper(item, x, idx_list + [index])

        return output_processor(lst, init_tree)
                
    return helper(tree, x, [])

tree = [501,502,[503,[504,555,634,[724,9234]],[10324]],1134,[1234],[1343,[1344],1345,[1346,1437]]]
print(find_x(1344, tree))
print(find_x(5, [1, 5]))
print(find_x(3, [1,5]))
print(find_x(5, [1, 3, [5], 3]))

