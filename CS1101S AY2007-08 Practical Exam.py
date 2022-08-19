def is_palindrome(num):
    return str(num) == str(num)[::-1]

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],  accumulate(fn, initial, seq[1:]))

def filter_and_sort(list1, list2):
    l1 = sorted(list1)
    l2 = sorted(list2)
    set1, set2 = set(l1), set(l2)
    intersection_set = set1.intersection(set2)
    filtered_sorted =  list(filter(lambda x: x in list(intersection_set), list2))
    return accumulate(lambda x,y: x + y, [], [list(filter(lambda x: x == i, filtered_sorted)) for i in list1])

print(filter_and_sort([1, 2, 3], [4, 5, 1, 3, 3, 1, 2]))

class Transformer(object):
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle_name = vehicle
        self.current_status = "robot"
        self.alive = True
    
    def status(self):
        if not self.alive:
            return f"{self.name} is destroyed"
        return f"{self.name} is in {self.current_status} form"
    
    def transform(self):
        if not self.alive:
            return False
        if self.current_status == "robot":
            self.current_status = self.vehicle_name
        else:
            self.current_status = "robot"

    def attack(self, defender):
        if not self.alive or not defender.alive:
            return False
        if isinstance(self, Decepticon):
            self_type = "D"
        else:
            self_type = "A"

        if isinstance(defender, Autobot):
            defender_type = "A"
        else:
            defender_type = "D"

        if self_type == defender_type:
            defender.alive = False
        else:
            if self_type == "D":
                self.alive = False
            else:
                defender.alive = False
                
class Decepticon(Transformer):
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)

class Autobot(Transformer):
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)
