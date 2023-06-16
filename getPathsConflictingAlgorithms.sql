SELECT *
FROM benchmarks
WHERE "Dijkstra / PriorityQueue: cost" != "Dijkstra / BucketQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "Dijkstra / ArrayQueue: cost"
    
    OR "Dijkstra / PriorityQueue: cost" != "Dijkstra-Backwards / PriorityQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "Dijkstra-Backwards / BucketQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "Dijkstra-Backwards / ArrayQueue: cost"
    
    OR "Dijkstra / PriorityQueue: cost" != "BFS / UnweightedQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "BFS-Backwards / UnweightedQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "BFS-MeetInMiddle / UnweightedQueue: cost"
    OR "Dijkstra / PriorityQueue: cost" != "BFS-MeetAtTeleport / UnweightedQueue: cost"
;