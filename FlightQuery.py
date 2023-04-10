"""
Submitted on 9th April 2023

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati


Notes: 
    - Flight databases can be modeled as maps with Flight objects as keys and flight details as values. 
    - By ordering the keys lexicographically, we can efficiently find flights between cities, even with some flexibility in departure date and time. 
    - In this case, we used a sorted map implementation incorporating 'find range(k1, k2)'.
    - Additionally, our solutio can handle 'None' values in the earliest and latest time and date user queries

Assumptions:
    - It is necessary to implement the find range method in one of the files and the book recommends implementing the method in the SortedTable Map class, which we did.
    - The current implementation of the code excludes the lower limits of searches.
    - We added more observations and values to the observations to test the robustness of the code.

"""


from SortedTableMap import *


# Defining FlightQuery class as a subclass of SortedTableMap
class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    
    # Define a nested Key class to be used as keys in the table
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"
        
        # Constructor for Key objects with origin, destination, date and time
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        # Less than comparison between Key objects
        def __lt__(self, other):
            if self._origin != other._origin:
                return self._origin < other._origin
            if self._dest != other._dest:
                return self._dest < other._dest
            if self._date != other._date:
                if self._date is None:
                    return False
                if other._date is None:
                    return True
                return self._date < other._date
            if self._time != other._time:
                if self._time is None:
                    return False
                if other._time is None:
                    return True
                return self._time < other._time
            return False
        
        # Greater than comparison between Key objects
        def __gt__(self, other):
            if self._origin != other._origin:
                return self._origin > other._origin
            if self._dest != other._dest:
                return self._dest > other._dest
            if self._date != other._date:
                if self._date is None:
                    return True
                if other._date is None:
                    return False
                return self._date > other._date
            if self._time != other._time:
                if self._time is None:
                    return True
                if other._time is None:
                    return False
                return self._time > other._time
            return False

        def __ge__(self, other):
            return not self.__lt__(other)

        def __le__(self, other):
            return not self.__gt__(other)



        # Define a string representation of the Key object
        def __str__(self):
            return "Origin: {0}, Destination: {1}, Date: {2}, Time: {3}".format(self._origin, self._dest, self._date, self._time)
        
    # Finds all key-value pairs between start and stop    
    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, False)  # find first result

        while j < len(self._table) and (stop is None or self._table[j]._key <= stop):
            if start is None or self._table[j]._key >= start:
                yield (self._table[j]._key, self._table[j]._value)
            j += 1

    # Define a query method that finds all key-value pairs between k1 and k2 (exclusive)
    def query(self, k1, k2):
        return self.find_range(k1, k2)
    
    # Returns the minimum flight date
    def get_min_date(self):
        if not self:
            return None
        min_date = None
        for item in self._table:
            key = item._key
            if min_date is None or key._date < min_date:
                min_date = key._date
        return min_date

    # Returns the minimum flight time 
    def get_min_time(self):
        if not self:
            return None
        min_time = None
        for item in self._table:
            key = item._key
            if min_time is None or key._time < min_time:
                min_time = key._time
        return min_time

    

# Create a FlightQuery object
a = FlightQuery()

# Create flight key-value pairs using 'for' loop
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3"), ("A", "B", 620, 1330, "No4"), ("A", "B", 630, 1400, "No5"), ("A", "B", 624, 1430, "No6")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value


                        
# Interface for inputing user queries
print("""✈︎✈︎✈︎ Welcome to GenericFlightBooking.Com! ✈︎✈︎✈︎
      
Please follow the instructions to complete your query:
    """)
    
# Accepting input from user for origin airport, destination airport, earliest date, earliest time, latest date, and latest time
origin = input("1. Enter origin airport (A, B, or C): ") or None
dest = input("2. Enter destination airport (A, B, or C): ") or None
earliest_date = input("3. Earliest Date (or press Enter for no preference): ") or str(a.get_min_date()-1)
earliest_time = input("4. Earliest Time (or press Enter for no preference): ") or str(a.get_min_time()-1)
latest_date = input("5. Latest Date (or press Enter for no preference): ") or None
latest_time = input("6. Latest Time (or press Enter for no preference): ") or None

# Converting inputs to integers
if earliest_date:
    earliest_date = int(earliest_date)
if earliest_time:
    earliest_time = int(earliest_time)
if latest_date:
    latest_date = int(latest_date)
if latest_time:
    latest_time = int(latest_time)
    
# Creating Key objects for search criteria
k1 = a.Key(origin, dest, earliest_date, earliest_time)
k2 = a.Key(origin, dest, latest_date, latest_time)

print(k1)
print(k2)
print("--- Please choose from the following flights: ---")

# Run the query and print results
results = a.query(k1, k2)
for value, key in results:
    print(f"{value} :: {key}")

# Farewell message
print("""Have a pleasant flight!""")

