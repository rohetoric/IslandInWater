import sys
import os

class IslandsInWater():
  def __init__(self, file_name,island_matrix=[]):
    self.file_name = file_name
    self.island_matrix = []

  def read_from_file(self):
    with open(self.file_name, 'r') as f:
      data = f.readlines() # reading into matrix
    for raw_line in data:
      split_line = raw_line.strip().split(" ")
      nums_ls = [int(x) for x in split_line] #string conversion to integer
      self.island_matrix.append(nums_ls)

    
def main(args):
  filename = args[0]
  islandsinwater = IslandsInWater(filename)
  islandsinwater.read_from_file()

  #write the code to count number of islands now..


if __name__ == '__main__':
  main(sys.argv[1:])