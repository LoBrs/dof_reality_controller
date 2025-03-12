import unittest
from dof_reality.serial_comm import percentage_to_value

class TestSerialComm(unittest.TestCase):
    def test_percentage_to_value(self):
        self.assertEqual(percentage_to_value(0), 512)
        self.assertEqual(percentage_to_value(100), 1024)
        self.assertEqual(percentage_to_value(-100), 0)

if __name__ == '__main__':
    unittest.main()
