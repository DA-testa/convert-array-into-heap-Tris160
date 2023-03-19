# python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)

    return swaps


def sift_down(i, data, swaps):
    n = len(data)
    min_idx = i

    l = 2*i + 1
    if l < n and data[l] < data[min_idx]:
        min_idx = l

    r = 2*i + 2
    if r < n and data[r] < data[min_idx]:
        min_idx = r

    if i != min_idx:
        swaps.append((i, min_idx))
        data[i], data[min_idx] = data[min_idx], data[i]
        sift_down(min_idx, data, swaps)


def main():
    n, c = input().split()
    n = int(n)
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == '__main__':
    main()
