def tournamentWinner(competition,result):
    scores = {}
    winner = ""
    competitionWon = 0
    for idx in range(len(competition)):
        if result[idx] == 0:
            if competition[idx][1] in scores.keys():
                scores[competition[idx][1]] += 1
            else:
                scores[competition[idx][1]] = 1
                
            if scores[competition[idx][1]] > competitionWon:
                winner = competition[idx][1]
                competitionWon = scores[competition[idx][1]]
        else:
            if competition[idx][0] in scores.keys():
                scores[competition[idx][0]] += 1
            else:
                scores[competition[idx][0]] = 1
                
            if scores[competition[idx][0]] > competitionWon:
                winner = competition[idx][0]
                competitionWon = scores[competition[idx][0]]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))