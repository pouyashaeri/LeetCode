nums = [1,1,2,2,2,2,2,3,3]
k = 2

freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

# Step 2: get keys sorted by their frequency (highest first)
# sorted(dict, key=dict.get, reverse=True) sorts keys by values
sorted_keys = sorted(freq, key=freq.get, reverse=True)

# Step 3: return first k keys
print(sorted_keys[:k])