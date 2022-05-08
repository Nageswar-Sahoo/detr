n = int(input())

ele = input()
lists = [int(i) for i in ele.split(" ")]
key = int(input())


# Write your code here
def findMinElement(lists):
    index = -1;
    start = 0
    end = n - 1
    while start <= end:
        mid = start + int((end - start) // 2)
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n

        if lists[mid] < lists[next] and lists[mid] < lists[prev]:
            return mid
        if (lists[start] < lists[end]):
            return start
        elif lists[start] < lists[mid]:
            start = mid + 1
        elif lists[mid] < lists[end]:
            end = mid - 1
    return index


def findElement(lists, start, end):
    index = -1;
    while start <= end:

        mid = start + int((end - start) / 2)
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n
        if lists[mid] == key:
            return mid

        elif lists[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return index


pivot = findMinElement(lists)

left = findElement(lists, 0, pivot - 1)
right = findElement(lists, pivot, n - 1)

if left != -1:
    print(left)
elif right != -1:
    print(right)
else:
    print(-1)
