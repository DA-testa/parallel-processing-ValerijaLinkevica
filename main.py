# python3

# the

# def task(id, time):

# def custom_thread(id, task_id, task_time_counter):


# def get_thread(thread_list):

# n - amount of threads
# m - amount of tasks
# data - individual task length
# def parallel_processing_new(n, m, data):
#     output = []
#     # TODO: write the function for simulating parallel tasks, 
#     # create the output pairs
#     ticks = [0] * n

#     for task in range(m):
#         free_thread = ticks.index(min(ticks))
#         # 
#         output.append((free_thread, ticks[free_thread]))
#         ticks[free_thread] += data[task]
#     return output


# def parallel_processing(n, m, data):
#     output = []
#     threads = []
#     thr = []
#     # TODO: write the function for simulating parallel tasks,
#     # create the output pairs
#     rev = []

#     for i in reversed(data):
#         rev.append(i)

#     for i in range(n):
#         thr.append(i)

#     for i in thr:
#         a = i, rev.pop() - 1
#         threads.append(a)
#         m = m - 1

#     #print(len(threads))

#     counter = 0
#     while True:

#         t = data[counter]

#         # for thread in range(len(threads)):
#         #     values = threads[thread]
#         #     if values[1] == 0:
#         #         values = (thread, rev.pop() - 1)
#         #         m = m - 1
#         #     else:
#         #         values = (thread, thread[1] - 1)

#         #     out = values, counter
#         #     output.append(out)

#         for i in threads:
#             #print(i)
            

#             if i[1] == 0:
                

#                 i = i[0], rev.pop() - 1

                
#                 m = m - 1
#             else:
#                 i = i[0], i[1] - 1

#             out = i[0], counter
#             output.append(out)

#         # print(counter)
#         counter = counter + 1

#         if m == 0:
#             for i in threads:
#                 out = i[0], counter
#                 output.append(out)
#             break

#     return output

# NOTE: Tried another method.
# Got confused.
# It does work, but I haven't figured out how to show the counter.
# Only which thread takes the task.


class CustomTask:
    def __init__(self, id, time):
        self.id = id
        self.time = time


class CustomThread:
    def __init__(self, id, task_id, timer):
        self.id = id
        self.task_id = task_id
        self.timer = timer


# declare lists
# th1 = CustomThread(0, -1, 0)
# th2 = CustomThread(1, -1, 0)
#
# tsk1 = CustomTask(0, 1)
# tsk2 = CustomTask(1, 2)
# tsk3 = CustomTask(2, 3)
# tsk4 = CustomTask(3, 4)
# tsk5 = CustomTask(4, 5)
#
# th_list = [th1, th2]
# tsk_list = [tsk1, tsk2, tsk3, tsk4, tsk5]

th_list = []
tsk_list = []


def get_thread():
    for th in th_list:
        if th.task_id == -1:
            return th
    # no thread is available
    return None


def decrease_timer():
    for th in th_list:
        if th.task_id == -1:
            continue

        th.timer = th.timer - 1
        if th.timer == 0:
            th.task_id = -1

def main():
    i = 1

    n = 0
    m = 0

    values = input().split()

    n = int(values[0])
    m = int(values[1])

    for j in range(n):
        th_list.append(CustomThread(j, -1, 0))

    data = []
    data_temp = []
    data_temp = input().split()

    order = 0
    for j in data_temp:
        data.append(int(i))
        tsk_list.append(CustomTask(order, int(j)))
        order += 1

    while len(tsk_list) > 0:
        # for x in range(
        for j in range(n):
            th_to_work = get_thread()

    #  gives a thread
            if th_to_work is not None:
                th_to_work.task_id = tsk_list[0].id
                th_to_work.timer = tsk_list[0].time
                print(str(th_to_work.id)+ " " + str(i - 1))
                tsk_list.pop(0)

        decrease_timer()

        i = i + 1



# n = threads   m = tasks to do   # data = task length
# def parallel_processing(n, m, data):
#     output = []
#     threads = []
#     reversed_data = []
#     total_len = [0, 0]

#     for element in reversed(data):
#         reversed_data.append(element)

#     for thread in range(n):
#         total_len[thread] = data[thread]
#         threads.append(reversed_data.pop())
#         m = m - 1

#     # print(threads)
#     # print(total_len)
#     a = 0
#     counter = 0
#     while True:

#         id = 0
#         for time in threads:

#             print(total_len[id])

#             if time == 1:
#                 threads[id] = reversed_data.pop()
                
#                 a = threads[id]

#                 total_len[id] = total_len[id] + a

#                 out = id, counter
#                 output.append(out)

#                 m = m - 1
                    
#             else:
#                 a = threads[id]
#                 threads[id] = time - 1

            
#             if counter == total_len[id] - a - 1:
                
#                 # print(total_len[id] - 1)
#                 out = id, counter
#                 output.append(out)

#             id = id + 1

#         counter = counter + 1

#         if m == 0:
#             id = 0

#             for i in threads:
#                 out = id, counter
#                 output.append(out)
                
#                 id = id + 1

#             break

#     return output


# def main():
#     # TODO: create input from keyboard
#     # input consists of two lines
#     # first line - n and m
#     # n - thread count
#     # m - job count
#     n = 0
#     m = 0

#     values = input().split()

#     n = int(values[0])
#     m = int(values[1])


#     # second line - data 
#     # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
#     data = []
#     # data = [1, 2, 3, 4, 5]
#     data_temp = []
#     data_temp = input().split()

#     for i in data_temp:
#         data.append(int(i))

#     # TODO: create the function
#     result = parallel_processing_new(n, m, data)

#     # TODO: print out the results, each pair in it's own line
#     for i, j in result:
#         print(i, j)



if __name__ == "__main__":
    main()
