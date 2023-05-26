import threading
dataa = []

def main():
    for a in range(8):
        dataa.append("<1>")

def run():
    global counter
    counter += 1
    if counter < 200:
        threading.Timer(1, run).start()
    main()

counter = 0
run()

