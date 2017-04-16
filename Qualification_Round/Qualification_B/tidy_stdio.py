
def solve(n, case):
    m = n[0]
    number = list(m)
    length = len(number)
    if length == 1:
        output = 'Case #%d: %s' % (case, number[0])
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
    output = 'Case #%d: %d' % (case, result)
    return output

def run():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = [s for s in input().split(" ")]
        output = solve(n, i)
        print(output)

run()