import unittest
from fileio.fileio import File_reader, Output_handler

class TestFile_reader(unittest.TestCase):
    def setUp(self):
        filename = "src/tests/testfiles/test_data.txt"
        self.reader = File_reader(filename)

    def test_read_file(self):
        self.assertEqual(len(self.reader.read_file()), 3)

class TestOutput_handler(unittest.TestCase):
    def setUp(self):
        image_file = "src/tests/testfiles/testimage.png"
        result_file = "src/tests/testfiles/testresults"
        reader = File_reader("src/tests/testfiles/test_data.txt")
        output_format = "png"
        route = reader.read_file()
        self.outputtest = Output_handler(route, image_file, result_file, output_format)

    def test_plot(self):
        self.assertEqual(self.outputtest.plot(), True)

    def test_print_to_file(self):
        self.assertEqual(self.outputtest.print_to_file(), True)
