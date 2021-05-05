def who_are_you_and_hello():
    s = input()
    while True:
        if s.isalpha() and s[0].istitle() and s[1:].islower():
            break
        else:
            s = input()
    print(f'Привет, {s}!')