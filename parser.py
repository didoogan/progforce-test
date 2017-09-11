import os
from collections import namedtuple


Letter = namedtuple('Letter', 'sender date subject')


class LetterClass(object):
    sender = ''
    subject = ''
    date = ''

    def __init__(self, message):
        lines = message.splitlines()
        for line in lines:
            if not self.sender and line.startswith('Author: '):
                self.sender = line.split('Author: ')[1]
            if not self.subject and line.startswith('Subject: '):
                self.subject = line.split('Subject: ')[1]
            if not self.date and line.startswith('Date: '):
                self.date = line.split('Date: ')[1]

    def get_letter(self):
        if self.sender:
            return Letter(self.sender, self.date, self.subject)
        return False


if __name__ == '__main__':
    letters = []
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, 'dich.txt')) as f:
        line = f.read()
    messages = line.split('This automatic notification')
    for message in messages:
        letter = LetterClass(message)
        result = letter.get_letter()
        if result:
            letters.append(result)
    for letter in letters:
        print('{} ({}): {}'.format(letter.sender, letter.date, letter.subject))
    result = {}
    for letter in letters:
        if letter.sender not in result:
            result[letter.sender] = 1
        else:
            result[letter.sender] += 1
    for k in result:
        print('{}: {}'.format(k, result[k]))
