def calculate_energy(mass):
    speed_of_light = 300000000  
    energy = mass * speed_of_light ** 2
    return energy

def main():
    mass = int(input("Enter the mass in kilograms: "))
    energy = calculate_energy(mass)
    print("Equivalent energy in Joules:", energy)

if __name__ == "__main__":
    main()
