import unittest
import read_data

class TestReadData(unittest.TestCase):
    def setUp(self):
        self.data = read_data.read_data("../Experimental Data/Trial 21.dat")

    def test_read_data_works(self):
        print(repr(self.data.events[0].event))
        print(repr(self.data.events[1].event))

    # def test_data_valid(self):
    #     self.reader.read()
    #     data = self.reader.get_data()
        # TODO: validate received data

if __name__ == '__main__':
    unittest.main()
