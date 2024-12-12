file = open('test.txt', 'r')
f = file.readlines()
file.close()

safe_count = 0
unsafe_count = 0

for line in f:
    # print(line)
    report = line.split(' ')
    report[-1] = report[-1].replace('\n', ' ')
    report = list(map(int, report))

    start_value = report[0] - report[1]

    match start_value:
        case value if value > 0 and value <= 3:
            for i in range(len(report)-1):
                if report[i] - report[i + 1] > 3 or report[i] - report[i + 1] < 1:
                    unsafe_count += 1
                    break
            else:
                safe_count += 1
            
        case value if value < 0 and value >= -3:
            for i in range(len(report) - 1):
                if report[i] - report[i + 1] < -3 or report[i] - report[i + 1] > -1:
                    unsafe_count += 1
                    break
            else:
                safe_count += 1

        case _:
            unsafe_count += 1

print(safe_count)