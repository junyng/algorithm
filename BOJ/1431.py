N = int(input())

serial_numbers = []

for _ in range(N):
    serial_numbers.append(input())

serial_numbers.sort(key=lambda s: (len(s), sum(list(map(int, filter(lambda n: n.isnumeric(), s)))), s))

for serial_number in serial_numbers:
    print(serial_number)
