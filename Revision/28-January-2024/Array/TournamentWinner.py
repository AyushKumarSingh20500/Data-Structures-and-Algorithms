def tournamentWinner(competitions,results):
    score = {}
    winner = ""
    won = 0
    for idx in range(len(competitions)):
        if results[idx] == 0:
            if competitions[idx][1] in score:
                score[competitions[idx][1]] += 1
            else:
                score[competitions[idx][1]] = 1
                
            if score[competitions[idx][1]] > won:
                won = score[competitions[idx][1]]
                winner = competitions[idx][1]
        else:
            if competitions[idx][0] in score:
                score[competitions[idx][0]] += 1
            else:
                score[competitions[idx][0]] = 1
                
            if score[competitions[idx][0]] > won:
                won = score[competitions[idx][0]]
                winner = competitions[idx][0]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))