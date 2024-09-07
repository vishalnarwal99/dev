from queue import Queue


def breadth_first_search(current_volumes: list[int], target_volume: int, capacities: list[int]) -> None:
    front: Queue[list[int]] = Queue()
    front.put(current_volumes)
    visited: set[list[int]] = set()

    while not front.empty():
        if current_volumes[0] < capacities[0] and ([capacities[0], current_volumes[1]] not in visited):
            front.put([capacities[0], current_volumes[1]])
            visited.add([capacities[0], current_volumes[1]])

        if current_volumes[1] < capacities[1] and ([current_volumes[0], capacities[1]] not in visited):
            front.put([current_volumes[0], capacities[1]])
            visited.add([current_volumes[0], capacities[1]])


if __name__ == '__main__':
    capacities: list[int] = []
    capacities.append(int(input('Enter jug 1 capacity: ')))
    capacities.append(int(input('Enter jug 2 capacity: ')))

    target_volume: int = int(input('Enter target volume: '))
    current_volumes = [0, 0]

    breadth_first_search(current_volumes, target_volume, capacities)

