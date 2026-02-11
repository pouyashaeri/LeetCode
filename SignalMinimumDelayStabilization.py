'''
Problem: Minimum Delay Stabilization
You are simulating a digital signal that propagates through a chain of components.

You are given:
- A list of (time, value) samples of the input signal
- A propagation delay D (in nanoseconds)
- A stabilization window W (in nanoseconds)

Each time the input signal changes value, the output signal will reflect that change after exactly D nanoseconds.
However, the output signal is considered valid only if it stays constant for at least W nanoseconds after the propagation delay.

Task
Write a function that returns all time intervals where the output signal is valid.
Return intervals as (start_time, end_time).

Example
input_signal = [
    (0, 0),
    (5, 1),
    (12, 0),
    (30, 1),
    (60, 1),
]

D = 10
W = 15

Explanation:
Change at t=5 → output flips at t=15
Next change at t=12 → output flips at t=22
→ duration = 7 ns (too short)
Change at t=30 → output flips at t=40
No change afterward until end → stays stable ≥ 15 ns

Output:
[(40, 55)]
'''

def min_delay_stabilization(data, D, W):
    if not data or len(data) < 2:
        return []

    # Step 1: Build potential output transitions
    transitions = []
    previous_value = data[0][1]

    for i in range(1, len(data)):
        time = data[i][0]
        value = data[i][1]

        if value != previous_value:
            transitions.append((time + D, value))
            previous_value = value

    result = []
    i = 0

    # Step 2: Sequential glitch filtering
    while i < len(transitions):
        current_time = transitions[i][0]

        # If this is the last transition → it survives
        if i == len(transitions) - 1:
            result.append((current_time, current_time + W))
            break

        next_time = transitions[i + 1][0]
        duration = next_time - current_time

        if duration >= W:
            # Valid stable region
            result.append((current_time, current_time + W))
            i += 1
        else:
            # Glitch -> collapse this pulse
            i += 2

    return result





input_signal = [
    (0, 0),
    (5, 1),
    (12, 0),
    (30, 1),
    (60, 1),
]

D = 10
W = 15

print(min_delay_stabilization(input_signal, D, W))