import sys, os

# open file & create csvreader
import csv

# import the relevant model
#from zips.models import ZipCode

# Full path and name to your csv file
#csv_filepathname="/home/mitch/projects/wantbox.com/wantbox/zips/data/zipcodes.csv"
csv_filepathname="sub1.tsv"
# Full path to your django project directory
your_djangoproject_home="/home/mitch/projects/wantbox.com/wantbox/"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

     
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
	try:
		if row[0] != 'Series':
		    #zipcode = ZipCode()
		    series = row[0]
		    subseries = row[1]
		    box = row[2]
		    file = row[3]
		    year = row[4]
		    month = row[5]
		    day = row[6]
		    publication_series =  row[7]
		    document_number = row[8]
		    title = row[9]
		    scanned =  row[10]
		    reviewed = row[11]
		    follow_up = row[12]
		    subject = row[13]
		    keywords	= row[14]
		    summary = row[15]
		    researcher = row[16]
		    notes_comments = row[17]
		    personnel = row[18]																	
		    #zipcode.save()
	       
		    print(series)
	except:
		print("Error")
			
			