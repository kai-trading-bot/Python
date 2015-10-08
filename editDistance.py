# This function returns the unbiased distance between two string inputs
# Khizar Qureshi
# This version: 20151008

def editDistance(s1,s2): #Input two strings)
    if len(s1) > len(s2):
        s1,s2=s2,s1 #Switch order: shorter string first
    distances=range(len(s1)+1) #index shorter string for upcoming loop
    for index2, char2 in enumerate(s2):
        #Along the longer string, compute pairwise distances with shorter string and append.
        #Take last element as Edit distance
        newDistances=[index2+1] 
        for index1,char1 in enumerate(s1):
            if char1==char2:
                newDistances.append(distances[index1])
                #Distance remains the same
            else:
                newDistances.append(1+min((distances[index1],distances[index1+1],newDistances[-1])))
                #Creates a condition to append max distances between chars, equal or unequal
        distances=newDistances
                #Reset based on update
    return distances[-1]


# Test cases

print(editDistance("hello","ello"))
print(editDistance("code","model"))
print(editDistance("convert", "low"))