# ============================================================
# QUESTION:
#
# You are given a list of sensor measurements sampled at
# irregular time intervals. Each measurement is a tuple:
#     (timestamp, value)
#
# Given a fixed time window W (in seconds), compute a
# time-window moving average for each timestamp.
#
# For each time t, average all values whose timestamps fall
# within the interval [t - W, t].
#
# If no samples fall in the window, return None for that time.
#
# Example:
# data = [
#     (0, 10.0),
#     (3, 12.0),
#     (8, 14.0),
#     (15, 16.0),
#     (20, 18.0),
# ]
# W = 10
#
# Output:
# [
#     (0, 10.0),
#     (3, 11.0),
#     (8, 12.0),
#     (15, 15.0),
#     (20, 17.0),
# ]
# ============================================================

from collections import deque

def moving_average_time_window(data, W):
    window = deque()
    window_sum = 0.0
    result = []

    for i in range(len(data)):
        current_time = data[i][0]
        current_value = data[i][1]

        while window and current_time - window[0][0] > W:
            oldest_point = window.popleft()
            oldest_value = oldest_point[1]
            window_sum -= oldest_value

        window.append((current_time, current_value))
        window_sum += current_value

        result.append((current_time, window_sum/len(window)))

    return result


data = [
            (0, 10.0),
            (3, 12.0),
            (8, 14.0),
            (15, 16.0),
            (20, 18.0),
        ]

W = 10

print(moving_average_time_window(data, W))