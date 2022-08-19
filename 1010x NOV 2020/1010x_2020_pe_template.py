##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def ET_number(number, mapping):
    base = len(mapping)
    res = ""
    if number == 0:
        return mapping[0]

    while number > 0:
        remainder = number % base
        number = number//base
        res += mapping[remainder]

    return res[::-1]

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14')
    print(ET_number(6, ('0','4')) == '440')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')

test1a()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

def max_ET_number(ET_numbers, mapping):
    lst = []
    for number in ET_numbers:
        base = len(mapping)
        number_old = 0
        for digit in number:
            remainder = mapping.index(digit)
            number_old = number_old * base + remainder
        
        lst.append(number_old)

    max_num = max(lst)
    return ET_numbers[lst.index(max_num)]

def test1b():
    print("=====Test 1b=====")
    # checking for normal decimal
    print(max_ET_number(('1','2','3','4','5'), ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for swapped digits
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    # different bases
    print(max_ET_number(('14','15'),('0','1','2','3','5','4'))=='14')
    print(max_ET_number(('707','700','770'),('0','7'))=='770')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311','713','413'),('7','1','3','4'))=='413')
    print(max_ET_number(('aba', 'abc', 'ca', 'cb'), ('a', 'b', 'c')) == 'cb')

test1b()

############################
# Question 2: Tesla stocks #
############################

import csv
import datetime

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

######################################################
# Question 2a: Retrieving tweets by date [ 3 Marks ] #
######################################################
def get_tweet_by_date(date):
    date_given = datetime.datetime.strptime(date, "%m/%d/%Y")
    rows = read_csv('tweets.csv')
    rows = rows[1:]
    final_output = ()
    for i in rows:
        date_incoming = datetime.datetime.strptime(i[6], "%m/%d/%Y")
        if date_incoming == date_given:
            final_output += (i[2]),
    return final_output
    

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

test2a()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    date_given = datetime.datetime.strptime(date, "%m/%d/%Y")
    req_1 = get_tweet_by_date(date)
    rows = read_csv('TSLA.csv')
    rows = rows[1:]
    lst = []
    if not req_1:
        return None
    
    for i in rows:
        date_incoming = datetime.datetime.strptime(i[0], "%m/%d/%Y")
        for day in range(0,6):
            new_date = date_given + datetime.timedelta(days = day)
            if new_date == date_incoming:
                lst.append(eval(i[1]))
    return (req_1 + (lst,))
    

def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013') == ("Just want to say thanks to customers & investors that took a chance on Tesla through the long, dark night. We wouldn't be here without you.", [55.790001, 69.400002, 76.760002, 87.800003]))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

test2b()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def money_tweets(start_date, end_date):
    start_date_d = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end_date_d = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    rows = read_csv("tweets.csv")
    rows = rows[1:]
    lst = []
    for i in rows:
        date_incoming = datetime.datetime.strptime(i[6], "%m/%d/%Y")
        if start_date_d <= date_incoming <= end_date_d:
            input_txt = tweet_effect(i[6])
            list_of_numbers = input_txt[-1]
            lst.append([i[2], max(list_of_numbers) - min(list_of_numbers)])

    if not lst:
        return None
    max_val = max(tuple(map(lambda x:x[1], lst)))
    b = tuple(filter(lambda x:x[1] == max_val, lst))
    a = (tuple(map(lambda x: x[0], b)),)
    a += (max_val,)
    return a
    
def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020') == (('Ice cream sundae in a martini glass https://t.co/zAVFlOsYkM', 'Super exciting day coming up! https://t.co/7ZdFsJE9zR', 'https://t.co/lQWpSwtRj7'), 22.669983000000002))
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))

test2c()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbour = None
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_pos(self):
        return (self.x, self.y)
    def attach(self, car):
        avaliable = ((self.get_pos()[0]-1, self.get_pos()[1]),
                     (self.get_pos()[0]+1, self.get_pos()[1]),
                     (self.get_pos()[0], self.get_pos()[1] + 1),
                     (self.get_pos()[0], self.get_pos()[1] - 1))
        
        if car.get_pos() in avaliable:
            engine.train.append(car)
            return "Attached."
        
        else:
            return "Can't attach."
    

class engine (carriage):
    train = []  
    def __init__(self, x, y):
        super().__init__(x,y)
        engine.train.insert(0, self)
            
    def matrix_repr(train):
        train_tuples = list(map(lambda car: car.get_pos(), train))
        matrix = []
        for j in range(5):
            matrix.append([" " for i in range(13)])

        for a,b in train_tuples:
            matrix[a][b] = "X"
        
        for i in matrix:
            print(i)
  
    def move(self, track):
        for i in track:
            new_train = engine.train[:-1]
            new_train_mapping = list(map(lambda car: car.get_pos(), new_train))
            train = engine.train
            print(engine.matrix_repr(train))
            
            if i == "l":
                if (train[0].x - 1, train[0].y) in new_train_mapping:
                    return "Collision!"
                else:
                    for index,tup in enumerate(new_train_mapping):
                       train[index + 1].x, train[index + 1].y = tup[0], tup[1]
                       
                    train[0].x, train[0].y  = train[0].x - 1, train[0].y
                    
            elif i == "r":
                if (train[0].x + 1, train[0].y) in new_train_mapping:
                    return "Collision!"
                else:
                    for index,tup in enumerate(new_train_mapping):
                       train[index + 1].x, train[index + 1].y = tup[0], tup[1]
                       
                    train[0].x, train[0].y  = train[0].x + 1, train[0].y
                    
            elif i == "u":
                if (train[0].x, train[0].y + 1) in new_train_mapping:
                    return "Collision!"
                else:
                    for index,tup in enumerate(new_train_mapping):
                       train[index + 1].x, train[index + 1].y = tup[0], tup[1]
                       
                    train[0].x, train[0].y  = train[0].x, train[0].y + 1
                    
            elif i == "d":
                if (train[0].x, train[0].y - 1) in new_train_mapping:
                    return "Collision!"
                else:
                    for index,tup in enumerate(new_train_mapping):
                        train[index + 1].x, train[index + 1].y = tup[0], tup[1]
                       
                    train[0].x, train[0].y  = train[0].x, train[0].y -1
                    
        
        return None
        
def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    # Checking for get_x and get_y functions
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    # Checking for get_pos function
    print(c0.get_pos() == (1,0))

    # Attaching carraiges together to build the train
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")

    # c1 and c4 are not adjacent
    print(c1.attach(c4) == "Can't attach.")
    
    print(c1.attach(c0) == "Attached.")

    # Checking for movement
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 3), (2, 2), (1, 2), (1, 1), (1, 0)))
    print(e.move('uuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 6), (2, 5), (2, 4), (2, 3), (2, 2)))
    print(e.move('r') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 6), (2, 6), (2, 5), (2, 4), (2, 3)))
    print(e.move('uuuuuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 12), (3, 11), (3, 10), (3, 9), (3, 8)))
    print(e.move('rdll') == "Collision!")
    #print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    #print(e.move('ldrr') == "Collision!")
    #print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    #print(e.move('d') == None)
    #print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 10), (4, 11), (4, 12), (3, 12), (3, 11)))

test3()
