# ABS ECU reads the following signals
# Speed received from gearbox
# Speed received from every wheel (stored in dictionary)
# Speed received from GPS
# Create ESP ECU (using shallow copy) which reads the same signals
# Change the speed of gearbox, one wheel and speed from GPS
# Compare values read by ABS and ESP

import copy

ABS_ECU = {"gearbox": 10, "wheel": {"wheel1":1,"wheel2":2,"wheel3":3,"wheel4":4}, "GPS": 15}

ESP_ECU = copy.copy(ABS_ECU)
ESP_ECU["gearbox"] = 22
ESP_ECU["GPS"] = 33
print(ABS_ECU["wheel"]["wheel1"])
ESP_ECU["wheel"]["wheel1"] = 55

print(ABS_ECU["wheel"]["wheel1"])
print(ESP_ECU["wheel"]["wheel1"])

print(ABS_ECU["gearbox"])
print(ESP_ECU["gearbox"])

print(ABS_ECU["GPS"])
print(ESP_ECU["GPS"])

print(ABS_ECU)
print(ESP_ECU)
