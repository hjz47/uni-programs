def main(n):
    ls = [x for x in range(1, n + 1)]
    helper(ls, 0)

def helper(ls, i):
    if i == len(ls):
        print(ls)
    j = i
    while j < len(ls):
        print(j, i)
        ls[i], ls[j] = ls[j], ls[i]
        helper(ls, i + 1)
        ls[i], ls[j] = ls[j], ls[i]
        j += 1

n = int(input("Enter a number: "))
main(n)