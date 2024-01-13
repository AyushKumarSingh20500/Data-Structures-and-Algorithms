def tournamentWinner(competitions,results):
    scores = {}
    winner = ""
    won = 0
    for idx in range(len(competitions)):
        if results[idx] == 0:
            if competitions[idx][1] in scores:
                scores[competitions[idx][1]] += 1
            else:
                scores[competitions[idx][1]] = 1
                
            if scores[competitions[idx][1]] > won:
                winner = competitions[idx][1]
                won = scores[competitions[idx][1]]
        else:
            if competitions[idx][0] in scores:
                scores[competitions[idx][0]] += 1
            else:
                scores[competitions[idx][0]] = 1
                
            if scores[competitions[idx][0]] > won:
                winner = competitions[idx][0]
                won = scores[competitions[idx][0]]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))