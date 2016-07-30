def max(x, y):
    return (x, y)[x < y]


def min(x, y):
    if x > y:
        return y
    return x


def calc_k(max, x):
    return max / x


def calc_q(k, p):
    return 0.5 * k + 0.5 * p


def calc_minimum(p):
    return (0.5 - (0.5 * p)) / 0.5


def interpolate_q(q):
    # map 1-0.5 to 1-4
    return (((q - 1) * (4 - 1)) / (0.5 - 1)) + 1


def opt1():
    try:
        x = float(input("Insert Points in main exam:\t"))
        y = float(input("Insert Points in after exam:\t"))
        z = float(input("Insert Points in projects:\t"))
    except ValueError:
        print("Error in Input. Cancelling!")
        exit()

    k = calc_k(max(x, y), 100)
    p = min(z, 100) / 100

    q = calc_q(k, p)
    grade = interpolate_q(q)

    if q >= 0.5:
        if k >= 0.5:
            print("you've pass with a grade of {0}!".format(grade))

    else:
        print("you didn't pass! Loser")


def opt2():
    try:
        x = float(input("Insert Points in your projects:\t"))
    except ValueError:
        print("Error in Input. Cancelling!")
        exit()

    p = min(x, 100) / 100

    print("you'll need a minimum {0} percentage".format(max(calc_minimum(p) * 100, 50)))


if __name__ == "__main__":
    try:
        if (int(input('Opt: \n'
                      '(1) Calculate your grade based of your points \n'
                      '(2) Calculate percentage needed to pass exam out of project points\n'
                      'Your Input: ')) == 1):
            opt1()
        else:
            opt2()
    except ValueError:
        print("Error in Input. Cancelling!")
