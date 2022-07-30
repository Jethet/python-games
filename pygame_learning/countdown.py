import time

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d} : {:02d}".format(mins, secs)
        print(timer, end = "\r")
        time.sleep(5)
        t -= 1
        
    print("Time!")

t = input("your time in seconds: ")

countdown(int(t))