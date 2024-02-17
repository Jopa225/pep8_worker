
dtc = 40

memory_is_full = False
engine_speed = 0
vehicle_speed = 0

if(engine_speed == 0 and vehicle_speed == 0 and dtc == 40):
    print("Clearing dtc acitvated")

interior_light = False
doors_are_open = False
car_locked = False

if(doors_are_open == False):
    interior_light = False
    print("interior light off")
elif(doors_are_open == True and car_locked == False):
    interior_light = True
    print("interior light on")

steering_vheel = False
if(vehicle_speed != 0):
    steering_vheel = False

airbag_activate
crash = False

if(crash == True and vehicle_speed < 60):
    airbag_activate = True
    print("airbag activated")

warning_light = False
light_bulbs = False

if(light_bulbs == False):
    warning_light = True
    print("warninglight working")

engine_started = False
if(doors_are_open == False and engine_started == True):
    interior_light = False
    print("interior light turned off")

bist_error = True

if(bist_error == True):
    print("DIFERENT reaction")



