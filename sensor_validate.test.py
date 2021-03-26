import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_current_jumps(self):
    self.assertTrue(
      sensor_validate.validate_charging_parameter_reading([0.03, 0.03, 0.03, 0.33],"current")
    )
  def test_reports_error_when_none_sent(self):
    self.assertFalse(
      sensor_validate.validate_charging_parameter_reading(None,"None")
    )
  def test_reports_error_when_soc_jumps(self):
    self.assertFalse(
      sensor_validate.validate_charging_parameter_reading([0.0, 0.01, 0.05, 0.051],"soc")
    )

if __name__ == "__main__":
  unittest.main()
