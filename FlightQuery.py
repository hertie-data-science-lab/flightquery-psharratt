from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"
        pass

    def query(self, k1, k2):
        pass


a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value
print(len(a))

k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)