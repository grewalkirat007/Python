import threading
import time


def TestTimer():
    print("I am from the timer functions")


timer = threading.Timer(5.0, TestTimer)
timer.start()
timer.cancel()
print("I am at the end of the page")

m = 0
while m != 10:
    print(">> {}".format(m))
    # print(f">> {m}")
    time.sleep(5)
    m += 1
