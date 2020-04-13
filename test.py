from threading import Timer


def t ():
    print("Hello World")

x = Timer(5, t)
x.start()

y = Timer(5, lambda: print("Hello Universe"); print("egg"))
y.start()




