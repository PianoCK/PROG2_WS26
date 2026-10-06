import timer


# decorator
def f1(func):
    def wrapper(args, *kwargs):
        print("--Start--")
        func(args, *kwargs)
        print("--Stop--")
    return wrapper

@f1 # Gleichbedeutend wie f = f1(f)
def f(text):
    print(text)

f("Hallo")