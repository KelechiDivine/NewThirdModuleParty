class GlobalKeyword:
    
    scores = 0
    def update_scores(new_score):
        global scores
        scores = new_score
    print(scores)

if __name__ == '__main__':
    GlobalKeyword()
    