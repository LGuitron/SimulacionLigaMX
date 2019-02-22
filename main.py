from teams import teams_dictionary
from simulateGame import simulateGame
from simulate_league import simulate_league
from update_ratings import update_all_ratings

update_all_ratings()
result1 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Queretaro"])
result1 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Queretaro"], canTie = False)
#result2 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Chivas"])
#result2 = simulateGame(teams_dictionary["Monterrey"], teams_dictionary["Chivas"], canTie = False)
results = simulate_league(simulation_amount = 50000)
print(results)
