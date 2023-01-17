import time


def count():
    print("one")
    time.sleep(1)
    print("two")


def main():
    for i in range(3):
        count()


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"End in {elapsed:0.2f} sec")
