import heapq

# Dijkstra's Algorithm Function
def dijkstra(graph, source_node, n):
    # Distances to all nodes from the source
    distances = [float('inf')] * (n + 1)
    distances[source_node] = 0  

    # Queue to store the nodes to be processed
    pq = [(0, source_node)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

         
        if current_distance > distances[current_node]:
            continue

        # Check neighbors (adjacent nodes)
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update the distance and add to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def find_shortest_delivery_times():
    #Input the Grid (N and M)
    n = int(input("Enter number of intersections (N): "))
    m = int(input("Enter number of roads (M): "))

    #Initialize the graph (adjacency list)
    graph = {i: [] for i in range(1, n + 1)}

    print("Enter the roads with traffic delays (start_node, end_node, delay):")
    for _ in range(m):
        start, end, delay = map(int, input().split())
        graph[start].append((end, delay))

    #Input the delivery points
    delivery_points = list(map(int, input("Enter the delivery points (space-separated): ").split()))

    #Set the warehouse as the source (Node 1)
    source_node = 1

    #Run Dijkstra’s Algorithm to find the shortest paths from the warehouse (Node 1)
    distances = dijkstra(graph, source_node, n)

    #Find the shortest path to each delivery point
    shortest_times = {}
    for point in delivery_points:
        shortest_times[point] = distances[point]  # Shortest time to delivery point

    #Output the shortest delivery times
    print("Shortest Delivery Times to Delivery Points:")
    for point, time in shortest_times.items():
        print(f"Delivery Point {point}: {time} minutes")

    shortest_point = min(shortest_times, key=shortest_times.get)
    shortest_time = shortest_times[shortest_point]

    #Print the delivery point with the shortest delivery time
    print(f"\nDelivery Point with the Shortest Time: Delivery Point {shortest_point} with {shortest_time} minutes")

find_shortest_delivery_times()
