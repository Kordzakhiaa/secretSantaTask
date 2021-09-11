import random
import pprint

f = open('mails.txt')
emails = f.read().split('\n')
f.close()

random.shuffle(emails)
offset = [emails[-1]] + emails[:-1]


giver_reciever = [{santa: receiver} for santa, receiver in zip(emails, offset)]


if __name__ == '__main__':
    pprint.pprint(giver_reciever)
