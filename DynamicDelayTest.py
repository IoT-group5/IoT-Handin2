import time
if __name__ == '__main__':
    i = 0  # Incrementer for delay calculation
    times = []  # Placeholder for logged times
    diffs = []  # Placeholder for diff between times
    start = round(time.time()*1000)  # Start time
    # Loop through 1000 times
    while i <= 1000:
        t = round(time.time()*1000)  # Get current time
        outputDelay = start+(100*i)-t  # Calculate delay
        # Only delay if delay is greater than 0
        if delay > 0:
            time.sleep(outputDelay / 1000)  # Do delay
        times.append(round(time.time()*1000))  # Log time
        print(i, outputDelay, round(time.time()*1000))  # Print iteration, delay, and current time
        i += 1  # Increment incrementer i
    # For loop for calculating diffs between logged times
    for x in range(len(times)):
        # Skipping first element
        if x > 0:
            diffs.append(times[x]-times[x-1])  # Adding diff to the diffs placeholder
    print(sum(diffs)/len(diffs))  # Print average diff between prints
