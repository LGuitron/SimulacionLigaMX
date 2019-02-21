import random

# Calculate probability of teams win, tie, and lose,
# and simulate a game based on these probabilities

# Parameters:
# team1 - Team 1 stats (from dictionary)
# team2 - Team 2 stats (from dictionary)
# canTie - Boolean to define if the game can end in tie or not


# Returns:
# Result of the game
# {1        , 0     , -1       }
# {Team1 Win, Tie   , Team2 Win}
def simulateGame(team1, team2, canTie = True):
    
    # TODO use the ratings to Calculate this probability
    
    
    prob_win1 = 0.2     # % for team1 winning
    prob_tie  = 0.35    # % for tie
    
    
    # Tie outcome allowed
    if canTie:
    
        # Sample from probabilities to get result of the game
        random_value = random.random()
        if random_value < prob_win1:
            return 1
        elif random_value < prob_tie + prob_win1:
            return 0
        else:    # Sample from probabilities to get result of the game
    random_value = random.random()
    if random_value < prob_win1:
        return 1
    elif random_value < prob_tie + prob_win1:
        return 0
    else:
        return -1
    
            return -1
    
    # Tie not allowed
    else:
        
        
    
