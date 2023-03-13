def permutations(n):

    ls = [x for x in range(1, n + 1)]
    stack = [tuple(("s", 0, 0))]

    while len(stack) != 0:
        print(stack)
        c, i, j = stack.pop()

        if c == "s":
            if i == n:
                print(ls)
            else:
                ls[i], ls[j] = ls[j], ls[i]
                stack.append(tuple(("f", i, j)))
                stack.append(tuple(("s", i + 1, i + 1)))
                
        if c == "f":
            ls[i], ls[j] = ls[j], ls[i]
            if j < n - 1:
                stack.append(tuple(("s", i, j + 1)))

n = int(input("Enter an integer: "))
permutations(n)