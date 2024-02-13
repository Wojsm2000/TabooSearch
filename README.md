# Tabu Search
Repository contains code which implements tabu search - metaheuristics for solving optimization problems. 
If one would like to extend one's knowledge about theory of tabu search follow these links:
* https://en.wikipedia.org/wiki/Tabu_search
* https://www.baeldung.com/cs/tabu-search
* https://www.researchgate.net/publication/242527226_Tabu_Search_A_Tutorial

## Code overview
Repo contains two separte files. Each coresponds to two diffrent problems: 
* [traveling salesman problem](taboo_for_cities.py)
* [task scheduling problem](taboo_for_tasks.py)

Above code could and should be modified only where it comes to calculation of some sort value function (according to given problem).

## Neighbours finding methods

In given code one can choose between three given finding neighbour's methods:
* normal swap
* array swap
* insert swap

#### Normal swap


