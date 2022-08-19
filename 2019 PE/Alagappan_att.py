# difference between indexes + 1 =  total_matchsticks left
# match sticks removed = first_removed - last_removed + 1
# start 1, end 20

def valid_move(game, start, end):
    selected_start_lst, selected_end_lst = None, None
    for inner_lst in game:
        first, last = inner_lst
        if start in range(first, last + 1):
            selected_start_lst = inner_lst
            continue
        
        if end in range(first, last + 1):
            selected_end_lst = inner_lst
            break

    if not selected_start_lst and not selected_end_lst:
        return False
        
    if selected_start_lst == selected_end_lst or(not selected_start_lst or not selected_end_lst):
        return True
    
    return False

    
def make_move(game, start, end):
    
    def game_storer(message, *game):
        call_counter = 0
        game_state = None
        if message == "r":
            if call_counter == 0:
                call_counter += 1
                return game[0]
            else:
                return game_state
        
        elif message == "u":
            game_state = game[0].copy()

            
    game = game_storer("r", game)
    for index, inner_lst in enumerate(game):
        first, last = inner_lst
        if start in range(first, last + 1):
            selected_start_lst = inner_lst
            chosen_index = index
            break
        
    first, last = selected_start_lst
    if start == last:
        game.remove(selected_start_lst)
        game.insert(index, [first, start-1])
        
    elif start in range(first, last + 1) and end in range(first, last):
        game.remove(selected_start_lst)
        game.insert(index, [first, start-1])
        game.insert(index + 1, [end + 1, last])

    elif end not in range(first, last):
        game.remove(selected_start_lst)
        game.insert(index, [first, start-1])

    game_storer("u", game)
    return game


import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []
    with open(csvfilename, encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

import math
def get_distance(lat1, long1, lat2, long2):
    """
    Takes in two pairs of lat-long float coordinates,
    returns the distance between the two coordinates
    """
    return round(math.sqrt( (lat1-lat2)**2 + (long1-long2)**2 ), 5)

def k_nearest_listings(data, given_lat, given_lon, k):
    rows = read_csv(data)
    rows = rows[1:]
    d = {}
    for data in rows:
        distance = get_distance(given_lat, given_lon, eval(data[4]), eval(data[5]))
        d[data[0]] = distance

    sorted_mappings = sorted(d.items(), key = lambda x: x[1])
    required = sorted_mappings[:k]
    return list(map(lambda x: eval(x[0]), required))
        
def neighbourhood_price_per_region(data, string_val):
    rows = read_csv(data)
    rows = rows[1:]
    d = {}
    for data in rows:
        if eval(data[-1]) >= 1 and data[2] == string_val:
            if data[3] in d:
                d[data[3]] += [eval(data[-2])]
            else:
                d[data[3]] = [eval(data[-2])]

    for key in d:
        values = d[key]
        number_of_objects = len(values)
        average = sum(values)/number_of_objects
        average_rounded = round(average, 2)
        d[key] = average_rounded

    return d

class Doll(object):
    def __init__(self, name):
        self.name = name
        self.contains = None
        self.encased_by = None

    def encase(self, other_doll):
        if self.contains:
            return f"{self.name} already contains {self.contains.name}"
        if self.encased_by:
            return f"{self.name} is currently encased in {self.encased_by.name}"
        if other_doll.encased_by:
            return f"{other_doll.name} is currently encased in {other_doll.encased_by.name}"
        else:
            self.contains = other_doll
            other_doll.encased_by = self
            return f"{self.name} encases {other_doll.name}"

    def release(self):
        if self.encased_by:
            return f"{self.name} is currently encased in {self.encased_by.name}"
        elif not self.contains:
            return f"{self.name} does not contain any dolls"
        else:
            self.contains.encased_by = None
            self.contains = None
            return f"{self.name} releases {self.contains.name}"

    def name_of(self):
        return self.name

    def get_mother(self):
        return self.encased_by

    def get_daughter(self):
        return self.contains

    def doll_series(self):
        def recursion_down(obj):
            if obj.contains == None:
                return ()
            if obj.contains:
                return (obj.contains.name,) + recursion_down(self.doll.contains)

        def recursion_up(obj):
            if obj.encased_by == None:
                return ()
            if obj.contains:
                return (obj.encased_by.name,) + recursion_up(self.doll.encased_by)
            
        return recursion_up(self) + (self.name,) + recursion_down(self)
        
    
    def deeply_contains(self, other):
        flag = 0
        def recursion(obj, other):
            if obj.contains == None:
                return 
            if obj.contains == other:
                flag = 1
                return 
            if obj.contains:
                return recursion(self.doll.contains, other)
        recursion(self, other)
        if flag:
            return True
        else:
            return False
