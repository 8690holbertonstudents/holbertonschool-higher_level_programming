#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

print("--------------")

draco = Dragon()
draco_s = draco.swim()
draco_f = draco.fly()
draco_r = draco.roar()
draco_b = draco.breath()
draco_m = draco.master_of()
