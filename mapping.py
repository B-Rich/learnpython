class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   #privte copy of original update() method

class MappingSubclass:
    def update(self, keys, values):
        # provide new signature for update()
        # but does not break __init__
        for item in zip(keys, values):
            self.items_list.append(item)
        
