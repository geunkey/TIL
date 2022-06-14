from unittest import result


s = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A','B', 'O', 'B', 'AB']

A = s.count('A')
B = s.count('B')
O = s.count('O')
AB = s.count('AB')

result = {'A' : A, 'B' : B, 'O' : O, 'AB' : AB}

print(result)