import unittest
import analog_temp

class TestTemp(unittest.TestCase):
      def test_temp(self):
          self.assertEqual(analog_temp.readadc(0))
          self.assertEqual(analog_temp.readadc(1))
          self.assertEqual(analog_temp.readadc(2))  

if __name__=="__main__":
    unittest.main()
