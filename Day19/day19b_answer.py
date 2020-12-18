# After investigation of progress follows it loops with an inner and an outer loop:
# 1) inner loop --> Reg[4] += 1 from 1 to 10551368 (end value > Reg[5], which is fixed at 10551367)
# 2) outer loop --> Reg[1] += 1 from 1 to 10551368 (end value > Reg[5])
# Reg[0] is only updated if 3) is true:
# 3) Reg[0] = Reg[0] + Reg[1] if Reg[1] * Reg[4] == Reg[5] (which is fixed at 10551367)

# Conclusion --> At the end Reg[0] is equal to sum of the dividers of Reg[5], which is 10551367


def divider(num):
    dividers = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            dividers.append(i)
            dividers.append(int(num / i))
    return dividers


print(divider(10551367))

print('The answer is', sum(divider(10551367)))
