#Jessica Ennis
#Lab 8

#Sources: tutorialspoint.com/python/os_walk.htm
#nitratine.net/blog/post/how-to-hash-files-in-python
#pythontutorial.net/python-basics/python-write-csv-file/
#intellipaat.com/community/3770/how-to-get-file-creation-modification-date-times-in-python

import os
import hashlib
import csv
import os.path, time

csvList = []

BLOCK_SIZE = 65536
unhashable = ['/dev','/proc','/run','/sys','/tmp','/var/lib', '/var/run']
fHash = hashlib.sha256()

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if name in unhashable:
            continue
        else:
            file = os.path.join(root,name)
    for name in files:
        if name in unhashable:
            continue
        else:
            file = os.path.join(root,name)
            try:
                with open(file, "rb") as f:
                    csvList.append(file)
                    fBytes = f.read(BLOCK_SIZE)
                    while len(fBytes) > 0:
                        fHash.update(fBytes)
                        fBytes = f.read(BLOCK_SIZE)
                csvList.append(fHash.hexdigest())
                csvList.append(time.ctime(os.path.getmtime(file)))
                
                with open('hashList.csv', 'w', encoding='UTF8') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(csvList)
            except:
                file.close()
                continue


