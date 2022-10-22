if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    second_lowest = sorted(set(scores))[1]
    res = [i[0] for i in students if i[1]==second_lowest]
    for i in sorted(res):
        print(i)
