#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    n = get_table_state(table)
    flip_coins(table, n)

# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    n = get_table_state(table)
    flip_coins(table, n)

# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(check_solved(t4_2))

########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    
    if check_solved(table) == False:
        flip_coins(table, (1,0))

    else:
        True

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    A = ((1,0,1,0),)
    B = ((1,1,0,0),)
    C = ((1,0,0,0),)

    n = A + B + A + C + A + B + A
    for i in n:
      if not check_solved(table):
          flip_coins(table, i)

def solve_4_1(table):
    A = ((1,0,1,0),)
    B = ((1,1,0,0),)
    C = ((1,0,0,0),)
    
    n = A + B + A + C + A + B + A
    left = A
    x = len(n)
    while x >= 2:
        x = x//2
        result = left + n[x] + left
        left = result

    for i in result:
        if not check_solved(table):
          flip_coins(table, i)
    
# test:
#t4_4 = create_table(4)
# solve_4(t4_4)
# print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t4_4_1_run = create_table(4)
run(t4_4_1_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    """ Write your code here """
    pass

# test:
# t4_5 = create_table(4)
# solve(t4_5)
# print(check_solved(t4_5))

# t8_5 = create_table(8)
# solve(t8_5)
# print(check_solved(t8_5))

# t16_5 = create_table(16)
# solve(t16_5)
# print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.

