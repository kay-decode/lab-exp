num = int(input('enter the value :'))

while True:
    rev = int(str(num)[::-1])
    total = num + rev
    print(f"{num}+{rev}={total}")
    if (str(total)==str(total)[::-1]):
        print(f"the given number palindrom is :{total} ")
        break
    else:
        num = total

c = 12+45j
print(type(c))


