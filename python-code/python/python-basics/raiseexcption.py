try:
  x =15
  if x>10:
      raise Exception("Num is greater than 10")
  else:
    print("doing good")
except ValueError as e:
    print("ValueError.",e)
except Exception as e:
    print("Error.",e)


