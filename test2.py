import unittest
import analog_temp

class TestTemp(unittest.TestCase):
      def test_temp(self):
          self.assertGreaterEqual(analog_temp.mcp.read_adc(0),200)
      self.assertGreaterEqual(analog_temp.mcp.read_adc(1),200)
           

if __name__=="__main_":
    unittest.main()
