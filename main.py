def input_type(a):
  try:
    int(a)
    return "Integer"
  except ValueError:
    try:
      float(a)
      return "float"
      exceptValueError
        try:
          if a=="True" or a=="False":
            return "boolean"
            else:
              return "string"
              except:
                return a