def calculateFuelRequirementByMass(mass, recursive=True):
  fuel_requirment = int(mass) // 3 - 2
  if not recursive:
    return fuel_requirment
  if fuel_requirment <= 0:
    return 0
  return fuel_requirment + calculateFuelRequirementByMass(fuel_requirment)

def main():
  filename = "puzzle_1.txt"
  module_masses = open(filename, "r").readlines()
  
  # Part 1
  sum_fuel_requirment = 0
  for mass in module_masses:
    fuel_requirment = calculateFuelRequirementByMass(mass, False)
    sum_fuel_requirment += fuel_requirment
  print(f"Result part 1 = {sum_fuel_requirment}")

  # Part 2
  sum_fuel_requirment = 0
  for mass in module_masses:
    fuel_requirment = calculateFuelRequirementByMass(mass)
    sum_fuel_requirment += fuel_requirment
  print(f"Result part 2 = {sum_fuel_requirment}")

if __name__ == "__main__":
  main()
