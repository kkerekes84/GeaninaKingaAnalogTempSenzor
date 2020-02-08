
import unittest
import analog_temp_senzor_mqtt

class TestTempPort(unittest.TestCase):
      def test_temp_port(self):
          self.assertGreaterEqual(analog_temp.mcp.read_adc(0),200)
           

if __name__=="__main_":
    unittest.main()
