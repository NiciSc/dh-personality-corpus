"""This module validates if scrapted JSONS:
    -	contain any ID
    -	contain the same ID as their filename suggests
    and deletes faulty JSONs.
    Works under Windows"""
import csv
import datetime
import json
import os

time = datetime.datetime.now()
category = os.path.basename(os.getcwd())
# Create backup
csvFilename = rf'{category} errorList.csv'
csvBackupname = time.strftime(
    '%Y-%m-%d--%H-%M-%S')+rf' {csvFilename}'+r'.backup'
if os.path.exists(csvFilename):
    os.rename(csvFilename, csvBackupname)
csvFile = open(csvFilename, 'w', encoding='UTF-8')
reviewCount = 0
fileCount = 0
errorCount = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".json"):
            fileCount += 1
            idFromFilename = file.split('.')[0]
            try:
                data = json.load(open(os.path.join(file), encoding='UTF-8'))
            # Wenn ein Fehler beim Zugriff auf die Daten passiert wird das File gelöscht
            except:
                print(
                    rf'Fehler beim Zugriff auf ID: {idFromFilename} - Datei gelöscht')
                os.remove(file)
                reviewCount += 1
                data = []
                continue
            # Check ob ein Profil gescraped wurde, welches keine ID besitzt
            if 'id' in data:
                idFromData = str(data['id'])
                if idFromData != idFromFilename:
                    errorCount += 1
                    csvFile.write(f'{idFromFilename}\n')
            # Alle Profile ohne ID sehen so aus: https://imgur.com/a/2LJden3
            else:
                print(
                    rf'Datei {idFromFilename}.json hat keine ID - Datei gelöscht')
                fileCount -= 1
                # Das fehlerhafte Profil wird ins ReviewFolder verschoben.
                # Es wird nicht in die .csv geschrieben, da es nicht nochmal gescraped werden soll
                os.remove(file)
                reviewCount += 1
    break
csvFile.close()
errorRate = round((errorCount/fileCount)*100, 2)
print(f'{errorCount} of {fileCount} files were faulty ({errorRate}%)')
if reviewCount > 0:
    print(rf'{reviewCount} file(s) were removed due to having no ID or not being accessible')
log = open(rf'{category}_log.txt', 'a', encoding='UTF-8')
dateStr = time.strftime('%d.%m.%Y')
timeStr = time.strftime('%H:%M:%S')
log.write(
    f'Validierung am {dateStr} um {timeStr} Uhr:\n\
    Fehler: {errorCount}\n\
    Richtig: {fileCount - errorCount}\n\
    Gesamt: {fileCount}\n\
    Fehlerquote: {errorRate}%\n\
    \n')
log.close()
# Zweiter Teil:
# Alle fehlerhaften Profile koennen optional geloescht werden


def delete_faulty_jsons():
    """This function deletes JSONs if they're on the errorList.cvs"""
    deleteCounter = 0
    with open(rf'{category} errorList.csv', encoding='UTF-8') as file:
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
