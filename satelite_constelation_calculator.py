import math

# Define constants
gravitationalParameter = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

bodies = [
    # Planet name | Mass (kg)        | Equatorial radius (m) | Minimum safe orbital altitude (m)
    ["Kerbol",    1.7565459e28,      261600000,              1340],       # Star
    ["Moho",      2.5263314e21,      250000,                 10000],      # 1st planet
    ["Eve",       1.2243980e23,      700000,                 90000],      # 2nd planet
    ["Gilly",     1.2420512e17,      13000,                  6000],       # Moon of Eve
    ["Kerbin",    5.2915793e22,      600000,                 70000],      # 3rd planet
    ["Mun",       9.7599066e20,      200000,                 7000],       # Moon of Kerbin
    ["Minmus",    2.6457580e19,      60000,                  6000],       # Moon of Kerbin
    ["Duna",      4.5154270e21,      320000,                 60000],      # 4th planet
    ["Ike",       2.7821615e20,      130000,                 10000],      # Moon of Duna
    ["Dres",      3.2190937e20,      138000,                 10000],      # 5th planet
    ["Jool",      4.2332127e24,      6000000,                200000],     # 6th planet
    ["Laythe",    2.9397311e22,      500000,                 50000],      # Moon of Jool
    ["Vall",      3.1087655e21,      300000,                 10000],      # Moon of Jool
    ["Tylo",      4.2332127e22,      600000,                 10000],      # Moon of Jool
    ["Bop",       3.7261085e19,      65000,                  10000],      # Moon of Jool
    ["Pol",       1.0813507e19,      44000,                  10000],      # Moon of Jool
    ["Eeloo",     1.1149358e21,      210000,                 10000],      # 7th planet
]

# Get the number of rows
bodiesLength = len(bodies)

# List all available planets & moons
for currentRow in range(bodiesLength):
    print(f"{currentRow + 1}: {bodies[currentRow][0]}")

# Get desired body
body = int(input("Choose a body to start: "))
body -= 1
print(f"\nChosen body: {bodies[body][0]}")

# Minimum safe orbital altitude
safeAltitude = bodies[body][3]

# Get desired apoapsis and periapsis
while True:
    periapsis = int(input(f"Desired Periapsis in meters above sea level: "))
    if periapsis >= safeAltitude:
        break
    else:
        print(f"Warning: Periapsis must be at least {safeAltitude}m. Please enter a valid value.")

while True:
    apoapsis = int(input(f"Desired Apoapsis in meters above sea level: "))
    if apoapsis >= safeAltitude:
        break
    else:
        print(f"Warning: Apoapsis must be at least {safeAltitude}m. Please enter a valid value.")

# Ensure apoapsis is greater than periapsis
while apoapsis < periapsis:
    print("Warning: Apoapsis must be greater than Periapsis.")
    apoapsis = int(input("Please re-enter the Apoapsis in meters above sea level: "))

# Get number of satellites and number of passes per satellite
satellites = int(input("Desired number of satellites in constellation: "))
orbits = int(input("How many orbits per satellite: "))

# Get semi-major axis
semiMajorAxis = (apoapsis + periapsis) / 2 + bodies[body][2]

# Get orbital period using Kepler's third law
orbitalPeriod = 2 * math.pi * math.sqrt(semiMajorAxis ** 3 / (gravitationalParameter * bodies[body][1]))

# Transfer period calculation
transferPeriod = orbitalPeriod * (1 + 1 / (satellites * orbits))

# Calculate the transfer semi-major axis
transferSemiMajorAxis = ((gravitationalParameter * bodies[body][1] * transferPeriod**2) / (4 * math.pi**2)) ** (1/3)

# Calculate transfer apoapsis
transferApoapsis = int((transferSemiMajorAxis - bodies[body][2]) * 2 - periapsis)

# Compile and print the data
print("\nTransfer Orbit Plan:")
print(f"1: Get into an orbit with an apoapsis of {apoapsis}m, a periapsis of {periapsis}m")
print(f"2: Increase your apoapsis to {transferApoapsis}m")
print(f"3: Release a satellite every {orbits} orbits")
print(f"4: Reduce the satellite's apoapsis back to {apoapsis}m")
print(f"5: Repeat for all {satellites} satellites")
