import unittest
import island_in_water as script
from island_in_water import IslandsInWater as island_class
from unittest.mock import MagicMock

class TestIslandInWater(unittest.TestCase):
  
 
  def test_main(self):
    context = island_class("test_file_islands.txt")
    context.read_from_file()
    self.assertEqual(context.island_matrix, [[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]])
    result = script.main(["test_file_islands.txt"])
    self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()
