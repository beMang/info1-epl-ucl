def binary_search(course, list_of_courses):
    first = 0
    last = len(list_of_courses)-1
    found = False

    while first <= last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][0] == course:
            found = True
        else:
            if course < list_of_courses[middle][0]:
                last = middle-1
            else:
                first = middle+1

    if found == True:
        return list_of_courses[middle][1]
    else:
        return []
