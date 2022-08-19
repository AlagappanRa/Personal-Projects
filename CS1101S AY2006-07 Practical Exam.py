def split_list(lst, a):
    left_list, right_list = [], []
    for i in lst:
        if i <= a:
            left_list.append(i)
        else:
            right_list.append(i)
    return left_list, right_list

class Tamagotchi(object):
    def __init__(self, name):
        self.name = name
        self.words = []
        self.alive = 1

    def teach(self, *word):
        if not self.alive:
            return f"{self.name} is dead"
        
        for i in word:
            if i not in self.words:
                self.words.append(i)
        return
        
    def play(self):
        if not self.alive:
            return f"{self.name} is dead"
        string_output = f"{self.name} says "
        for i in self.words:
            string_output += i + " and " 
        return string_output[:-5]

    def kill(self):
        if not self.alive:
            return f"{self.name} is dead"
        self.alive = 0
        return 'tamagotchi killed'
