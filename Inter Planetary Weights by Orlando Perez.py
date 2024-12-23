MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066
sName = input("Please enter your name: ")
nEarthWeight = float(input("Enter your weight on Earth (in pounds): "))
nMercuryWeight = nEarthWeight * MERCURY_GRAVITY
nVenusWeight = nEarthWeight * VENUS_GRAVITY
nMoonWeight = nEarthWeight * MOON_GRAVITY
nMarsWeight = nEarthWeight * MARS_GRAVITY
nJupiterWeight = nEarthWeight * JUPITER_GRAVITY
nSaturnWeight = nEarthWeight * SATURN_GRAVITY
nUranusWeight = nEarthWeight * URANUS_GRAVITY
nNeptuneWeight = nEarthWeight * NEPTUNE_GRAVITY
nPlutoWeight = nEarthWeight * PLUTO_GRAVITY
print(f"{sName}, welcome to the Solar System's weight calculator!")
print(f"Your weight on different planets would be:")
print(f"Mercury:  {nMercuryWeight:10.2f} lbs")
print(f"Venus:    {nVenusWeight:10.2f} lbs")
print(f"Moon:     {nMoonWeight:10.2f} lbs")
print(f"Mars:     {nMarsWeight:10.2f} lbs")
print(f"Jupiter:  {nJupiterWeight:10.2f} lbs")
print(f"Saturn:   {nSaturnWeight:10.2f} lbs")
print(f"Uranus:   {nUranusWeight:10.2f} lbs")
print(f"Neptune:  {nNeptuneWeight:10.2f} lbs")
print(f"Pluto:    {nPlutoWeight:10.2f} lbs")

