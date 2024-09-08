from queue import Queue


def breadth_first_search(initial: tuple[int], target: int, capacity: tuple[int]) -> None:
    front: Queue[tuple[int]] = Queue()
    visited: set[tuple[int]] = set()

    front.put(initial)
    visited.add(initial)

    while not front.empty():
        current = front.get()

        if current[0] == target or current[1] == target:
            print('Found target volume.')
            return

        if current[0] < capacity[0] and ((capacity[0], current[1]) not in visited):
            front.put((capacity[0], current[1]))
            visited.add((capacity[0], current[1]))

        if current[1] < capacity[1] and ((current[0], capacity[1]) not in visited):
            front.put((current[0], capacity[1]))
            visited.add((current[0], capacity[1]))

        if current[0] > 0 and ((0, current[1]) not in visited):
            front.put((0, current[1]))
            visited.add((0, current[1]))

        if current[1] > 0 and ((current[0], 0) not in visited):
            front.put((current[0], 0))
            visited.add((current[0], 0))

        if current[0] > 0 and ((max(0, current[0] + current[1] - capacity[1]),
                                min(current[0] + current[1], capacity[1])) not in visited):
            front.put((max(0, current[0] + current[1] - capacity[1]),
                       min(current[0] + current[1], capacity[1])))
            visited.add((max(0, current[0] + current[1] - capacity[1]),
                         min(current[0] + current[1], capacity[1])))
            
        if current[1] > 0 and ((min(current[0] + current[1], capacity[0]),
                                max(0, current[0] + current[1] - capacity[0])) not in visited):
            front.put((min(current[0] + current[1], capacity[0]),
                       max(0, current[0] + current[1] - capacity[0])))
            visited.add((min(current[0] + current[1], capacity[0]),
                         max(0, current[0] + current[1] - capacity[0])))
            
        print(front.queue)
            
    print('Target volume not found.')


if __name__ == '__main__':
    capacity: tuple[int] = (int(input('Enter jug 1 capacity: ')),)
    capacity = capacity + (int(input('Enter jug 2 capacity: ')),)

    target: int = int(input('Enter target volume: '))
    initial = (0, 0)

    breadth_first_search(initial, target, capacity)

