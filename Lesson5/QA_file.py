def f():
    print("Log message!")
    return [1,2,3]


def generator():
    for i in range(0, 100):
        yield i
