from time import time
import os

# load the question
def get_question(num):
    file = open('testcase/' + num + '.txt', 'r')
    content = file.read()
    if len(content[:content.find("\n")])!= 9:
        content = content[content.find("\n"):]
    content = content.replace('\n', '')
    file.close()
    return content

# find the position with few (fewer than two) possible numbers, return that position and possible numbers
def lag_det(question):
    lag = 0
    length = 9
    possible = []
    for i in range(len(question)):
        if question[i] == '0':
            line = i // 9
            column = i % 9
            num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for j in question[line * 9: line * 9 + 9]:
                if j in num:
                    num.remove(j)
            for b in range(9):
                if question[9 * b + column] in num:
                    num.remove(question[9 * b + column])
            line = line // 3
            column = column // 3
            start = line * 27 + column * 3
            text = ''
            for ab in range(3):
                text += question[start: start + 3]
                start += 9
            for j in text:
                if j in num:
                    num.remove(j)
            if len(num) < 2:
                return i, num
            if length > len(num):
                length = len(num)
                possible = num
                lag = i
    return lag, possible


def solve(question):
    # check whether all the empty positions are
    # filled, if yes, print the solution
    if '0' not in question:
        print('Answer: ')
        for i in range(9):
            print(question[i * 9: i * 9 + 9])
        return True
    # if not, find the empty place with few
    # possible value, plug in possible value,
    # and go into the recursion function
    else:
        lag, nums = lag_det(question)
        possible = []
        for i in nums:
            possible.append(question[:lag] + i + question[lag + 1:])
        return any(solve(i) for i in possible)


def main():
    # load the question
    ques_num = input('which question do you want to solve? ')
    question = get_question(ques_num)
    # print the question
    print('Question:')
    for i in range(9):
        print(question[i * 9: i * 9 + 9])
    print(str(question.count('0')) + ' positions are blank')
    print()
    t = time()
    solve(question)
    print()
    print('time spent: ' + str(time() - t) + 's')


main()