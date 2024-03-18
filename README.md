# Tabu Search

The repository contains code implementing tabu search - a metaheuristic for solving optimisation problems. If you would like to expand your knowledge of the theory of tabu search, follow these links:
* https://en.wikipedia.org/wiki/Tabu_search
* https://www.baeldung.com/cs/tabu-search
* https://www.researchgate.net/publication/242527226_Tabu_Search_A_Tutorial

## Code overview

Repo contains two separate files. Each corresponds to two different problems:
* [traveling salesman problem](taboo_for_cities.py)
* [task scheduling problem](taboo_for_tasks.py)


The above code could and should only be modified when it comes to calculating some kind of value function (according to the given problem).


## Methods for finding neighbours

In the given code one can choose between three given neighbour finding methods:
* normal swap
* array swap
* insert swap

#### Normal swap


Normal swap is a method of creating neighbours in which two values in an array are selected and their places swapped.

#### Array swap

Array swap is a method of creating neighbours where two indexes are chosen and part of an array set between those two indices is swapped.

#### Insert swap

Array swap is a method of creating neighbours where a value and an index are taken and the given value is inserted into the array at the given place.

## Data input 

It should be taken into account that the data entered into the algortym should initially look like this:

![image](https://github.com/Wojsm2000/TabooSearch/assets/95697097/224a5c21-0804-4a40-ab2e-da6263223967)

when it comes to traveling salesman problem and :

![image](https://github.com/Wojsm2000/TabooSearch/assets/95697097/bcc09327-2f69-413e-bafd-f3982ca19dc5)

when it comes to task scheduling problem.



As can be seen in Figure 1, column A and row 1 are filled with the city numbers. The rest of the data are the distances between the cities.
In Figure 2, column A is filled with task numbers. Row 1 is filled with machine numbers. Each cell indicates how quickly a particular task number can be performed by a particular machine.
The algorithm has to be adapted if someone wants to use the data preprocessed diffrently.
