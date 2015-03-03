import sys

lower = 1

print "User supplied {} arguments at run time".format(len(sys.argv))

if len(sys.argv) == 1: #array
  my_input = raw_input("Enter something, yo!")
else: 
  my_input = sys.argv[1]
n = int(my_input)

for i in xrange(lower,n):
  try:
    if i % 15 == 0:
      print "fizz buzz"
    elif i % 3 == 0:
      print "fizz"
    elif i % 5 == 0:
      print "buzz"
    else:
      print i
  except ValueError: 
	  print ("Need to supply numeric inputs")