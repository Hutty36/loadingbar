import time

print("Hello")

x = 123
progress = 0
prev_progress = 0
print(" " + "_" * 35 + " . . . work in progress . . . " + "_" * 35 + " ")
print("\r" + "[" + " " * (100) + "]" + " 0%", end='', flush=True)
for i in range (x):
    progress = int(((i+1) / x) * 100)
    if (progress > prev_progress and progress > 0):
        print("\r" + "[" + "#" * progress + " " * (100-progress) + "]" + f" {progress}%", end='', flush=True)
    prev_progress = progress

    #content of the loop represented by time.sleep()
    time.sleep(5)
print("\n")

print("World")
