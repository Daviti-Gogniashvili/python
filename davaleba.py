def check(array):
  raw = open("samples.txt", "w")

  for dg in array:
    try:
      if dg.isdigit():
        writefile = raw.write(dg)
    except AttributeError:
      check(str(dg))
  raw.close()

def main():
  multi_dimensional_array = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]
  raw_list = [multi_dimensional_array]
  check(raw_list)
  new_list = []
  raw_file = open("samples.txt", "r")
  readfile = raw_file.read()
  for i in readfile:
      new_list.append(int(i))
  print(new_list)

main()