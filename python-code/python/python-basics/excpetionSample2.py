try:
  x = float(5.6)
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")
else:
  print("everythign is good")
  