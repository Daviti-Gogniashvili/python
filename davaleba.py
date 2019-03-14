def check(array, new_list):
  for i in array:
        if type(i) == int:
          new_list.append(i)
        else:
          check(i, new_list)

    

def main():
  multi_dimensional_array = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]
  new_list = []
  check(multi_dimensional_array,new_list)
  print(new_list)

if __name__ == "__main__":
  main()
