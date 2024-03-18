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


Array swap is a method of creating neighbours where two indices are chosen and part of an array set between those two indices is swapped.

### Insert swap

Array swap is a method of creating neighbours where a value and an index are taken and the given value is inserted into the array at the given place.
