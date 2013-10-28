#Basic bubble sort project
def bubble_sort(n):
    "The goal is to sort a series of numbers in ascending order. The procedure of a bubble sort"
    "is to compare adjacent numbers in pairs, two at a time, and swap the positions of the two"
    "numbers if a larger number comes before a shorter one. After the first pass through the series"
    "of numbers, the process repeats the pass through the entire list over and over again until there"
    "are no more number swaps needed.'"
    for i in range(0, len(n)):
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                
    return n