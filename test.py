def splitIntoTwo(arr):
    # Write your code here
    s = 0
    for i in len(arr) - 1:
        L = arr[:i+1]
        R = arr[i+1:]
        if sum(L) > sum(R):
            s += 1
    return s
if __name__ == '__main__':