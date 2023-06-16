import requests
import json
import sqlite3

urlPrefix = "http://localhost:8080/api/"
dbFile = "./data.db"
algorithms = [ "BFS / UnweightedQueue", "BFS-Backwards / UnweightedQueue", "BFS-MeetAtTeleport / UnweightedQueue", "BFS-MeetInMiddle / UnweightedQueue", "Dijkstra / ArrayQueue", "Dijkstra / BucketQueue", "Dijkstra / PriorityQueue", "Dijkstra-Backwards / ArrayQueue", "Dijkstra-Backwards / BucketQueue", "Dijkstra-Backwards / PriorityQueue"]

def requestRandomPathForAlgorithm(startCoordinate, endCoordinate, algorithm):
    return requests.post(url=urlPrefix + "path.json",
                  json={
                      "from": startCoordinate,
                      "to": endCoordinate,
                      "blacklist": [],
                      "algorithm": algorithm
                  }).json()

def requestRandomPathAllAlgorithms(algorithms):
    randomCoordinates = requests.get(urlPrefix + "debug/randomStartEndCoordinates.json").json()
    startCoordinate = randomCoordinates["start"]
    endCoordinate = randomCoordinates["end"]

    data = {
        "start": startCoordinate,
        "end": endCoordinate
    }
    for algorithm in algorithms:
        response = requestRandomPathForAlgorithm(startCoordinate, endCoordinate, algorithm)
        data[algorithm + ": cost"] = response["totalCost"] if response["pathFound"] else -1
        data[algorithm + ": computeTimeMs"] = response["computeTimeMs"]
    
    return data

def insertDataIntoDb(dbConn, data):
    variables = (
        data["start"]["x"],
        data["start"]["y"],
        data["start"]["z"],
        data["end"]["x"],
        data["end"]["y"],
        data["end"]["z"],
        data["Dijkstra / PriorityQueue: cost"],
        data["Dijkstra / PriorityQueue: computeTimeMs"],
        data["Dijkstra / BucketQueue: cost"],
        data["Dijkstra / BucketQueue: computeTimeMs"],
        data["Dijkstra / ArrayQueue: cost"],
        data["Dijkstra / ArrayQueue: computeTimeMs"],
        data["Dijkstra-Backwards / PriorityQueue: cost"],
        data["Dijkstra-Backwards / PriorityQueue: computeTimeMs"],
        data["Dijkstra-Backwards / BucketQueue: cost"],
        data["Dijkstra-Backwards / BucketQueue: computeTimeMs"],
        data["Dijkstra-Backwards / ArrayQueue: cost"],
        data["Dijkstra-Backwards / ArrayQueue: computeTimeMs"],
        data["BFS / UnweightedQueue: cost"],
        data["BFS / UnweightedQueue: computeTimeMs"],
        data["BFS-Backwards / UnweightedQueue: cost"],
        data["BFS-Backwards / UnweightedQueue: computeTimeMs"],
        data["BFS-MeetInMiddle / UnweightedQueue: cost"],
        data["BFS-MeetInMiddle / UnweightedQueue: computeTimeMs"],
        data["BFS-MeetAtTeleport / UnweightedQueue: cost"],
        data["BFS-MeetAtTeleport / UnweightedQueue: computeTimeMs"]
    )
    dbConn.cursor().execute("INSERT INTO benchmarks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", variables)
    dbConn.commit()


def main():
    db = sqlite3.connect(dbFile)
    db.cursor().execute("DROP TABLE IF EXISTS benchmarks;")
    db.cursor().execute(open("createTable.sql").read())

    count = 0
    while True:
        count += 1
        data = requestRandomPathAllAlgorithms(algorithms)
        insertDataIntoDb(db, data)
        print(f"insert {count}")

if __name__ == "__main__":
    main()






