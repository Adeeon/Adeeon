def compareTriplets(a, b):
    score = [0, 0]
    rot = 0
    while rot < 3:
        print(rot)
        if a[rot] < b[rot]:
            score[1] += 1
            rot += 1
            print('tea')
            print(rot)
        elif a[rot] > b[rot]:
            score[0] += 1
            rot += 1
            print('apples')
        elif a[rot] == b[rot]:
            rot += 1
    return score

list1 = [20, 20, 30]
list2 = [30, 10, 30]

print(compareTriplets(list1, list2))