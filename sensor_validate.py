def  is_charge_rate_threshold_limit_exceeds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return True
  return False
def validate_charging_parameter_reading(values,parameter):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
	if(parameter=='soc'):
		if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1],0.05)):
			return True
	elif(parameter=='current'):
		if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1],0.05)):
			return True
	return False
