import unittest
import analog_temp.py

class TestTemp(unittest.TestCase):
      def test_temp(self):
          self.assertEqual(analog_temp_senzor_mqtt.read_temp_in_Celsius(3))

if __name__=="__main__":
    unittest.main()
