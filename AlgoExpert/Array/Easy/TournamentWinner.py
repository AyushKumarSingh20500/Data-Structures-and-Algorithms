# Time: O(n)+O(m), n = length of competition/result array and m = length of scores dictionary | Space: O(m), m = length of score dictionary
# def tournamentWinner(competition, result):
#     score = {}
#     for idx in range(len(competition)):
#         if(result[idx] == 0):
#             if(competition[idx][1] in score.keys()):
#                 score[competition[idx][1]] += 1
#             else:
#                 score[competition[idx][1]] = 1
#         else:
#             if(competition[idx][0] in score.keys()):
#                 score[competition[idx][0]] += 1
#             else:
#                 score[competition[idx][0]] = 1
                
#     winner = ""
#     scored = 0
#     for k,v in score.items():
#         if(v > scored):
#             winner = k
#             scored = v
#     return winner
#     # return score

# print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))

# ----------------------------------------------------------------

# # Time: O(n), n = length of competition/result array | Space: O(m), m = length of score dictionary
# def tournamentWinner(competition, result):
#     score = {}
#     winner = ""
#     won = 0
#     for idx in range(len(competition)):
#         if(result[idx] == 0):
#             if(competition[idx][1] in score.keys()):
#                 score[competition[idx][1]] += 1
#                 if(score[competition[idx][1]] > won):
#                     winner = competition[idx][1]
#                     won = score[competition[idx][1]]
#             else:
#                 score[competition[idx][1]] = 1
#                 if(score[competition[idx][1]] > won):
#                     winner = competition[idx][1]
#                     won = score[competition[idx][1]]
#         else:
#             if(competition[idx][0] in score.keys()):
#                 score[competition[idx][0]] += 1
#                 if(score[competition[idx][0]] > won):
#                     winner = competition[idx][0]
#                     won = score[competition[idx][0]]
#             else:
#                 score[competition[idx][0]] = 1
#                 if(score[competition[idx][0]] > won):
#                     winner = competition[idx][0]
#                     won = score[competition[idx][0]]
                
#     return winner
#     # return score  # to check scores

# print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))

# Both done by me, without looking



def tournamentWinner(competitions,result):
    score = {}
    winner = ""
    winningScore = 0
    for idx in range(len(competitions)):
        if(result[idx] == 0):
            if(competitions[idx][1] in score.keys()):
                score[competitions[idx][1]] += 1
            else:
                score[competitions[idx][1]] = 1
                
            if(score[competitions[idx][1]] > winningScore):
                winningScore = score[competitions[idx][1]]
                winner = competitions[idx][1]
                
        elif(result[idx] == 1):
            if(competitions[idx][0] in score.keys()):
                score[competitions[idx][0]] += 1
            else:
                score[competitions[idx][0]] = 1
                
            if(score[competitions[idx][0]] > winningScore):
                winningScore = score[competitions[idx][0]]
                winner = competitions[idx][0]
                
    return winner

print(tournamentWinner([["html", "c#"], ["c#", "python"], ["python", "html"]], [0,0,1]))
