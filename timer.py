import time

input_timer = int(input('input the number: '))

for i in range(input_timer, 0, -1 ):
    second = int(i % 60)
    print(f"00:00:{second:02}")
    time.sleep(1)

print("TIME'S UP")

