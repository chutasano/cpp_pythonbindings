#!/usr/bin/env python


import test_cpp
import time

print test_cpp.greet()

test_cpp.initialize()
print "starting counter"
count = 0
while (count < 5):
  print test_cpp.get_count()
  time.sleep(2)
  count = count + 1

print "pausing count, next numbers should be same"
test_cpp.pause()
time.sleep(1)  #waiting at least 1 second to ensure the pausing is applied
print test_cpp.get_count()
time.sleep(2) #next number should be the same
print test_cpp.get_count()
print "disposing"
test_cpp.dispose()
