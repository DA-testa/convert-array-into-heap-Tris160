# python3

def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[min_index]:
        min_index = left

    if right < n and data[right] < data[min_index]:
        min_index = right

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))

    swaps = build_heap(data)

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])


if __name__ == '__main__':
    main()
