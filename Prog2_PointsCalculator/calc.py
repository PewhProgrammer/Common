def max(x, y):
    return (x,y)[x < y]


def min(x, y):
    if x > y:
        return y
    return x


def calcK(max, x):
    return max / x


def calcQ(k, p):
    return 0.5 * k + 0.5 * p


def calcMinimum(p):
    return (0.5 - (0.5 * p)) / 0.5

def interpolate_q(q):
    #map 1-0.5 to 1-4
    return (((q - 1) * (4 - 1)) / (0.5 - 1)) + 1


def Opt1():
    x = float(input("Insert Points in main exam:\t"))
    y = float(input("Insert Points in after exam:\t"))
    z = float(input("Insert Points in projects:\t"))

    k = calcK(max(x, y), 100)
    p = min(z, 100) / 100

    q = calcQ(k, p)
    grade = interpolate_q(q)
    if q >= 0.5:
        if k >= 0.5:
            print("you've pass with a grade of {0}!".format(grade))
    else:
        print("you didn't pass! Loser")


def Opt2():
    x = float(input("Insert Points in your projects:\t"))
    p = min(x, 100) / 100

    print("you'll need a minimum {0} percentage".format(max(calcMinimum(p) * 100, 50)))


if __name__ == "__main__":
    if (int(input('Opt: \n'
              '(1) Calculate your grade based of your points \n'
              '(2) Calculate percentage needed to pass exam out of project points\n'
              'Your Input: ')) == 1):
        Opt1()
    else:
        Opt2()
