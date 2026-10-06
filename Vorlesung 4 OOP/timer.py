import time

# decorator timer
def timer(func):
    def wrapper(args, *kwargs):
        before = time.time()
        func(args, *kwargs)
        time_gone = time.time() - before
        print(f"Zeit für Funktion {func}: {time_gone:.1f}s")
    return wrapper

@timer # Gleichbedeutend wie f = time(f)
def f(text):
    time.sleep(5)
    print(text)

f("Hallo")