def planetWeight():

	userW = float(input("Write your weight on Earth(in kg): "))
	print("Planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto")
	planet = input("Write a planet name: ").lower()

	planets = {
	"mercury": 0.38,
	"venus": 0.91,
	"earth": 1,
	"mars": 0.38,
	"jupiter": 2.34,
	"saturn": 1.06,
	"uranus": 0.92,
	"neptune": 1.19,
	"pluto": 0.06
	}

	if planet not in planets:
		print("Incorrect!")
	else:
		gravity = planets.get(planet)

		result = userW * gravity

		print(f"Your weight on {planet} would be {result:.2f}kg!")

planetWeight()