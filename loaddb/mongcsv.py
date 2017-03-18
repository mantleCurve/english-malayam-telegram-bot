from mongoengine import *
import json

connect('olam-ml3')


class Olamdict(Document):
	english = StringField()
	speech = StringField()
	malayalam = StringField()

file = open('olam-enml.csv')
a = []
for line in file.readlines()[1:]:
	print(line)
	li = line.split(",")
	olam = Olamdict()
	olam.english = li[1]
	olam.speech = li[2]
	olam.malayalam = li[3]
	olam.save()
	print(olam.to_json())