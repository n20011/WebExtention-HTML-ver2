N, Pass = map(int, input().split())



def safe_out(Score, Absence, Pass):
    Scoring = Score - (Absence * 5)
    if Scoring >= Pass or Pass == 0:
        return True
    return False



for nunber in range(N):
    Score, Absence = map(int, input().split())
    if safe_out(Score, Absence, Pass):
        print(nunber + 1)