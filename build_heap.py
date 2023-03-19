#python
import sys


def build_heap(data, n):
    swaps = []
 
    def heapify(i):
        nonlocal swaps

        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[smallest]:
            smallest = left

        if right < n and data[right] < data[smallest]:
            smallest = right

        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append((i, smallest))
            heapify(smallest)

    for i in range(n // 2, -1, -1):
        heapify(i)

    return swaps


def main():
  
    input_method = input().strip()
    if input_method.startswith("I"):
        # Input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif input_method.startswith("F"):
        print("File path:")
        file_name = input().strip()
        file_path = "./tests/"
        if "a" not in file_name:
            with open(file_path + file_name, mode="r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        else:
            exit()
    else:
        exit()


    assert len(data) == n, "Entered length must be the same as the actual length of the array"


    swaps = build_heap(data, n)


    assert len(swaps) <= 4 * n, "The number of swaps exceeds the limit."

  
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

