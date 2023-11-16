# this simple script will convert cbr comic files into a cbz files. There is no quality loss in the file images during the conversion. This script doesn't remove copy protection. 
# You will need to create two new folders, 'input' and 'output' or change the variables below.

# The script needs this to function: patoolib

import patoolib, os, time

inputPath = 'input'
outputPath = 'output'

for comic in os.listdir(inputPath):

    cSplit = os.path.splitext(comic)
    
    if cSplit[1].lower() != '.cbr':
        print(comic + ' is not a cbr file, skipping.')
        time.sleep(1)
        continue

    zipComic = cSplit[0] + '.zip'
    cbzComic = cSplit[0] + '.cbz'

    patoolib.repack_archive(os.path.join(inputPath, comic), os.path.join(outputPath, zipComic))

    os.rename(os.path.join(outputPath, zipComic), os.path.join(outputPath, cbzComic))
