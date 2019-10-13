#python3.6
#CEP 12AUG18
#This script will curate sanger sequences based on phred scores for nucleotides.
#It expects .qual file (contains phred scores) and .seq files in the same directory.
# .qual and .seq files should have matching names
#give the path starting and ending with /
#the minimal score it asks for is the expected length (number) of continuous nucleotides that had a pred of 20 or higher
#phred score of 20 means 99% base accuracy
#tests if .qual has the same or higher nr of continuous set of bases>20 compared to the given minimal input score
#the script will copy the associated .seq files that match to this rule to a new "curated_sequences" directory

#we need os, re and shutil

import os
import re
import shutil

#specify the path
path = input('please provide the path to the directory with .qual and .seq files (/Users/Bentley/example/):')

#first we need to get all the .qual files in a list
#make a file list from everything in the specified path
filelist = os.listdir(path)
#print(filelist)

#make a list of .qual files only
qualfilelist=[]
#find all files that end with .qual in the filelist, reg exp works on strings so iterated through that list!
for file in filelist:
    qualfilelist += re.findall('.*\.qual$',file)
#print(qualfilelist)

#start a dictionary to contain the qual data associated with the sequence name, which is also the file name
qual_dictionary = {}

#iterate through the qualfilelist and populate the qual_dictionary

for file in qualfilelist:
    # open a qual file that contains quality of basecalling
    f = open(path+file, 'r')
    qual_lines = f.readlines()
    f.close()
    #clean up filename using re
    rematch = re.match(r'(.+)(?:\.qual)', file)
    newfilename = rematch.group(1)
    #add filename to the dictionary and start phred subdir
    qual_dictionary[newfilename] = {'phred': ''}

    # iterate through the lines to populate the qual_dictionary with name as key and phredval as a string of values
    for line in qual_lines:
        #omit lines with a title which should always start with >
        if line[0] != '>':
            # append the phred data to the dictionary, always start with a space to prevent concatenating lines
            qual_dictionary[newfilename]['phred'] += ' ' + line.strip()


#the qual values are now a giant string. cnvert to a list of phred scores so it can be easily manipulated
#use a regular expression to find the numbers between the spaces \d+ is any digit plus any recurring digit so decades
#are picked up too
for sequence in qual_dictionary:
    phredlist = re.findall('\d+',qual_dictionary[sequence]['phred'])

    #iterate through the list to convert to integers
    phredlist = [int(i) for i in phredlist]
    qual_dictionary[sequence]['phred'] = phredlist

#for key1,key2 in qual_dictionary.items():
#    print(key1, '\n' ,key2)

#function to caldulate the quality score (number of consequtive nucs with phred=>20)
def calculateScore(phredlist):
    goodvalcount = 0
    highscore = 0
    for num in phredlist:
        # see if the number is 20 or higher, if so add to the good value counter
        if num >= 20:
            goodvalcount += 1
            # test if we got a new high score, if so pass it to the highscore variable. now we can continue looking
            if goodvalcount > highscore:
                highscore = goodvalcount
        # reset the goodvalcounter if we find a crappy value, highscore is saved
        else:
            goodvalcount = 0
    return highscore

#start iterating through the sequences and score based on the value under 'phred'. add score key to the dictionary
for sequence_name in qual_dictionary:
    #add qualscore to each dictionary, fill it with the result from the calculate score function
    qual_dictionary[sequence_name]["qualscore"]= calculateScore(qual_dictionary[sequence_name]['phred'])
    #print(qual_dictionary[sequence_name]["qualscore"])

#now that we have a dictionary with the phred score, we are going to test if its high enough and if ok,
# move the associated .seq file to a new folder
#function to create a folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#function to copy files
def copyFile(source, target):
    try:
        shutil.copy(source, target)
        print("copying: "+source +"to "+target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())



#use the createfolder function above to create a directory in the given path
curatedSeqPath = path+'curated_sequences'
createFolder(curatedSeqPath)

#now ask user for the minimal score, then test against that and copy .seq files with score or higher score
# to the new directory using the copyFile function

while True:
    try:
        minimalscore = int(input("please provide minimal length nucleotides>phred20:"))
        break
    except:
        print('score must be an integer! Try again')


for sequencekey in qual_dictionary:
    if qual_dictionary[sequencekey]['qualscore']>=minimalscore:
        source = path+sequencekey+'.seq'
        print('passed! '+ sequencekey + ' score: ' + str(qual_dictionary[sequencekey]['qualscore']))
        target = curatedSeqPath+'/'+sequencekey+'.seq'
        copyFile(source, target)
    else:
        print("not passed: " + sequencekey + ' score: ' + str(qual_dictionary[sequencekey]['qualscore']))

print("DONE!")
