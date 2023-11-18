result = []
def divider(a, b):
  try:
    if a < b:
      try:
        return a
      except ValueError:
        print(ValueError)
        raise a
    if b > 100:
      raise IndexError
    try:
      return a/b
    except ZeroDivisionError:
      print(ZeroDivisionError)
      return a+b
  except TypeError:
    print(TypeError)
    return b
data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8 : 4}
for key in data:
  res = divider(key, data[key])
  result.append(res)
  print(result)