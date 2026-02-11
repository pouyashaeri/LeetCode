'''
Problem: Signal Glitch Detection
You are analyzing a digital signal over time.
You are given a list of (time, value) pairs where:
- time is in nanoseconds (strictly increasing)
- value is either 0 or 1

A glitch is defined as:
A short pulse where the signal flips to a different value and returns back within G nanoseconds.

Task
Write a function that returns all glitch intervals as (start_time, end_time).

Example
data = [
    (0, 0),
    (5, 1),
    (8, 0),
    (20, 1),
    (35, 0),
]

G = 10

Output
[(5, 8)]
'''

def glitch_detection(data, G):
    glitches = []

    for i in range(1, len(data) - 1):
        prev_time, prev_value = data[i - 1]
        curr_time, curr_value = data[i]
        next_time, next_value = data[i + 1]
        if prev_value != curr_value and prev_value == next_value:
            if next_time - curr_time <= G:
                glitches.append((curr_time, next_time))

    return glitches

data = [
    (0, 0),
    (5, 1),
    (8, 0),
    (20, 1),
    (35, 0),
]

G = 10

print(glitch_detection(data, G))