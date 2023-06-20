class Score:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        
    def increaseScore1(self):
        self.score1 += 1
        
    def increaseScore2(self):
        self.score2 += 1
        
    def get_score1(self):
        return self.score1

    def get_score2(self):
        return self.score2