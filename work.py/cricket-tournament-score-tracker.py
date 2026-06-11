class Player:
    def __init__(self, name): 
        self.name, self.runs = name, []

    def add_runs(self, r): 
        self.runs.append(r)

class Tournament:
    def report(self, player):
        total = sum(player.runs)
        matches = len(player.runs)
        avg = total / matches if matches else 0  # Formula: Total Runs / Matches Played
        
        print("="*50)
        print("             PLAYER PERFORMANCE REPORT")
        print("="*50)
        print(f"\nPlayer Name    : {player.name}")
        print(f"\nTotal Runs     : {total}")
        print(f"Matches Played : {matches}")
        print(f"Average Runs   : {avg}\n")
        print("="*50)

# Test Case
p = Player("Arjun")
for r in [50, 75, 100]: 
    p.add_runs(r)
Tournament().report(p)