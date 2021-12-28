def dirReduc(arr):
    arr.append(None)
    x = arr.count(None)
    while x>0:
        for i in range(0, len(arr)-1):
            if arr[i] == "EAST" and arr[i + 1] == "WEST" or arr[i] == "WEST" and arr[i + 1] == "EAST":
                arr[i + 1] = None
                arr[i] = None
            elif arr[i] == "SOUTH" and arr[i + 1] == "NORTH" or arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
                arr[i + 1] = None
                arr[i] = None
        x = arr.count(None)
        res = [i for i in arr if i]
        arr = res
    return arr