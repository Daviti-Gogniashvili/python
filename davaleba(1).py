def extractor(x):
  edited_str = ""
  if type(x) == list:
    for ext in x:
      for string in ext:
        edited_str += string
  else:
    for string in x:
      edited_str += string
  return edited_str

def length(x):
  if len(x) < 6:
    print("please reenter with valid length - (6+)")


def nums(x):
  count = 0
  for ext in x:
    if ext.isdigit():
      count += 1
  if count < 2:
    print("please enter at least 2 nums")


def upper(x):
  count = 0
  for ext in x:
    if ext.isupper():
      count += 1
  if count < 1:
    print("please enter at least 1 uppercase letter")


def symbols(x):
  for sym in "~!@#$%^&*()_-+=}{|[]\?/:;'<>,.":
    if sym in x:
      print("please enter only letters and numbers")

def main():
  raw = "WycuuDn44y"
  length(extractor(raw))
  nums(extractor(raw))
  upper(extractor(raw))
  symbols(extractor(raw))
main()
