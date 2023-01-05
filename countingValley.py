def countingValleys(steps, path):
    valleys = 0
    stepLevel = 0
    for steps in path:
        if(steps == 'U'):
            stepLevel += 1
            if(stepLevel == 0):
                valleys += 1
        elif(steps == 'D'):
            stepLevel -= 1
    return(valleys)
