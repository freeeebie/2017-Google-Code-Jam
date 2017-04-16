from sys import argv
import os

def open_file():
    input_argv = argv[1]
    cur_path = os.getcwd()
    input_file = cur_path + '/' + input_argv
    output_file = cur_path + '/' + input_argv + '.out'
    return input_file, output_file

def solve(n, m, case):
    m = int(m)
    length = len(n)
    flag = True
    for x in n:
        if x == '-':
            flag = False
            break
    if flag is True:
        output = 'Case #%d: %s\n' % (case, "0")
        return output

    cnt = 0
    n = list(n)
    flag = True
    result = 0

    for x in n:
        if x == '-':
            n[cnt] = '+'
            for i in range(1, m):
                if n[cnt + i] == '-':
                    n[cnt + i] = '+'
                else:
                    n[cnt + i] = '-'
            result += 1
        if (length - cnt == m):
            for y in n[cnt + 1:]:
                if y == '-':
                    flag = False
                    break
            break
        cnt += 1

    if flag is True:
        output = 'Case #%d: %d\n' % (case, result)
    else:
        output = 'Case #%d: %s\n' % (case, "IMPOSSIBLE")
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
