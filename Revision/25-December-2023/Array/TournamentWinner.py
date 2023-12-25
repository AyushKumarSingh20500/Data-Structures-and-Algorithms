def tournamentWinner(competition,result):
    score = {}
    winner = ""
    competitionWon = 0
    for idx in range(len(competition)):
        if result[idx] == 0:
            if competition[idx][1] in score:
                score[competition[idx][1]] += 1
            else:
                score[competition[idx][1]] = 1
                
            if score[competition[idx][1]] > competitionWon:
                winner = competition[idx][1]
                competitionWon = score[competition[idx][1]]
        else:
            if competition[idx][0] in score:
                score[competition[idx][0]] += 1
            else:
                score[competition[idx][0]] = 1
                
            if score[competition[idx][0]] > competitionWon:
                winner = competition[idx][0]
                competitionWon = score[competition[idx][0]]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))
