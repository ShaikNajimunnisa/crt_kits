class Player:
    def __init__(self, name): 
        self.name = name
        self.scores =  []

class Match:
    def __init__(self, score): 
        self.score = score

class Tournament:
    def report(self, player):
        final = sum(player.scores)  # Formula: Sum of Match Scores
        rank = "QUALIFIED" if final >= 300 else "NOT QUALIFIED"
        
        print("="*50)
        print("            TOURNAMENT REPORT")
        print("="*50)
        print(f"\nPlayer Name : {player.name}\n")
        print(f"Final Score : {final}\n")
        print(f"Rank Status : {rank}\n")
        print("="*50)

# Test Case
p = Player("Leo")
p.scores = [100, 150, 200]
Tournament().report(p)