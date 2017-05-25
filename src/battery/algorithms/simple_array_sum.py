import sys

size = int(raw_input().strip())
numbers = map(int, raw_input().strip().split(' '))

if len(numbers) != size:
    print 'error!'

print sum(numbers)