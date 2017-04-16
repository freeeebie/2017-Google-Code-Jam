from sys import argv
import os

def open_file():
    input_argv = argv[1]
    input_file = cur_path + '/' + input_argv
    output_file = cur_path + '/' + input_argv + '.out'
    return input_file, output_file

def solve(n, case):
    m = n[0]
    number = list(m)
    length = len(number)
    if length == 1:
        output = 'Case #%d: %s\n' % (case, number[0])
        return output
    cnt = 0
    old = -1
    for i in number:
        if cnt == 0:
            cnt += 1
            old = int(i)
            continue

        if int(i) < old:
            for k in range(cnt, length):
                number[k] = '9'
            for k in range(cnt - 1, -1, -1):
                if k == 0 or number[k - 1] < number[k]:
                    number[k] = str(int(number[k]) - 1)
                    break;
                number[k] = '9'
        old = int(i)
        cnt += 1
    result = "".join(number)
    result = int(result)
    output = 'Case #%d: %d\n' % (case, result)
    return output

def run(file_in, file_out):
    with open(file_in, 'r') as fin, open(file_out, 'w') as fout:
        lines = fin.read().splitlines()
        cnt = 0
        t = int(lines[cnt])  # read a line with a single integer
        cnt += 1
        for i in range(1, t + 1):
            l = lines[i]
            n = [s for s in l.split(" ")]
            output = solve(n, i)
            fout.write(output)

input_file, output_file = open_file()
run(input_file, output_file)


