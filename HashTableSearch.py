def search(self,item):
    startslot = self.hashfunction(item,len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and not found and not stop:
        if self.slots[position] == item:
            found = True
            data = self.data[position]
        else:
            position = self.rehash(position,lesn(self.slots))
            if position == startslot:
                stop = True
    return data
