
import threading,time

dataa=[]
def main():
    # time.asctime() prints the current date & time in string.
    dataa.append("<1>")
    print(dataa)
def run():
    # created a global variable.
    global counter
    counter += 1
    # stop after 5 executions
    if counter < 100:
        # where 5 is the number of seconds to wait
        threading.Timer(1, run).start()
    # running the main function
    main()
counter = 0

run()

