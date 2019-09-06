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
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Parent Class
class Vehicle:
    pass

#child of Parent class
class GroundVehicle(Vehicle):
    pass

#child of GroundVehicle
class Car(GroundVehicle):
    pass

#child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass

#child of Vehicle
class FlightVehicle(Vehicle):
    pass

#child of FlightVehicle
class Airplane(FlightVehicle):
    pass

#child of FlightVehicle
class Starship(FlightVehicle):
    pass