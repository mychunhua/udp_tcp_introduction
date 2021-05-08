import time

def task1():
    for i in range(6):
        print("___task1___")
        time.sleep(1)

def task2():
    for i in range(6):
        print("___task2___")
        time.sleep(1)

def main():
    task1()
    task2()


if __name__ == "__main__":
    main()