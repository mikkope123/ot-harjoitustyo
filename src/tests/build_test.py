import unittest
from build import File_builder



class TestFile_builder(unittest.TestCase):

    def setUp(self):
        outputfile = "data/data.txt"
        self.builder = File_builder(outputfile)

    def test_two_coordinates(self):
        self.assertEqual(self.builder.two_coordinates([1, 2, 3]), False)
        self.assertEqual(self.builder.two_coordinates([1, 2]), True)

    def test_proper_coordinates(self):
        self.assertEqual(self.builder.proper_coordinates(["a", "b"]), False)
        self.assertEqual(self.builder.proper_coordinates([1, 2]), True)
