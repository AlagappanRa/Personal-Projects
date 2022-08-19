def col_sum(m):
    if m == []:
        return []

    res = [0]*len(m[0]) # or res = [0 for i in range(len(m[0]))]

    for row in m:
        for i in range(len(row)):
            res[i] += row[i]
            
    return res
        
# col_sum with map	
def col_sum(m):
    if m == []:
        return []

    res = []
    for i in range(len(m[0])): # column index
#        print(i, ': ', list(map(lambda row:row[i], m)))
        res.append(sum(map(lambda row:row[i], m)))

    return res

# one liner
def col_sum(m):
    if m == []:
        return []

    res = [sum(map(lambda row:row[i], m)) for i in range(len(m[0]))]
    return res
    
m = [[1,2,3],[4,5,6],[7,8,9]]
print(col_sum(m))

def row_sum(m):
    if m == []:
        return []
    res = []
    for row in m:
        res.append(sum(row))
    return res

print(row_sum(m))

# map
def row_sum(m):
    return list(map(lambda row: sum(row), m))
# no need to check for empty list
print(row_sum(m))

def transpose(m):
    if m == []:
        return []

    new_m = []
    for i in range(len(m[0])): # column in matrix
        new_m.append(list(map(lambda x:x[i], m)))
                   
    m.clear()
    m.extend(new_m)
    return m

def transpose(m):
    if m == []:
        return []
    new_m = [list((map(lambda row:row[i], m))) for i in range(len(m[0]))]
    m.clear()
    m.extend(new_m)
    return m

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 =  transpose(m1)
print(m2)
print(m2 is m1)

'''
a = [[0]*4]*3 => [ref]*3 (fake list)
print(a)
a[0][0] = 1
print(a)
# [[1,0,0,0],[1,0,0,0],[1,0,0,0]]
'''

'''
modified
a = [[0]*4 for i in range(3)]
'''

def transpose(m):
    if m == []:
        return []
    new_m = [[0]*len(m)for i in range(len(m[0]))] #mirror list
    for i in range(len(m)): # idx row
        for j in range(len(m[0])): #idx col
            new_m[j][i] = m[i][j]
    m.clear()
    m.extend(new_m)
    return m

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 =  transpose(m1)
print(m2)
print(m2 is m1)


def transpose(m):
    #if m == []:
    #    return []
    # new_m = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    new_m = list(map(list, zip(*m)))
    m.clear()
    m.extend(new_m)
    return m

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 =  transpose(m1)
print(m2)
print(m2 is m1)

students = [
('tiffany', 'A', 15),
('jane', 'B', 10),
('ben', 'C', 8),
('simon', 'A', 21),
('eugene', 'A', 21),
('john', 'A', 15),
('jimmy', 'F', 1),
('charles', 'C', 9),
('freddy', 'D', 4),
('dave', 'B', 12)]

names, grades, scores = zip(*students)
print(names)
print(grades)
print(scores)


def mode_score(students):
    scores = []
    count = []
    for name, grade, score in students:
        is_appeared = False
        for i in range(len(scores)):
            if score == scores[i]:
                count[i] += 1
                is_appeared = True

        if not is_appeared:
            scores.append(score)
            count.append(1)

    res = []
    max_count = 0
    for i in range(len(scores)):
        if count[i] > max_count:
            max_count = count[i]
            res = [scores[i]]
            
        elif count[i] == max_count:
            res.append(scores[i])

    return res


def mode_score(students):
    scores = list(map(lambda stu:stu[-1], students))
    max_count = max(map(lambda x: scores.count(x), scores))
    res = list(filter(lambda x:scores.count(x) == max_count, scores))
    return list(set(res))

    # alternatively cast the list to a set, apply count to find unique element

print(mode_score(students))
    

def top_k(students, k):
    scores = sorted(list(map(lambda stu:stu[-1], students)))
    k_th_score = scores[-k]
    k_th_stu = list(filter(lambda stu: stu[-1] >= k_th_score, students))
    return sorted(sorted(k_th_stu, key = lambda stu: stu[0]), key = lambda stu:stu[-1], reverse = True)
    

print(top_k(students,3))




