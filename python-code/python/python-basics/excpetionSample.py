try:
  x = float("hello")
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")

  