for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = [x for x in range(1,n+1)]
    i = 0
    cnt = 0
    while i <= n and cnt < n - k:
        arr[i] = -1 * arr[i]
        i += 2
        cnt += 1
    i = n-1
    while cnt < n - k and i >= 0:
        if arr[i] > 0:
            arr[i] *= -1
            cnt += 1
        i -= 1
    print(*arr)