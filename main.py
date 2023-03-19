# python3


def parallel_processing(n, m, data):
    output = []
    threads = []
    thr = []
    # TODO: write the function for simulating parallel tasks,
    # create the output pairs
    rev = []

    for i in reversed(data):
        rev.append(i)

    for i in range(n):
        thr.append(i)

    for i in thr:
        a = i, rev.pop() - 1
        threads.append(a)
        m = m - 1

    counter = 0
    while True:

        for i in threads:
            if i[1] == 0:
                out = i[0], counter
                output.append(out)

                i = i[0], rev.pop() - 1
                
                m = m - 1
            else:
                i = i[0], i[1] - 1

        # print(counter)
        counter = counter + 1

        if m == 0:
            for i in threads:
                out = i[0], counter
                output.append(out)
            break

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count
    # m - job count
    n = 0
    m = 0

    values = input().split()

    n = int(values[0])
    m = int(values[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data_temp = []
    data_temp = input().split()

    for i in data_temp:
        data.append(int(i))

    length = len(data)

    # TODO: create the function
    result = parallel_processing(n, m, data)

    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
