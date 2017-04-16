from sys import argv
import os
import heapq

def open_file():
    input_argv = argv[1]
    cur_path = os.getcwd()
    input_file = cur_path + '/' + input_argv
    output_file = cur_path + '/' + input_argv + '.out'
    return input_file, output_file

def solve(n, m, case):
    n = int(n)
    m = int(m)
    if n == m:
        output = 'Case #%d: %d %d\n' % (case, 0, 0)
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
        output = 'Case #%d: %d %d\n' % (case, y1, z1)
    else:
        output = 'Case #%d: %d %d\n' % (case, z1, y1)
    return output
def run(file_in, file_out):
    with open(file_in, 'r') as fin, open(file_out, 'w') as fout:
        lines = fin.read().splitlines()
        cnt = 0
        t = int(lines[cnt])  # read a line with a single integer
        cnt += 1
        for i in range(1, t + 1):
            l = lines[i]
            n, m = [s for s in l.split(" ")]
            output = solve(n, m, i)
            fout.write(output)

input_file, output_file = open_file()
run(input_file, output_file)


