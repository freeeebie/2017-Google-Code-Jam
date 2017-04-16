import heapq

def solve(n, m, case):
    n = int(n)
    m = int(m)
    if n == m:
        output = 'Case #%d: %d %d' % (case, 0, 0)
        return output

    start = 0
    end = n - 1

    q = []
    heapq.heappush(q, (-(end - start), (start, end)))  # uses max heap, So uses negative values
    y1 = 0
    z1 = 0

    for i in range(0, m):
        if len(q) == 0:
            y1 = 0
            z1 = 0
            break

        (distance, (start, end)) = heapq.heappop(q)

        if end - start <= 0:
            y1 = 0
            z1 = 0
            continue

        middle = start + int((end - start) / 2)
        y1 = end - middle
        z1 = middle - start
        heapq.heappush(q, (-(middle - 1 - start), (start, middle - 1)))
        heapq.heappush(q, (-(end - (middle + 1)), (middle + 1, end)))

    if y1 > z1:
        output = 'Case #%d: %d %d' % (case, y1, z1)
    else:
        output = 'Case #%d: %d %d' % (case, z1, y1)
    return output

def run():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, m = [s for s in input().split(" ")]
        output = solve(n, m, i)
        print(output)

run()