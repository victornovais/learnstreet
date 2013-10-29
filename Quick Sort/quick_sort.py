# Quick Sort Exercise
def quickSort(l):
    run.ctr += 1
    
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        lesser = quickSort([el for el in l[1:] if el < pivot])
    	greater = quickSort([el for el in l[1:] if el >= pivot])
        
        return lesser + [pivot] + greater

# Take things from text box and prepare output
def run(text):
    run.ctr = 0
    outstring = ""
    numbers = map(int, text.split(' '))
    outstring += "Sorted Numbers: " + str(quickSort(numbers))
    outstring += "<br>Recursions: " + str(run.ctr)
    return outstring