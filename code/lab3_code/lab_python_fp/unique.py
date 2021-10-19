# Iterating through unique values of a data.
class Unique:
    def __init__(self, data, ignore_case=False):
        self.used_elements = set() 
        self.data = data
        self.index = 0
        self.ignore_case = ignore_case

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]      
                self.index = self.index + 1
                if (self.ignore_case):
                    current_lowered = current.lower();
                    if current_lowered not in self.used_elements:
                        self.used_elements.add(current_lowered)
                        return current
                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current
