# python3

def heapify(data, n, i, swaps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        swaps.append((i, largest))
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, swaps)


def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i, swaps)

    for i in range(n-1, 0, -1):
        swaps.append((0, i))
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0, swaps)

    return swaps


def main():
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4 * n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

