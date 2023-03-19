# python3

def sift_down(i, n, data):
    max_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[max_index]:
        max_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[max_index]:
        max_index = r
    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(max_index, n, data)

def build_heap(data):
    n = len(data)
    for i in range(n // 2, -1, -1):
        sift_down(i, n, data)
    return data

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    global swaps
    swaps = []
    build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
