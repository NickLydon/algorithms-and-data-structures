class Map:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size

    def put(self, key, data):
        slot = key % self.size
        slot_bucket = self.slots[slot]

        if slot_bucket == None:
            slot_bucket = [(key, data)]
        else:
            slot_bucket = [(k, v) for (k, v) in slot_bucket if k != key]
            slot_bucket.append((key, data))

        self.slots[slot] = slot_bucket

    def get(self, key):
        slot = key % self.size
        slot_bucket = self.slots[slot]
        if slot_bucket == None:
            return None
        else:
            matching_data = [data for (k, data) in slot_bucket if k == key]
            if len(matching_data) == 0:
                return None
            else:
                return matching_data[0]


mymap = Map()
mymap.put(1, "hello")
mymap.put(2, "goodbye")
mymap.put(3, "world")
mymap.put(4, "collision")
for i in range(1, 5):
    print(mymap.get(i))