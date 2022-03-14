for a in range(1, 4):
    for b in range(1, 4):
        if b != a :
            for c in range(1, 4):
                if c != a and c != b:
                    print(a, b, c)

