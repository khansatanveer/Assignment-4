def main():
    planet_gravity = {
        "MERCURY": 0.376,
        "VENUS": 0.889,
        "MARS": 0.378,
        "JUPITER": 2.36,
        "SATURN": 1.081,
        "URANUS": 0.815,
        "NEPTUNE": 1.14,
    }

    # Ask for user's weight on Earth
    try:
        earth_weight = float(input("Enter your weight on Earth : "))
    except ValueError:
        print("Please enter a valid number for weight.")
        return

    # Ask for the target planet
    planet = input("Enter a planet: ").strip().upper()

    # Calculate the equivalent weight
    if planet in planet_gravity:
        equivalent_weight = round(earth_weight * planet_gravity[planet], 2)
        print(f"Your weight on {planet.title()} would be: {equivalent_weight} ")
    else:
        print("That planet is not in our database.")

if __name__ == "__main__":
    main()
