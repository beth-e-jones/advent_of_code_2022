# %%
def read_text_file(path: str) -> list[str]:
    """Read text file.

    Reads an input text file into a list of strings. Removes trailing
    new line characters.

    Parameters
    ----------
    path : str
        path to input text file.

    Returns
    -------
    list: [str]
        text file content in a list of strings
        pretend change

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


DATAPATH = "test_input.txt"

matches = read_text_file(DATAPATH)
# %%
# Sets scores for all possible rock, paper, scissors moves
my_scores_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

opponent_scores_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def find_scores(matches):
    """Generates a list of all the scores from the moves in each game 
    by matching the moves against a dictionary of scores for both 
    players and appending the values to lists of scores.

    Args:
        matches (list): List of strings, each containing 2 letters to
        represent each players' move.

    Returns:
        opponent_scores (list): List of integers for the scores for
        each match in the list of matches.
        
        my_scores (list): list of integers for the score for each match
        in the list of matches
    """
    my_scores = []
    opponent_scores = []
    for match in matches:
        opponent_play, my_play = match.split(" ")
        opponent_scores.append(opponent_scores_dict[opponent_play])
        my_scores.append(my_scores_dict[my_play])
                   
    return opponent_scores, my_scores

#find_scores(matches)

def score_wins():
    my_wins = []
    opponent_wins = []
    opponent_scores, my_scores = find_scores(matches)

    for opponent_score, my_score in zip(opponent_scores, my_scores):
        #print(opponent_scores)
        #print(my_scores)
        match opponent_score:
            # Where opponent score is a certain score, and my score is
            # a set score, carry out specific actions to add points
            case 1:
                match my_score:
                    case 1:
                        my_wins.append(3)
                        opponent_wins.append(3)
                    case 2:
                        my_wins.append(6)
                    case _:
                        opponent_wins.append(6)
            case 2:
                match my_score:
                    case 1:
                        opponent_wins.append(6)
                    case 2:
                        my_wins.append(3)
                        opponent_wins.append(3)
                    case _:
                        my_wins.append(6)
            case _:
                match my_score:
                    case 1:
                        my_wins.append(6)
                    case 2:
                        opponent_wins.append(6)
                    case _:
                        my_wins.append(3)
                        opponent_wins.append(3)
                    
    return sum(my_scores) + sum(my_wins)


score_wins()

""" Part 2"""

# run the scores 
# if X,lose
# if y, draw

def follow_strategy():
    opponent_scores, my_scores = find_scores(matches)
    part_2_wins = []
    part_2_opponent_wins = []
    
    # maths not right here!
    for opponent_score, my_score in zip(opponent_scores,my_scores):
        if opponent_score == 1:
            if my_score == 1:
                part_2_wins.append(3)
                part_2_opponent_wins.append(6)
            elif my_score == 2:
                part_2_wins.append(1)
                part_2_opponent_wins.append(3)
                part_2_wins.append(3)
            else:
                part_2_wins.append(2)
                part_2_wins.append(6)
        
        elif opponent_score == 2:
            if my_score == 1:
                part_2_wins.append(1)
            
            elif my_score == 2:
                part_2_wins.append(2) 
                part_2_opponent_wins.append(3)
                part_2_wins.append(3)
            
            else:
                part_2_wins.append(3)
                part_2_wins.append(6)
        
        else:
            if my_score == 1:
            # lose
                part_2_opponent_wins.append(6)
                part_2_wins.append(2)
            elif my_score == 2:
                part_2_wins.append(3) 
                part_2_opponent_wins.append(3)
                part_2_wins.append(3)
            else:
                part_2_wins.append(1)
                part_2_wins.append(6)
    #print(part_2_wins)
    return sum(part_2_wins)

follow_strategy()