'''
Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
For the multiples of seven (7, 14, 21, etc.) print "Monkey".
For numbers which are multiples of both five and seven print "ChickenMonkey".
To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.
'''

nums_from_1_to_100 = range(1,101,1)
for num in nums_from_1_to_100:
  if num%5 == 0:
    if num%7 ==0:
          print(f'{num}: Chicken Monkey!!!')
    print(f'{num}: Chicken')
  elif num%7 == 0:
      print(f'{num}: Monkey')
  else: print(num)