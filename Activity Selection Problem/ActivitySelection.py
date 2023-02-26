
interviewList = [["I1", 8.00, 12.00],
                 ["I2", 11.00, 14.00],
                 ["I3", 9.00, 10.00],
                 ["I4", 10.00, 11.00],
                 ["I5", 11.00, 13.00],
                 ["I6", 15.00, 16.00]]


def selectInterviews(interviewList):
    interviewList.sort(key=lambda x: x[2])

    selected = 0
    first = interviewList[selected][0]
    print(first)

    for interview in range(len(interviewList)):
        if interviewList[interview][1] >= interviewList[selected][2]:
            print(interviewList[interview][0])
            selected = interview


selectInterviews(interviewList)
