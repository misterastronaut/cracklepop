def cracklepop(number):
    if number % 15 == 0:
        return 'CracklePop'
    elif number % 5 == 0:
        return 'Pop'
    elif number % 3 == 0:
        return 'Crackle'
    else:
        return number


assert cracklepop(1) == 1
assert cracklepop(3) == 'Crackle'
assert cracklepop(5) == 'Pop'
assert cracklepop(15) == 'CracklePop'
assert cracklepop(41) == 41
assert cracklepop(69) == 'Crackle'
assert cracklepop(70) == 'Pop'
assert cracklepop(75) == 'CracklePop'
numbers = range(1,101)
for number in numbers:
    print cracklepop(number)