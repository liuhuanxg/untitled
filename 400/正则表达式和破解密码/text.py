def out(n):
    q = list(range(1, n + 1))
    c = 1
    while len(q) != 1:
        t = []
        for i in q:
            if c != 3:
                t.append(i)
            c += 1
            if c > 3:
                c -= 3
        q = t
    return q[0]

def main():
    n = input('Enter a number: ')
    try:
        n = int(n)
    except Exception as e:
        print('Invalid input.')
        return
    print('The last one is:', out(n))


if __name__ == '__main__':
    main()


