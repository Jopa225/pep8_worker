
car = {1: {"break":False,"torque":False,"rotary_speed":10},
       2: {"break":False,"torque":False,"rotary_speed":26},
       3: {"break":False,"torque":False,"rotary_speed":30},
       4: {"break":False,"torque":False,"rotary_speed":40}}
avg = 0
for wheel in car:
    avg += car[wheel]["rotary_speed"]
# avg = car[1]["rotary_speed"] +car[2]["rotary_speed"] +car[3]["rotary_speed"] +car[4]["rotary_speed"] / 4
avg = avg / len(car)
print(avg)

deviation = avg * 0.05
print(deviation)

for wheel in car:
    if(car[wheel]["rotary_speed"] > avg + deviation):
        car[wheel]["break"] = True
    if(car[wheel]["rotary_speed"] < avg - deviation):
        car[wheel]["torque"] = True

for wheel in car.values():
    print(wheel)


