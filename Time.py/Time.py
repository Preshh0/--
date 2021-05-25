# Program checks if the number is positive or negative
# And displays an appropriate message
import time
time.time()
seconds = time.time()
local_time = time.ctime(seconds)
print ("Local time:", local_time)
morning = "00:00:00"
afternoon = "12:00:00"
evening = "16:00:00"
night = "21:00:00"
if local_time < morning:
    print("Good afternoon.")
elif local_time > morning and afternoon :
    print("Good evening.")
elif local_time > evening:
    print("Good night.")
else :
    print("Good morning.")
    
    
#num = 3
#if num == 0:
#  print("Zero")
#elif num > 0:
  #print("Positive Number")
#else:
#  print ("Negative number")
  