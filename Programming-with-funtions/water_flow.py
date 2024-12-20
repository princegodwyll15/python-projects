# EARTH_ACCELERATION_OF_GRAVITY 
gravity =	9.8066500
# WATER_DENSITY
w_density= 998.2000000
# WATER_DYNAMIC_VISCOSITY
viscosity = 0.0010016



print("""A program to help an engineer design a water distribution system. """)
# function to calculate the height of a column of water from a tower height and a tank wall height
# h is height of the water column
# t is the height of the tower
# w is the height of the walls of the tank that is on top of the tower
def water_column_height(t, w):
    h = t + ((3 * w) / 4)
    return h


# pressure in kilopascals
def pressure_gain_from_water_height(height):
    # h height of a column of water column in meters
    h = water_column_height(height, 0)  # Pass height as t and 0 as w
    pressure = (w_density * gravity * h) / 1000
    return pressure


def pressure_loss_from_pipe(d, L, f, v):
    # d is the diameter of the pipe in meters
    # L is the length of the pipe in meters
    # f is the pipe's friction factor
    # v velocity of the water flowing through the pipe in meters/second(fluid_velocity)
    pressure_lost = (-f * (L * w_density * (v**2))) / (2000 * d)
    return pressure_lost


def pressure_loss_from_fittings (v, n):
    # P is the lost pressure in kilopascals
    # v is the velocity of the water flowing through the pipe in meters / second
    # n is the quantity of fittings
    P = (-0.04 * w_density * (v**2) * n) /2000
    return P


def reynolds_number(d, v):
# R is the Reynolds number
# d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
# v is the velocity of the water flowing through the pipe in meters / second
    R = (w_density * d * v) / viscosity
    return R

def pressure_loss_from_pipe_reduction(D, v, R, d):
# k is a constant computed by the first formula and used in the second formula
# R is the Reynolds number that corresponds to the pipe with the larger diameter
# D is the diameter of the larger pipe in meters
# d is the diameter of the smaller pipe in meters
# P is the lost pressure kilopascals
# v is the velocity of the water flowing through the larger diameter pipe in meters / second
    k = (0.1 + 50/R) * ((D/d)**4 -1)
    P = ((-k) * w_density * v**2) / 2200
    return P

def convert_kpa_to_psi(kpa):
    psi = kpa / 6.895
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    pressure_kpa = pressure_gain_from_water_height(water_height)
    pressure_psi = convert_kpa_to_psi(pressure_kpa)

    print(f"Pressure in kPa: {pressure_kpa:.2f}")
    print(f"Pressure in psi: {pressure_psi:.2f}")

if __name__ == "__main__":
    main()

