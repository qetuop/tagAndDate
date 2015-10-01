# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "brian"
__date__ = "$Sep 30, 2015 8:06:34 PM$"

def createTagDateDict(tdfLines):
    tdfDict = {}
    
    for line in tdfLines:
        tmp = line.split(',')
        if ( tmp[0].isdigit() ):
            try:
                tdfDict[tmp[0]] = tmp[1].strip()
            except:
                print('this line is messed up %s', line)
                
    return tdfDict

def mergeData(tagDatesFile, tagInfoFile, mergedFile):
    tdfLines = tagDatesFile.readlines()
    tifLines = tagInfoFile.readlines()
    
    # create dictionary of tag:date
    tdfDict = createTagDateDict(tdfLines)
    #print(tdfDict)
    
    # loop through Info and search for tags
    foundTags = []
    for line in tifLines:
        tmp = line.split(',')
        
        if ( tmp[0] in tdfDict.keys() ):
            print('%s has a date of %s' %(tmp[0], tdfDict[tmp[0]]))
            
            # write to merged file
            print(tmp[:-1])
            mergedFile.write('%s,%s\n'%(','.join(tmp[:-1]), tdfDict[tmp[0]]) )
            
            # save for below
            foundTags.append(tmp[0])
        else:
            print('%s was not found in the Dates file' %tmp[0] )
            mergedFile.write('%s'%(','.join(tmp[:]) ) )
    
    # print tags that have dates but no info
    s1 = set(tdfDict.keys())
    s2 = set(foundTags)
    
    print('These tags are not in the Info file: %s' %(s1.difference(s2)) ) 

if __name__ == "__main__":
    tdf = open('tagDates.txt')
    tif = open('tagInfo.txt')
    mergedFile = open('mergedFile.csv', 'w')
    
    mergedFile.write(tif.readline()) # get the first line info
    
    mergeData(tdf, tif, mergedFile)