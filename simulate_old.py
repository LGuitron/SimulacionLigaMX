from teams import teams_dictionary
from simulateGame import simulateGame
from future_games import *

# Parameters:
# jornada - 2D array of teams playing agains each other this week


# function to simulate a week of games
# Updates teams dictionary
def simulate_jornada(jornada):
    pass





def sort_teams():
    pass



def simulate_playoffs():
    pass
    
    
    
def simulate_league(simulation_amount = 1):
    
    # Dictionary for storing wins for each team
    victory_dict = {
        "Monterrey": 0,
        "Tigres":    0,
        "Leon":      0,
        "Chivas":    0,
        "Necaxa":    0,
        "Santos":    0,
        "Pachuca":   0,
        "Xolos":     0,
        "Atlas":     0,
        "Lobos":     0,
        "America":   0,
        "Pumas":     0,
        "Puebla":    0,
        "Cruz Azul": 0,
        "Toluca":    0,
        "Monarcas":  0,
        "Tiburones": 0,
        "Queretaro": 0
        }
    
    
    for i in range(simulation_amount):
        break
        #simulate_jornada(jornada8)
        #simulate_jornada(jornada9)
        #simulate_jornada(jornada10)
        #simulate_jornada(jornada11)
        #simulate_jornada(jornada12)
        #simulate_jornada(jornada13)
        #simulate_jornada(jornada14)
        #simulate_jornada(jornada15)
        #simulate_jornada(jornada16)
        #simulate_jornada(jornada17)
        #sort_teams()
        #simulate_playoffs()
    
    # Divide by number of simulations to get probabilities
    for team in victory_dict:
        victory_dict[team] *= 1/simulation_amount
    return victory_dict
