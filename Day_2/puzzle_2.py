def calculate(programCodeOne, programCodeTwo, opCodes):
  opCodes[1] = programCodeOne
  opCodes[2] = programCodeTwo
  index = 0
  result = 0
  while opCodes[index] != 99:
    if index > len(opCodes):
      break
    opCode = opCodes[index]
    NumberOne = opCodes[opCodes[index + 1]]
    numberTwo = opCodes[opCodes[index + 2]]
    if opCode == 1:
      result = NumberOne + numberTwo
    if opCode == 2:
      result = NumberOne * numberTwo
    opCodes[opCodes[index + 3]] = result
    index += 4

  #print(f"Iteration #{index//4}")
  #print(opCodes)
  #print("")
  return opCodes[0]

def getProgramCode(opCodes, goal, rangeLimit=100):
  for i in range(rangeLimit):
    for j in range(rangeLimit):
      if calculate(i, j, opCodes[:]) == goal:
        result = 100 * i + j
        print(f"Noun = {i}, Verb = {j}")
        return result

def main():
  fileName = "puzzle_2.txt"
  opCodesFile = open(fileName, "r").readlines()[0].strip("\n")
  opCodes = [int(element) for element in opCodesFile.split(",")]

  # Part 1
  result1 = calculate(12, 2, opCodes[:])
  print(f"Result to part 1 = {result1}")

  # Part 2
  goal = 19690720
  result2 = getProgramCode(opCodes[:], goal)
  print(f"Result to part 2 = {result2}")

if __name__ == "__main__":
  main()
