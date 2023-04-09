"""
Submitted on 9th April 2023

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati


Notes: 
    - Flight databases can be modeled as maps with Flight objects as keys and flight details as values. 
    - By ordering the keys lexicographically, we can efficiently find flights between cities, even with some flexibility in departure date and time. 
    - In this case, we used a sorted map implementation incorporating 'find range(k1, k2)'.

Assumptions:
    - It is necessary to implement the find range method in one of the files and the book recommends implementing the method in the SortedTable Map class, which we did.
    - The current implementation of the code excludes the lower and upper limits of searches.
    - We added more observations and values to the observations to test the robustness of the code.

"""


from SortedTableMap import *


# Defining FlightQuery class as a subclass of SortedTableMap
class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    # Define a nested Key class to be used as keys in the table
    class Key:
        # Define the slots to optimize memory usage
        __slots__ = "_origin", "_dest", "_date", "_time"
        
        # Initialize a Key object with the given values for the four attributes
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        # Define the less than operator to compare Key objects        
        def __lt__(self, other):
            # If the origin airports are different, sort by origin airport
            if self._origin != other._origin:
                return other._origin is None or (self._origin is not None and self._origin < other._origin)
            
            # If the destination airports are different, sort by destination airport
            if self._dest != other._dest:
                return other._dest is None or (self._dest is not None and self._dest < other._dest)
            
            # If the dates are different, sort by date
            if self._date != other._date:
                return other._date is None or (self._date is not None and self._date < other._date)
            
            # If the times are different and not None, sort by time
            if self._time is not None and other._time is not None:
                return self._time < other._time
            
            # If all attributes are equal, return False
            return False
        
        # Define the greater than operator to compare Key objects
        def __gt__(self, other):
            # If the origin airports are different, sort by origin airport
            if self._origin != other._origin:
                return self._origin is None or (other._origin is not None and self._origin > other._origin)
            
            # If the destination airports are different, sort by destination airport
            if self._dest != other._dest:
                return self._dest is None or (other._dest is not None and self._dest > other._dest)
            
            # If the dates are different, sort by date
            if self._date != other._date:
                return self._date is None or (other._date is not None and self._date > other._date)
            
            # If the times are different and not None, sort by time
            if self._time is not None and other._time is not None:
                return self._time > other._time
            
            # If all attributes are equal, return False
            return False
            
        
        # Define a string representation of the Key object
        def __str__(self):
            return "Origin: {0}, Destination: {1}, Date: {2}, Time: {3}".format(self._origin, self._dest, self._date, self._time)
        
    # Define a query method that finds all key-value pairs between k1 and k2 (exclusive)
    def query(self, k1, k2):
        return self.find_range(k1, k2)
    

# Create a FlightQuery object
a = FlightQuery()

# Create flight key-value pairs using 'for' loop
s = [("A", "B", 622, 1200, "Flight No1"), ("A", "B", 622, 1230, "Flight No2"), ("A", "C", 622, 1300, "Flight No3"), ("A", "B", 620, 1330, "Flight No4"), ("C", "B", 630, 1400, "Flight No5"), ("A", "B", 624, 1430, "Flight No6")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value

print(len(a))

                        
# Interface for inputing user queries
print("""✈︎✈︎✈︎ Welcome to GenericFlightBooking.Com! ✈︎✈︎✈︎
      
Please follow the instructions to complete your query:
    """)
    
origin = input("1. Enter origin airport: ") or None
dest = input("2. Enter destination airport: ") or None
earliest_date = input("3. Earliest Date (or press Enter for no preference): ") or None
earliest_time = input("4. Earliest Time (or press Enter for no preference): ") or None
latest_date = input("5. Latest Date (or press Enter for no preference): ") or None
latest_time = input("6. Latest time (or press Enter for no preference): ") or None

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

# farewell message
print("""Have a pleasant flight!""")

