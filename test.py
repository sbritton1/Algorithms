from code.classes.statespace import Statespace

def test(*arg):
    print(f"{len(arg)} arguments for {arg}")

if __name__ == "__main__":
    test()

    test(1, 2, 3)

    test(1, 2.0, 3)

    test("hi", 1)

    ss = Statespace(True, 2, 0, 1, 0, 1)

    print(ss.ranges)