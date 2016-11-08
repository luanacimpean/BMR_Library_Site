import csv
# import model
from polls.models import Question
from django.utils import timezone

# open and read csvfile
dataReader = csv.reader(open('/Users/luanacimpean/Documents/Work/Web Developer/question.csv'), delimiter=',', quotechar='"')

#count is to count the number of lines: ignore line 0
line_count = 0
for line in dataReader:
	if line_count > 0:
		print(line)
		q = Question(question_text=line[0], pub_date=timezone.now())
		try:
			q.save()
		except:
			print ("there was a problem with line", line)
	line_count += 1

# print ("total count of lines:", line_count)