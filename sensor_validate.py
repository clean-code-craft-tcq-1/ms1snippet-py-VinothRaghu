
def  is_charge_rate_threshold_limit_exceeds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return True
  return False

def validate_soc_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1], 0.05)):
      return True
  return False

def validate_current_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1], 0.1)):
      return True
  return False
