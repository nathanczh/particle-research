import unittest
import read_data

class TestReadData(unittest.TestCase):
    def setUp(self):
        self.reader = read_data.DrsoscReader("../Experimental Data/Trial 21.dat")

    def test_read_data_works(self):
        self.reader.read()
        print(repr(self.reader.channels))

    def test_data_valid(self):
        self.reader.read()
        data = self.reader.get_data()
        # TODO: validate received data

if __name__ == '__main__':
    unittest.main()
