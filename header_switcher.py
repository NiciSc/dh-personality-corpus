import csv
import random

class header_switcher:
    def __init__(self):
        self.headersList = []
        databaseFilename = r'resources/user-agent-database.csv'
        with open(databaseFilename, 'r') as file:
            databaseCSV = csv.DictReader(file)
            for line in databaseCSV:
                #self.headersList.append({'User-Agent':line['user_agent']})
                self.headersList.append(line['user_agent'])
                #self.headersList.append({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'api.personality-database.com','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'cross-site','Sec-Fetch-User':'?1','TE':'trailers','Upgrade-Insecure-Requests':'1','User-Agent':line['user_agent'],})

    def switch(self):
        random.shuffle(self.headersList)
        return self.headersList.pop()