import time

print("Hello")

x = 123
progress = 0
prev_progress = 0
print(" " + "_" * 34 + " . . . work in Progress . . . " + "_" * 34 + " ")
for i in range (x):
    progress = int((i / x) * 100) - 1
    if (progress > prev_progress and progress > 0):
        print("\r" + "[" + "#" * progress + " " * (98-progress) + "]", end='', flush=True)
    prev_progress = progress

    #content of the loop represented by time.sleep()
    time.sleep(0.05)
print()

print("\nWorld")
