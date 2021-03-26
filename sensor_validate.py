def  is_charge_rate_threshold_limit_exceeds(value, nextValue, parameter):
  maxDelta={"soc":0.05 ,"current":0.1}
  print(maxDelta[parameter])
  if nextValue - value > maxDelta[parameter]:
    return True
  return False
def validate_charging_parameter_reading(values,parameter):
   if(is_none(values) == False):
       last_but_one_reading = len(values) - 1
       print(last_but_one_reading)
       print(last_but_one_reading)
       for i in range(last_but_one_reading):
           print(i)
           if(is_charge_rate_threshold_limit_exceeds(values[i], values[i + 1],parameter)):
               print("charge rate reached maximum threshold limit exceeds")
               return True
   else:
       print("Given input is None")
   return False
def is_none(values):
    if values is None:
        return True
    else:
        return False
