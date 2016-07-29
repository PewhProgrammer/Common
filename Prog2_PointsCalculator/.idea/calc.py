def max(x,y):
    if x > y :
        return x
    return y

def min(x,y):
    if x > y :
        return y
    return x

def calcK(max,x):
    return max / x

def calcQ(k,p):
    return 0.5 * k + 0.5 * p

def calcMinimum(p):
    return (0.5 - (0.5*p)) / 0.5

def no():
    x = float(input("Insert Points in main exam: \n"))
    y = float(input("Insert Points in after exam: \n"))
    z = float(input("Insert Points in projects: \n"))

    k = calcK(max(x,y),100)
    p = min(z,100) / 100

    q = calcQ(k,p)
    if q >= 0.5:
        if k >= 0.5:
            print("Sie haben bestanden!")
    else:
        print("Sie haben nicht bestanden! Loser")

def yes():
    x = float(input("Insert Points in your projects: \n"))
    p = min(x,100) / 100

    print("Sie brauchen {} Prozent".format(max(calcMinimum(p) * 100,50)))



if(input('Would you like to know how much points '
         'you need in the exam to pass ?') == 'no'):
    no()
else:
    yes()


