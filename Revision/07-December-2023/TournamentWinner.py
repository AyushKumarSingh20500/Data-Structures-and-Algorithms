def tournamentWinner(competition,result):
    score = {}
    winner = ""
    won = 0
    for i in range(len(competition)):
        if result[i] == 0:
            if competition[i][1] in score.keys():
                score[competition[i][1]] = score[competition[i][1]] + 1
            else:
                score[competition[i][1]] = 1
                
            if score[competition[i][1]] > won:
                winner = competition[i][1]
                won = score[competition[i][1]]
        else:
            if competition[i][0] in score.keys():
                score[competition[i][0]] = score[competition[i][0]] + 1
            else:
                score[competition[i][0]] = 1
                
            if score[competition[i][0]] > won:
                winner = competition[i][0]
                won = score[competition[i][0]]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))
