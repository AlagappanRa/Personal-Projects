# 2048 Game

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    return [[0 for i in range(n)] for j in range(n)]

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    if not has_zero(mat):
        return mat
    else:
        # create a coordinate cache for the 0s
        # use randint for the coordinate cache list
        # replace 0 for the coordinate
        coordinate_cache = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    coordinate_cache.append((i,j))
                    
        index = randint(0,len(coordinate_cache)-1)
        k,l = coordinate_cache[index]
        mat[k][l] = 2
        return mat

###########
# Task 2  #
###########
def possible_moves(mat):
    # exclude the top and bottom indices
    for i in range(1, len(mat)):
        # exclude the first row and first column 
        for j in range(1, len(mat[0])):
            # check if up, left are equal
            at = mat[i][j]
            if mat[i-1][j] == at or mat[i][j-1] == at:
                return True
    # check left of row 0
    for k in range(1, len(mat)):
        if mat[0][k] == mat[0][k-1]:
            return True
        
    # check top of column 0 
    for m in range(1, len(mat[0])):
        if mat[m][0] == mat[m-1][0]:
            return True

    return False 

def game_status(mat):
    flattened_mat = flatten(mat)
    if 2048 in flattened_mat:
        return 'win'
        
    elif has_zero(mat):
        return 'not over'
        
    elif not possible_moves(mat):
        return 'lose'

    else:
        return 'not over'


###########
# Task 3a #
###########

def transpose(mat):
    return list(map(list, zip(*mat)))



###########
# Task 3b #
###########

def reverse(mat):
    return list(map(lambda x:x[::-1], mat))



############
# Task 3ci #
############

def merge_left(mat):
    new_lst = []
    score = 0
    for row in mat:
        a = list(filter(lambda x: x != 0, row))
        i = 0
        while i < len(a) - 1:
            if a[i] == a[i+1]:
                a[i] *= 2
                a[i+1] = 0
                score += a[i]
                i += 2
            else:
                i += 1
    
        b = list(filter(lambda x: x != 0, a))
        c = b + [0 for i in range(len(row) - len(b))]
        new_lst.append(c)
        
    return new_lst, new_lst != mat, score



#############
# Task 3cii #
#############

def merge_right(mat):
    a,b,c = merge_left(reverse(mat))
    return reverse(a),b,c

def merge_up(mat):
    a,b,c = merge_left(transpose(mat))
    return transpose(a),b,c

def merge_down(mat):
    a,b,c = merge_right(transpose(mat))
    return transpose(a),b,c


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:
# Achieving 2048 everytime may not be possible. We can implement scaled down checks. For example, instead
# of testing 2048 in matrix, we can test 128 in matrix, 32 in matrix, 64 in matrix, etc. If the game
# stops for all those tests, we can reasonably extrapolate it to 2048 will work as a win condition.


##########
# Task 4 #
##########

'''
# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}
'''
# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
# gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return [mat, increment]

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############
stack_of_records = []

def make_new_records():
    return stack_of_records*0

def push_record(new_record, stack_of_records):
    init_len = len(stack_of_records)
    idx = init_len % 3
    if idx < 3:
        stack_of_records.append(new_record)
    else:
        stack_of_records[idx] = new_record
    return stack_of_records

def is_empty(stack_of_records):
    return not stack_of_records 

def pop_record(stack_of_records):
    return ((None, None) if is_empty(stack_of_records) else stack_of_records.pop())

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return [matrix, total_score, records]

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def get_records(state):
    return state[2]

def make_new_game(n):
    matrix = new_game_matrix(n)
    add_two(matrix)
    add_two(matrix)
    total_score = 0
    records = make_new_records()
    return make_state(matrix, total_score, records)

def fn(func,state):
    init_score = get_score(state)
    init_matrix = get_matrix(state)
    matrix, is_valid, score = func(init_matrix)
    final_score = init_score + score
    records = stack_of_records
    if is_valid:
        matrix = add_two(matrix)
        new_record = make_new_record(matrix, score)
        records = push_record(new_record, stack_of_records)
      
    game_state = make_state(matrix, final_score, records)
    print(stack_of_records)
    print(stack_of_records[-1])
    return game_state, is_valid
    
def left(state):
    return fn(merge_left,state)

def right(state):
    return fn(merge_right,state)

def up(state):
    return fn(merge_up,state)

def down(state):
    return fn(merge_down,state)

# NEW FUNCTIONS TO DEFINE
def undo(state):
    if pop_record(stack_of_records) == (None,None):
        return pop_record(stack_of_records)
    return stack_of_records[-1]


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
gamegrid = GameGrid(game_logic)

