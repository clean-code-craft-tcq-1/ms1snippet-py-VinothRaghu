def  is_charge_rate_threshold_limit_exceeds(value, nextValue, parameter):
  maxDelta={"soc":0.05 ,"current":0.1}
  print(maxDelta[parameter])
  if nextValue - value > maxDelta[parameter]:
    return True
  return False


def validate_charging_parameter_reading(values,parameter):
    if(values != None): 
        return parameter_excheed_thresholds_limit(values,parameter)
    else:
        print("Given input is None")
        return False
    

def parameter_excheed_thresholds_limit(values_1,parameter_1):
       last_but_one_reading = len(values_1) - 1
       for i in range(last_but_one_reading):
           print(i)
           if(is_charge_rate_threshold_limit_exceeds(values_1[i], values_1[i + 1],parameter_1)):
               print(f'{parameter_1} maximum threshold limit exceeds')
               return True
       print(f'{parameter_1} limit not reached')
       return False
