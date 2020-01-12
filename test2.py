import unittest
import analog_temp

class TestTemp(unittest.TestCase):
      def test_temp_port0(self):
          self.assertGreaterEqual(analog_temp.mcp.read_adc(0),200)
      def test_temp_port1(self)
          self.assertGreaterEqual(analog_temp.mcp.read_adc(1),200)
           

if __name__=="__main_":
    unittest.main()
