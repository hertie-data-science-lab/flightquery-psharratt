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



# create a sorted map called flightquery
# aim is to add flights in a particular timeframe and make them searchable 
# testing in file


# FQ GPT
class FlightQuery(SortedTableMap):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError('Map is empty')
        flight = Flight(key, None, None, None)
        i = self._find_index(flight, 0, len(self.data) - 1)
        if i == len(self.data):
            return None
        if self.data[i].origin != flight.origin or \
                self.data[i].destination != flight.destination:
            return None
        return self.data[i]

    def __setitem__(self, key, value):
        flight = Flight(key[0], key[1], key[2], key[3])
        i = self._find_index(flight, 0, len(self.data) - 1)
        if i < len(self.data) and self.data[i].origin == flight.origin and \
                self.data[i].destination == flight.destination:
            self.data[i] = flight
        else:
            self.data.insert(i, flight)

    def __delitem__(self, key):
        flight = Flight(key, None, None, None)
        i = self._find_index(flight, 0, len(self.data) - 1)
        if i == len(self.data) or self.data[i].origin != flight.origin or \
                self.data[i].destination != flight.destination:
            raise KeyError('Flight not found')
        self.data.pop(i)

    def __iter__(self):
        for flight in self.data:
            yield flight

    def __reversed__(self):
        for flight in reversed(self.data):
            yield flight

    def _find_index(self, flight, low, high):
        if high < low:
            return high
        mid = (low + high) // 2
        if self.data[mid] == flight:
            return mid
        elif self.data[mid] < flight:
            return self._find_index(flight, mid + 1, high)
        else:
            return self._find_index(flight, low, mid - 1)

    def flights_from_city(self, origin, destination, departure_date):
        flights = []
        for flight in self.data:
            if flight.origin == origin and flight.destination == destination and \
                    (departure_date is None or flight.departure_date == departure_date):
                flights.append(flight)
        return flights
