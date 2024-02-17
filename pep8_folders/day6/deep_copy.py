# One ECU monitors the following systems in endless loop:
# Cameras (4)
# Ultrasonic sensors (12)
# Radar (1)
# If any of the systems detect potential crash, signal in shape of the boolean value is sent to master ECU. Master
# ECU iterates through boolean list. If more than one sensor group detected potential crash, crash routine is started.
# One of the procedures triggered within crash routine is writing data to black box data recorder. This procedure 
# takes 5 seconds and boolean vector is written altogether with other data.
# Program should be written that boolean data will be preserved, after they are passed to master ECU and black box 
# recorder.

import time
import copy
cameras = [1,0,1,1]
sensor = [1,0,1,1,0,1,1,0,1,1,1,1]
radar = [1]
black_box_data_recorder = []

ECU = {"camera": cameras, "sensor": sensor, "radar": radar}
print(ECU)
master_ECU = copy.deepcopy(ECU)
print(master_ECU)

potential_crash = 0
for element in master_ECU.values():
    for i in element:
        if(i == 0):
            potential_crash += 1
            break

print(potential_crash)
if potential_crash > 1:
    print("crash routine started")
    for element in master_ECU.values():
        black_box_data_recorder = copy.deepcopy(master_ECU)
        time.sleep(5)

print(black_box_data_recorder)

