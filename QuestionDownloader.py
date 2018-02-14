import requests
import os

# using the difficulty, and date to download the question
def get_question(difficulty, year, month, day):
    url = 'http://cn.sudokupuzzle.org/printable.php?nd=%s&y=%s&m=%s&d=%s' % (difficulty, year, month, day)
    content = requests.get(url).text
    index = content.find("tmda='")
    content = content[index + 6: index + 87]
    return url, content

# prompt you to enter information, and download the questions regarding the information
# save the questions to testcase folder
def main():
    difficulty = input("difficulty(0-4): ")
    date = eval(input('Start YYYYMMDD: '))
    date1 = eval(input('End YYYYMMDD: '))
    num = 1
    while os.path.exists('testcase/' + str(num) + '.txt'):
        os.remove('testcase/' + str(num) + '.txt')
        num += 1
    num = 0
    while date <= date1:
        url, question = get_question(difficulty, str(date)[0:4], str(date)[4:6], str(date)[6:8])
        if question.isdigit():
            num += 1
            print(str(date) + ' done!')
            file = open("testcase/" + str(num) + '.txt', 'w')
            file.write(url + "\n")
            for i in range(9):
                file.write(question[i * 9: i * 9 + 9] + '\n')
        date += 1
        if date % 100 == 32:
            date += 69
        if date % 10000 == 1301:
            date += 8800
    print('All DONE!')
main()