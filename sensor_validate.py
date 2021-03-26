maxDelta={"soc":0.05 ,"current":0.1}
def  is_charge_rate_threshold_limit_exceeds(value, nextValue, parameter):
  print(maxDelta[parameter])
  if nextValue - value > maxDelta[parameter]:
    return True
  return False
def validate_charging_parameter_reading(values,parameter):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
        if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1],parameter)):
              return True
        return False
