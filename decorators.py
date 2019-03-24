def noun_counter(func):
  def wrapper(checked):
    if func(checked) != None:
      for i in 'aeiouyAEIOUY':
        if func(checked).count(i) >= 1:
          counted = func(checked).count(i)
          print('{}: {}'.format(i, counted))
  return wrapper

def censorer(func):
  def wrapper(string_output):
    censorship = ["I Hate Python"]
    for i in censorship:
      if string_output.count(i) >= 1:
        print("words or sentences such is/are '{}' is/are forbiden!".format(i))
        break
      else:
        return string_output

  return wrapper



@noun_counter
@censorer
def string(string_output):
  return string_output

string("I Love Python")
