SELECT
    AVG("Dijkstra / ArrayQueue: cost") AS "AVG(cost)",
    AVG("Dijkstra / PriorityQueue: computeTimeMs"),
    AVG("Dijkstra / BucketQueue: computeTimeMs"),
    AVG("Dijkstra / ArrayQueue: computeTimeMs"),
    AVG("Dijkstra-Backwards / PriorityQueue: computeTimeMs"),
    AVG("Dijkstra-Backwards / BucketQueue: computeTimeMs"),
    AVG("Dijkstra-Backwards / ArrayQueue: computeTimeMs"),
    AVG("BFS / UnweightedQueue: computeTimeMs"),
    AVG("BFS-Backwards / UnweightedQueue: computeTimeMs"),
    AVG("BFS-MeetInMiddle / UnweightedQueue: computeTimeMs"),
    AVG("BFS-MeetAtTeleport / UnweightedQueue: computeTimeMs")
FROM benchmarks;