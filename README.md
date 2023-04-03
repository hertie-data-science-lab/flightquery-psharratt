# FlightQuery

There are several Web sites on the Internet that allow users to perform queries on flight databases. 

* To make a query, a user specifies origin and destination cities, a departure data, and a departure time.
* We can model such a database as a map, where keys are Flight Objects that contain fields corresponding to these 4 parameters.
* Additional information about a flight, such as the flight number, the number of seats still available in first (F) and coach (Y) class, the flight duration, and the fare, can be stored in the value object.

Finding a requested flight is not simply a matter of finding an exact match for a requested query. 

Although a user typically wants to exactly match the origin and destination cities, he or she may have flexibility for the departure date,
and certainly will have some flexibility for the departure time on a specific day.
We can handle such a query by ordering our keys lexicographically. Then, an efficient implementation for a sorted map would be a good way to satisfy users’
queries.

Complete the FlightQuery class to implement the SortedTableMap interface and to return a requested flight within a flexible departure date.
