'''
Problem:
You are simulating a digital signal sampled over time.
You are given a list of (time, value) pairs, where:
- time is an integer timestamp in nanoseconds (strictly increasing)
- value is either 0 or 1
A signal is considered stable if its value does not change for at least W nanoseconds.

Task:
Write a function that returns all time intervals during which the signal is stable for at least W nanoseconds.
Return the result as a list of (start_time, end_time) intervals.

Example
data = [
    (0, 1),
    (5, 1),
    (10, 1),
    (15, 0),
    (20, 0),
    (30, 0),
    (40, 1),
]

W = 10

Output
[(0, 10), (15, 30)]
'''

def check_stable_signal(data, W):
    start_time = data[0][0]
    current_value = data[0][1]

    result = []

    for i in range(1, len(data)):
        time, value = data[i]
        if value != current_value:
            duration = time - start_time
            if duration >= W:
                result.append((start_time, data[i - 1][0]))
            start_time = time
            current_value = value

    # Handling the end time
    end_time = data[-1][0]
    if end_time - start_time >= W:
        result.append((start_time, end_time))

    return result

data = [
    (0, 1),
    (5, 1),
    (10, 1),
    (15, 0),
    (20, 0),
    (30, 0),
    (40, 1),
]

W = 10

print(check_stable_signal(data, W))