import sys
import os

class IslandsInWater():
  def __init__(self, file_name:str,island_matrix:list=[]):
    self.file_name = file_name
    self.island_matrix = []

  def read_from_file(self) -> None:
    with open(self.file_name, 'r') as f:
      data = f.readlines() # reading into matrix
    for raw_line in data:
      split_line = raw_line.strip().split(" ")
      nums_ls = [int(x) for x in split_line] #string conversion to integer
      self.island_matrix.append(nums_ls)

  def _dfs(self, row, col):
    self.island_matrix[row][col] = 0 #flipping 1 to 0 to see we have traversed the position
    bounding_conditions = [(row-1,col), (row+1,col), (row, col-1), 
                           (row,col+1), (row-1,col-1), (row-1,col+1),
                           (row+1,col+1), (row+1, col-1)]
    for bounding_row, bounding_col in bounding_conditions:
      if bounding_row >= 0 and bounding_col >= 0 and bounding_row <= len(self.island_matrix) and bounding_col <= len(self.island_matrix[row]) and self.island_matrix[bounding_row][bounding_col] == 1:
        print(f"We are in position :: {bounding_row} | {bounding_col}")
        self._dfs(bounding_row, bounding_col)
    
  def count_number_of_islands(self) -> int:
    num_of_islands = 0
    for row in range(len(self.island_matrix)):
      for col in range(len(self.island_matrix[row])):
        if self.island_matrix[row][col] == 1:
          num_of_islands = num_of_islands + 1
          self._dfs(row, col)
    return num_of_islands 
  
def main(args):
  if args is None:
    filename = "islands.txt"
  else:
    filename = args[0]
  islandsinwater = IslandsInWater(filename)
  islandsinwater.read_from_file()
  num_of_islands = islandsinwater.count_number_of_islands()
  print(num_of_islands)

if __name__ == '__main__':
  main(sys.argv[1:])