#!/usr/bin/python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print("-----")
print("Using the .mro() method:")
print(FlyingFish.mro())

print("-----")
print("Using the .__mro__ attribute:")
print(FlyingFish.__mro__)

print("-----")
print("The class name MRO order:")
print("(Bottom to Top, Left to Right)")
for cls in FlyingFish.__mro__:
    print(f"Name: {cls.__name__}")
