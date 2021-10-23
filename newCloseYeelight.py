import yeelight

bulbs = yeelight.discover_bulbs()

for b in bulbs:
    bulb = yeelight.Bulb(b["ip"])
    print(bulb.turn_off(1))