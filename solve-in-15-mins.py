# https://practice.geeksforgeeks.org/problems/frequency-game/1

def LargButMinFreq(arr,n):
    cnts = {}
    for a in arr:
        if a in cnts.keys():
            cnts[a]+=1
        else:
            cnts[a]=1
    min_freq = min(cnts.values())
    return max([k for k in cnts.keys() if cnts[k]==min_freq])
