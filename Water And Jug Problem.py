from queue import Queue


def breadth_first_search(current_volumes: tuple[int], target_volume: int, capacities: tuple[int]) -> None:
    front: Queue[tuple[int]] = Queue()
    front.put(current_volumes)
    visited: set[tuple[int]] = set()

    while not front.empty():
        if current_volumes[0] == target_volume or current_volumes[1] == target_volume:
            print('Found target volume.')
            return

        if current_volumes[0] < capacities[0] and ((capacities[0], current_volumes[1]) not in visited):
            front.put((capacities[0], current_volumes[1]))
            visited.add((capacities[0], current_volumes[1]))

        if current_volumes[1] < capacities[1] and ((current_volumes[0], capacities[1]) not in visited):
            front.put((current_volumes[0], capacities[1]))
            visited.add((current_volumes[0], capacities[1]))

        if current_volumes[0] > 0 and ((0, current_volumes[1]) not in visited):
            front.put((0, current_volumes[1]))
            visited.add((0, current_volumes[1]))

        if current_volumes[1] > 0 and ((current_volumes[0], 0) not in visited):
            front.put((current_volumes[0], 0))
            visited.add((current_volumes[0], 0))

        if current_volumes[0] > 0 and ((max(0, current_volumes[0] + current_volumes[1] - capacities[1]),
                                        min(current_volumes[0] + current_volumes[1], capacities[1])) not in visited):
            front.put((max(0, current_volumes[0] + current_volumes[1] - capacities[1]),
                       min(current_volumes[0] + current_volumes[1], capacities[1])))
            visited.add((max(0, current_volumes[0] + current_volumes[1] - capacities[1]),
                         min(current_volumes[0] + current_volumes[1], capacities[1])))
            
        if current_volumes[1] > 0 and ((min(current_volumes[0] + current_volumes[1], capacities[0]),
                                        max(0, current_volumes[0] + current_volumes[1] - capacities[0])) not in visited):
            front.put((min(current_volumes[0] + current_volumes[1], capacities[0]),
                       max(0, current_volumes[0] + current_volumes[1] - capacities[0])))
            visited.add((min(current_volumes[0] + current_volumes[1], capacities[0]),
                         max(0, current_volumes[0] + current_volumes[1] - capacities[0])))
            
    print('Target volume not found.')


if __name__ == '__main__':
    capacities: tuple[int] = (int(input('Enter jug 1 capacity: ')),)
    capacities = capacities + (int(input('Enter jug 2 capacity: ')),)

    target_volume: int = int(input('Enter target volume: '))
    current_volumes = (0, 0)

    breadth_first_search(current_volumes, target_volume, capacities)

