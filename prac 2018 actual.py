from math import *


###############
# Question 1a #
###############
def smallest(*args):
    if not args:
        return None
    
    check = len(list(filter(lambda x: x == 0,args)))
    if check == len(args):
        return 0

    lst = []
    lst2 = []
    sorted_args = sorted(list(args))
    for i in sorted_args:
        if i == 0:
            lst.append(i)
        else:
            lst2.append(i)

    for index in range(1,len(lst2)):
        for y in lst:
            lst2.insert(index, y)
            lst.remove(y)
    return eval("".join(list(map(str, lst2))))


def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
test1a() 

###############
# Question 1b #
###############
def second_smallest(*args):
    if len(args) == 1:
        return None
    if not args:
        return None
    
    if min(args) == max(args):
        return None

    output = list(str(smallest(*args)))
    output[-1], output[-2] = output[-2],output[-1]
    return eval("".join(output))

def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1,1,1)==None)
     
test1b() 

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###############
# Question 2a #
###############

def most_common_major(filename, year):
    rows = read_csv(filename)
    years_filtered = list(filter(lambda row: row[3] != "na", list(filter(lambda row: row[0] == str(year), rows))))
    courses_and_grads = list(map(lambda x: (x[2],x[3]), years_filtered))
    init = 0
    for course in set(list(map(lambda x: x[0], courses_and_grads))):
        x = list(filter(lambda x: course == x[0], courses_and_grads))
        course_grad_total = sum(list(map(lambda y:int(y[1]), x)))
        if course_grad_total > init:
            init = course_grad_total
            course_max = course
    return course_max
        

def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2000)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2010)=="Engineering Sciences")

test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    rows = read_csv(filename)
    required_courses = map(lambda x: x[2], list(filter(lambda y: int(y[0]) <= start_year,list(filter(lambda row: row[3] == "na", rows)))))
    lst = []
    for course in required_courses:
        course_instances = list(filter(lambda row:row[2] == course, rows))
        for index,obj in enumerate(course_instances):
            if obj[3] != "na" and obj[3] != str(0):
                required_year = course_instances[index][0]
                if course not in list(map(lambda x:x[0], lst)):
                    lst.append([course,required_year])
                    break
    for i in lst:
        if int(i[1]) > end_year:
            lst.remove(i)
        elif int(i[1]) < start_year:
            lst.remove(i)
    return sorted(list(map(lambda x:(x[0],int(x[1])), lst)), key = lambda x: x[1])
                 
def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])

test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    rows = read_csv(filename)
    def valid(row):
        year, gender, course, grads = row 
        if (start_year == eval(year)) or (eval(year) == end_year):
            if course not in list(map(lambda x: x[1], new_courses(filename, start_year, end_year))):
                if grads != str(0) and grads != "na":
                    return True
        return False

    valid_outputs = list(filter(valid, rows[1:]))
    year_courses_and_grads = list(map(lambda x: (x[0],x[2],x[3]), valid_outputs))

    last_lst =[]
    for course in set(list(map(lambda x: x[1], year_courses_and_grads))):
        courses_4_instances = list(filter(lambda x: course == x[1], year_courses_and_grads))
        if len(courses_4_instances) < 4:
            continue
        temp1, temp2 = 0,0
        for year, course, grad in courses_4_instances:
            if eval(year) == start_year:
                temp1 += eval(grad)
            else:
                temp2 += eval(grad)
        percentage = (temp2 - temp1)/temp1
        last_lst.append([course, percentage])

    return list(map(lambda x:x[0], sorted(last_lst, key = lambda x:x[1], reverse = True)))[:k]
        

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])

test2c()
    
##############
# Question 3 #
##############

class Timeline(object):
    def __init__(self):
        self.output = []
        
    def born(self,name,year,lifespan):
        a = Person(name, year, lifespan)
        self.output.append(a)
        return a

    def get_people(self,year):
        lst = []
        for person in self.output:
            for birth_yr, max_life, iden, alive in person.timeline:
                if birth_yr <= year < max_life:
                    lst.append((person.name, iden))
                           
        return lst
                           
class Person(object):
    def __init__(self, name, birth_year, lifespan):
        self.name = name
        self.birth_year = birth_year
        self.lifespan = lifespan
        self.max_life = self.lifespan + self.birth_year
        self.timeline = [[birth_year, self.max_life, birth_year, True]]
        
    def jump(self,from_year, to_year, identity):
        # no need to check range because characters may void death by jumping to_year beyond death date
        for index,i in enumerate(self.timeline):
            start, end, iden, alive = i
            if iden == identity:
                #jump forward => create new timeline list
                if to_year > from_year:
                    self.timeline.insert(index + 1, [to_year, self.max_life, from_year, True])
                    self.timeline[index][1] = from_year
                    return 
                
                #jump backwards => add a backward instance and delete subsequent instances
                elif from_year > to_year:
                    self.timeline = self.timeline[:index + 1]
                    self.timeline[index][1] = from_year
                    self.timeline.append([to_year, self.max_life, from_year, True])
                    return 
        else:
            return "Invalid Input"
        
    def kill(self, death_year, person, identity):
        for index,i in enumerate(person.timeline):
            start, end, iden, alive = i
            if iden == identity and alive:               
                person.timeline = person.timeline[:index + 1]
                person.timeline[index][1] = death_year
                person.timeline[index][3] = False
                
                return True
        else:
            return False 

def test3():
    print('=== Q3 ===')
    t = Timeline()
    thor = t.born("Thor",518,5000)
    thanos = t.born("Thanos",1950,1000000)

    print(t.get_people(2017))
    print(thor.kill(2018,thanos,1950)) # whoops. Violence. :'(
    print(not thor.kill(2018,thanos,1950)) # Can't kill him twice!
    print("kills", t.get_people(2018)) # Thanos dead.
    
    thor.jump(2023,2013,518)
    thor.jump(2014,2024,2023)

    print(set(t.get_people(2013)))
    print(set(t.get_people(2014)))

    print(t.get_people(2022))
    print(t.get_people(2023)==[])
    print(t.get_people(2024))

    thanos.jump(2014,2024,1950)
    print(set(t.get_people(2024))==set([('Thor', 2014), ('Thanos', 2014)]))

    # New Thor and old Thanos jumped so only old Thor left
    print(t.get_people(2014)==[('Thor', 518)]) 
    print(t.get_people(2017)==[('Thor', 518)])

    #Thanos is no longer around to die. 
    print(not thor.kill(2018,thanos,1950))


test3()
