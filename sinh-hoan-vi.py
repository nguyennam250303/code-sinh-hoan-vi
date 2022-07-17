def inithv(n):

    hv = [i for i in range(1, n + 1)]

    return hv


def printhv(hv):

    print("".join(map(str, hv)), end=" ")

def sinhhoanvi(n):

    hv = inithv(n)

    printhv(hv)

    result = hv[-1::-1]

    while True:

        i = n - 1

        while i > - 1 and hv[i] < hv[i - 1]:

            i -= 1

        j = i - 1

        for k in range(n - 1, j, -1):

            if hv[k] > hv[j]:

                temp = hv[k]

                hv[k] = hv[j]

                hv[j] = temp

                break

        hv = hv[:j+1] + sorted(hv[j + 1:])

        if i == 0:

            break

        printhv(hv)

sinhhoanvi(n)
