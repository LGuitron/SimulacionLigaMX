from teams import teams_dictionary
from simulateGame import simulateGame


result1 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Chivas"])
result2 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Chivas"], canTie = False)

print("r1: " , result1, " r2: " , result2)
