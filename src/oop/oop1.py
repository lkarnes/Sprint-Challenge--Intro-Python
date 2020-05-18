# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.

#base for all
class Vehicle:
    pass
#base for ground vehicles car and motorcyle
class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
#base for flying airplane and startship
class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass


#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
