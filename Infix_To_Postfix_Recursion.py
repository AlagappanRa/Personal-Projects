def postfix(tree):
    if tree == ():
        return ()
        
    elif type(tree) != tuple:
        return (tree,)
        
    else:
        return postfix(tree[0]) + postfix(tree[2]) + postfix(tree[1])

print(postfix((1, '+', 2)))
print(postfix((3, '*', (1, '+', 2))))
print(postfix(((1, '+', 25), '*', 3)))
