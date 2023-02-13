import os
import json
import datetime
import csv


time = datetime.datetime.now()
category = os.path.basename(os.getcwd())
#Create backup
csvFilename = rf'{category} errorList.csv'
csvBackupname = time.strftime('%Y-%m-%d--%H-%M-%S')+rf' {csvFilename}'+r'.backup'
if os.path.exists(csvFilename):
	os.rename(csvFilename,csvBackupname)
csvFile = open(csvFilename, 'w')
#Create folder for inspection
reviewFolder = r'./manualReview'
if not os.path.exists(reviewFolder):
	os.mkdir(reviewFolder)
reviewCount = 0
fileCount = 0
errorCount = 0
for root, dirs, files in os.walk('.'):
	for file in files:
		if(file.endswith(".json")):
			fileCount += 1
			idFromFilename = file.split('.')[0]
			try:
				data = json.load(open(os.path.join(file), 'r'))
			#Wenn ein Fehler beim Zugriff auf die Daten passiert wird das File ins ReviewFolder verschoben
			except:
				print(rf"Fehler bei ID: {idFromFilename} - in reviewFolder verschoben")
				os.rename(rf'{idFromFilename}.json', rf'{reviewFolder}/No Access to Data - {idFromFilename}.json')
				reviewCount += 1
				data = []
				continue
			#Check ob ein Profil gescraped wurde, welches keine ID besitzt
			if 'id' in data:
				idFromData = str(data['id'])
				if idFromData != idFromFilename:
					errorCount += 1
					csvFile.write(f'{idFromFilename}\n')
			#Alle Profile ohne ID sehen so aus: https://imgur.com/a/2LJden3
			else:
				print(rf'Datei {idFromFilename}.json hat keine ID - in reviewFolder verschoben')
				fileCount -= 1
				#Das fehlerhafte Profil wird ins ReviewFolder verschoben. Es wird nicht in die .csv geschrieben, da es nicht nochmal gescraped werden soll
				os.rename(rf'{idFromFilename}.json', rf'{reviewFolder}/No ID in Data - {idFromFilename}.json')
				reviewCount += 1
	break
csvFile.close()
errorRate = round((errorCount/fileCount)*100, 2)
print(f'{errorCount} of {fileCount} files were faulty ({errorRate}%)')
if reviewCount > 0:
	print(rf'{reviewCount} file(s) moved to reviewFolder - please manually review these files.')
log = open(rf'{category}_log.txt', 'a')
dateStr = time.strftime('%d.%m.%Y')
timeStr = time.strftime('%H:%M:%S')
log.write(f'Validierung am {dateStr} um {timeStr} Uhr:\nFehler: {errorCount}\nRichtig: {fileCount - errorCount}\nGesamt: {fileCount}\nFehlerquote: {errorRate}%\n\n')
log.close()
#Zweiter Teil:
#Alle fehlerhaften Profile koennen optional geloescht werden
def delete_faulty_jsons():
	deleteCounter = 0
	with open(rf'{category} errorList.csv', mode = 'r') as file:
		tempCsv = csv.reader(file)
		for line in tempCsv:
			filename = line[0]+'.json'
			if os.path.exists(filename):
				os.remove(filename)
				deleteCounter += 1
			else:
				print(rf'File {filename} not found')
	print(rf'{deleteCounter} files deleted')
confirmation = input(r"Type 'DELETE' to delete faulty .jsons: ")
if confirmation == 'DELETE':
	delete_faulty_jsons()
else:
	print('No files deleted')