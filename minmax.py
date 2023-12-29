import math
 
def minimax (curDepth, nodeIndex,
             maxTurn, scores, 
             targetDepth):
    # print("curDepth ="+str(curDepth)+" ,nodeIndex ="+str(nodeIndex)+", maxTurn ="+str(maxTurn)+", scores="+str(scores)+", targetDepth ="+str(targetDepth))
    if (curDepth == targetDepth): 
        print("curent node is "+str(scores[nodeIndex]))
        return scores[nodeIndex]
     
    if (maxTurn):
        x =max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
        print("current max score is "+str(x))
        return x
    else:
        y= min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))
        print("current min score is "+str(y))
        return y
scores = [3, 5, 2, 9, 12, 5, 23, 23]
 
treeDepth = math.log(len(scores), 2)
 
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
