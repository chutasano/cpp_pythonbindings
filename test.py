import test
import time

print test.greet()

test.initialize()
print "starting counter"
count = 0
while (count < 5):
  print test.get_count()
  time.sleep(2)
  count = count + 1

print "pausing count, next numbers should be same"
test.pause()
time.sleep(1)  #waiting at least 1 second to ensure the pausing is applied
print test.get_count()
time.sleep(2) #next number should be the same
print test.get_count()
print "disposing"
test.dispose()
