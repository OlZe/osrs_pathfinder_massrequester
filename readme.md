# OSRS Pathfinder Mass Requester

This is a python script designed to perform random pathfinding requests on the [OSRS Pathfinder Project](https://github.com/OlZe/osrs_pathfinder) to compare the performance of each algorithm.

For each iteration it retrieves one pair of random coordinates and requests the same path once for each algorithm. The results are saved in `data.db` using sqlite. The table `benchmarks` contains the following data:

- Start/end coordinate
- For each algorithm:
    - The returned total path cost
    - Computation time