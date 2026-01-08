# Name: Nicolle Cuterez
# Class: CSC110 - Spring 2024
# Assignment: Programming Project Implementation
# Due Date: April 29, 2024

# Project Tite: TV Show Data


# Project Description:
# --------------------
# This program will read a TV Show Data file and allow the user to choose from a list of options
# (1-7) about the TV shows. The program will then respond with the results of the chosen choice.
# Using the file the program will continue for as long as wanted until the user chooses to quit.

# General Solutions:
# -------------------
# Enter the file name. Open, read file and use it to run through the program. Keep empty lists
# to store file data. Present the users with a set of 7 options. The user chooses and option.
# The program runs the function for that input. Displays it to the user. When the user chooses 7,
#the program is quit.


# Pseudocode:
# -----------------
# User enters data file
# Display options user can choose from
# If user inputs 1
#       Program displays all shows with a certain rating
# If user inputs 2
#       Program finds the show with the highest score released in a speciied range of years
# If user inputs 3
#       Program searches for show by title
# If user inputs 4
#       Programs finds the average score for films with a specific rating
# If user inputs 5
#       Program finds all shows with a score higher than the score for a given show
# If user inputs 6
#       Program sorts all lists by year and writes results to a new file
# If user inputs 7
#       Program quits
#       prints("Good-bye")

# Function Design:
# --------------------------------------------------------------------------------------

# Function takes file name and prompts the user to input another name if invalid
# Takes no parameters
# Returns inFile(file being opened)
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter the name of the data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name - try again")
            
    return inFile

# Function reads and gets the data from the file
# Takes no parameters
# Returns 4 lists from the users (title, rating, year, & score)
def getData():
    inFile = openFile()
    titleList = []
    ratingList = []
    yearList = []
    scoreList = []
    line = inFile.readline()
    for line in inFile:
        line = line.strip()
        title, rating, year, score = line.split(',')
        title = str(title)
        rating = str(rating)
        year = int(year)
        score = int(score)
        titleList.append(title)
        ratingList.append(rating)
        yearList.append(year)
        scoreList.append(score)
    inFile.close()

    return titleList, ratingList, yearList, scoreList

# Function gets the users choice input while prompting the user to re-enter the value
# if not within options range or an integer
# Takes no parameters
# Returns valid choice
def getChoice():
    print("Please choose one of the following options:")
    print("1 -- Find all shows with a certain rating")
    print("2 -- Find the show with the highest score released in a specified range of years")
    print("3 -- Search for a show by title")
    print("4 -- Find the average score for films with a specific rating")
    print("5 -- Find all shows with a score higher than the score for a given show")
    print("6 -- Sort all lists by year and write results to a new file")
    print("7 -- Quit")
    OK = False
    while OK == False:
        try:
            choice = int(input("Choice ==> " ))
            if choice >= 1 and choice <= 7:
                OK = True
            else:
                print("Invalid entry - try again ")
        except ValueError:
            print("Invalid entry - try again ")      
    return choice

#---------------------------------------------------------------------------------------
# START OF CHOICE 1

# Function gets a passing rating that the program will use to find the shows with
# that rating & makes sure a valid input is used by running the user rating in the
# ratingList
# Takes ratingList as a parameter to use in comparison
# Returns the rating input
def getPassingRatingThreshold(ratingList):
    OK = False
    while OK == False:
        try:
            rating = str(input("Enter rating:"))
            
            if rating in ratingList:
                OK = True
            else:
                print("Invalid entry - try again")
        except ValueError:
            print("Invalid entry - try again")
    return rating

# Function gets the index of the ratings that match the rating input by going thru a loop
# thru the ratingList and stores the index to it when a match is found to later use to 
# print their titles, years, and score 
# Takes user rating and ratingList as parameters
# Returns the indexes of matches
def searchRatings(rating, ratingList):
    foundIndex = []
    found = 0
    i = 0
    while i < len(ratingList):
        if ratingList[i] == rating:
            found = 1
            foundIndex.append(i)
        i = i + 1
    return foundIndex

# END OF CHOICE 1
#---------------------------------------------------------------------------------------
# START OF CHOICE 2

# Function get the range of years that the user wants to find the highest score released
# in input range & will check for a valid year entry ensuring to prompt the user until
# valid entry is used for both years. The exception accounts for non integers, values
# outside yearList range and for cases where year2 is not greater than year 1 (is older)
# and prompt the user to re-enter both years in order of older year first 
# Takes no parameters
# Returns valid year1 and valid year2
def getPassingYear():
    print("Enter year range to search (oldest year first)")
    OK = False
    while OK == False:
        try:
            year1 = int(input("Year1: "))
            if year1 >= 1990 and year1 <=2017:
                OK = True
            else:
                 print("Invalid year - try again")
        except ValueError:
            print("Invalid entry - try again")
            
    OK = False
    while OK == False:
        try:
            year2 = int(input("Year2: "))
            if year2 >= 1990 and year2 <=2017:
                if year2 > year1:
                    OK = True
                else:
                    print("Second year should be after first year - try again")
                    year1 = int(input("Year1: "))
            else:
                print("Invalid year - try again")
                
        except ValueError:
            print("Invalid entry - try again")     
    return year1, year2

# Function finds the years that fall in the valid years range by going thru the yearList
# and saves their indexes when the year is equal to or between year1 and year2 to use
# later to find their corresponding scores
# Takes parameters of year1, year2, and yearList
# Returns index of the years from the file in the range of year1 and year2
def getYearsinRange(year1, year2, yearList):
    yearFoundIndex = []
    found = 0
    i = 0
    while i < len(yearList):
        if yearList[i] >= year1 and yearList[i] <= year2:
            found = 1
            yearFoundIndex.append(i)
        i = i + 1
    return yearFoundIndex

# Function compares the years that fell between year1 and year2 by using their index to
# find their scores then comparing them to find the highest one and save that index
# to later print the score and its matching title, rating and year.
# Takes parameters of yearFoundIndex and scoreList
# Returns the index of the highest scoring title
def getHighestScore(yearFoundIndex, scoreList):
    highestScore = 0
    highestIndex = 0
    for i in range (len(yearFoundIndex)):
        if scoreList[yearFoundIndex[i]] > highestScore:
            highestScore = scoreList[yearFoundIndex[i]]
            highestScoreIndex = yearFoundIndex[i]
    return highestScoreIndex

# END OF CHOICE 2
#---------------------------------------------------------------------------------------
# START OF CHOICE 3

# I emailed TA claudia and she recommended .title()
# Function finds a passing title where it can be matched regardless of case by creating a
# new stored title and if no show meets the criteria rather than ask for a new title it 
# asks the user to select from options again
# Takes titleList as parameter
# returns the title 
def getPassingTitle(titleList):
    OK = False
    while OK == False:

        title = str(input("Enter show title: "))
        newTitle = title.title()
        if newTitle in titleList:
            OK = True
        else:
            print("No shows meet your criteria")
            choice = getChoice()
    return newTitle

# Function takes the the title, finds its index and stores it to later print
# its title, rating, year, and score
# Takes parameters of the title and titleList
# Returns the index of the show
def searchTitleIndex(newTitle, titleList):
    showFoundIndex = []
    found = 0
    i = 0
    while i < len(titleList) and found == 0:
        if titleList[i] == newTitle:
            found = 1
            showFoundIndex = i
        i = i + 1
    return showFoundIndex

# END OF CHOICE 3
#---------------------------------------------------------------------------------------
#START OF ADDITIONAL CODE FOR CHOICE 4

# Runs pre-existing function in main: rating = getPassingRatingThreshold(ratingList)
# to get a valid rating from the user 
# Runs pre-existing function in main: foundIndex = searchRatings(rating, ratingList)
# to store the indexes of ratings that match the input 

# Function takes the index of the ratings matching input rating and uses it to get its
# corresponding score, then adds it to the totalScore thats initliazed at 0 and loops
# through the length of indexes in foundIndex to add all the scores with that rating
# after adding all it then computes the average score of all shows with that rating and
# gets the result to be used later when results are printed
# Takes parameters of foundIndex and scoreList
# Returns the average
def averageScoreofShows(foundIndex, scoreList):
    totalscore = 0
    for i in range (len(foundIndex)):
        totalscore = totalscore + scoreList[foundIndex[i]]
    average = totalscore/len(foundIndex)
    return average

# END OF CHOICE 4
# --------------------------------------------------------------------------------------
# START OF CHOICE 5

# Function gets a valid title from the user using exception handling, if the entry is
# invalid the user is asked to enter another title until the title is found in titleList
# Takes parameter of titleList
# Returns the title
def getTitle(titleList):
    OK = False
    while OK == False:
        try:
            title = str(input("Enter title:"))
            if title in titleList:
                OK = True
            else:
                print("Invalid entry - try again")
        except ValueError:
            print("Invalid entry - try again")
    return title

# Runs pre-existing function in main: showFoundIndex = searchTitleIndex(title, titleList)
# to find the index of the title and storing it


# Function helps find the shows with higher scores than the title entry, so it uses the
# foundIndex to get the titles score and then compare the rest of the scoreList, storing
# those with higher scores however if the len of the list is empty it prints that there
# are no shows
# Takes parameters of showFoundIndex and scoreList
# Returns the index of the higher scores
def greaterScoresIndex(showFoundIndex, scoreList):
    higherScoresIndex = []
    for i in range(len(scoreList)):
        if scoreList[showFoundIndex]< scoreList[i]:
            found = 1
            higherScoresIndex.append(i)

    if len(higherScoresIndex) == 0:
        print("No shows meet your criteria")
        
    return higherScoresIndex


# END OF CHOICE 5
# --------------------------------------------------------------------------------------
# START OF CHOICE 6

# I refrenced homework 6 to modify for this function
# Function sorts the data starting from oldest year in ascending order
# Takes parameters of yearList
# Returns the indexList of the sorteed years

def sortData(yearList):
    indexList = list(range(0,len(yearList)))
    newList = yearList.copy()
    
    for i in range(0,len(indexList)):
        min = i
        for j in range(1+i, len(indexList)):
            # comparison
            if newList[min] > newList[j]:
                min = j
        # swap
        newList[i],newList[min] = newList[min],newList[i]      
        indexList[i],indexList[min] = indexList[min],indexList[i]
              
    return indexList
            

#END OF CHOICE 6
# -------------------------------------------------------------------------------------

#These functions pull the results/index/info calculation from other functions and prints
# the results to the corresponding actions

def printResults1(foundIndex,titleList, ratingList, yearList, scoreList):
    print("\nThe TV shows that meet your criteria are:\n")
    print("TITLE".ljust(40), "RATING".ljust(8), "YEAR".ljust(5), "SCORE".ljust(4))
    for i in range(len(foundIndex)):
        print(titleList[foundIndex[i]].ljust(40),ratingList[foundIndex[i]].ljust(8),str(yearList[foundIndex[i]]).ljust(5),str(scoreList[foundIndex[i]]).ljust(4))
        # END OF CHOICE 1 RESULTS

def printResults2(highestScoreIndex,titleList, ratingList, yearList, scoreList):
    print("The TV shows that meet your criteria are:")
    print("TITLE".ljust(40), "RATING".ljust(8), "YEAR".ljust(5), "SCORE".ljust(4))
    print(titleList[highestScoreIndex].ljust(40),ratingList[highestScoreIndex].ljust(8),str(yearList[highestScoreIndex]).ljust(5),str(scoreList[highestScoreIndex]).ljust(4))
        # END OF CHOICE 2 RESULTS


def printResults3(showFoundIndex, titleList, ratingList, yearList, scoreList):
    print("The TV shows that meet your criteria are:")
    print("TITLE".ljust(40), "RATING".ljust(8), "YEAR".ljust(5), "SCORE".ljust(4))
    print(titleList[showFoundIndex].ljust(40),ratingList[showFoundIndex].ljust(8),str(yearList[showFoundIndex]).ljust(5),str(scoreList[showFoundIndex]).ljust(4))
        # END OF CHOICE 3 RESULTS

def printResults4(rating, average):
    print("The average score for shows with a ", rating, "rating is " "{:.2f}".format(average))
        # END OF CHOICE 4 RESULTS


def printResults5(higherScoresIndex, titleList, ratingList, yearList, scoreList):
    if (len(higherScoresIndex)) > 0:
        print("The TV shows that meet your criteria are:")
        print("TITLE".ljust(40), "RATING".ljust(8), "YEAR".ljust(5), "SCORE".ljust(4))
        for i in range(len(higherScoresIndex)):
            print(titleList[higherScoresIndex[i]].ljust(40),ratingList[higherScoresIndex[i]].ljust(8),str(yearList[higherScoresIndex[i]]).ljust(5),str(scoreList[higherScoresIndex[i]]).ljust(4))
        # END OF CHOICE 5 RESULTS


def printResults6(indexList, titleList, ratingList, yearList, scoreList):
    outname = ("year-sorted-shows.csv")
    outFile = open(outname, 'w')
    outFile.write('Title,Rating,Year,Score\n')
    for i in range(len(indexList)):
        ind = indexList[i]
        outFile.write(str(titleList[ind]) + ',' + str(ratingList[ind]) + ',' + str(yearList[ind]) + ',' + str(scoreList[ind])+ '\n')
    outFile.close()
    print("Data sorted by years written to file", outname)
        # END OF CHOICE 6 RESULTS


#--------------------------------------------------------------------------------------
# Function runs the loop for the options so that when the user chooses the program executes
# the corresponding instruction and when 7 is entered it ends the loop and program
def main():
    titleList, ratingList, yearList, scoreList = getData()
    choice = getChoice()
    while choice != 7:
        if choice == 1:
            rating = getPassingRatingThreshold(ratingList)
            foundIndex = searchRatings(rating, ratingList)
            printResults1(foundIndex,titleList, ratingList, yearList, scoreList)
        elif choice == 2:
            year1, year2 = getPassingYear()
            yearFoundIndex = getYearsinRange(year1, year2, yearList)
            highestScoreIndex = getHighestScore(yearFoundIndex, scoreList)
            printResults2(highestScoreIndex,titleList, ratingList, yearList, scoreList)
        elif choice == 3:
            newTitle = getPassingTitle(titleList)
            showFoundIndex = searchTitleIndex(newTitle, titleList)
            printResults3(showFoundIndex, titleList, ratingList, yearList, scoreList)
        elif choice == 4:
            rating = getPassingRatingThreshold(ratingList)
            foundIndex = searchRatings(rating, ratingList)
            average = averageScoreofShows(foundIndex, scoreList)
            printResults4(rating, average)
        elif choice == 5:
            title = getTitle(titleList)
            showFoundIndex = searchTitleIndex(title, titleList)
            higherScoresIndex = greaterScoresIndex(showFoundIndex, scoreList)
            printResults5(higherScoresIndex, titleList, ratingList, yearList, scoreList)
        elif choice == 6:
            indexList = sortData(yearList)
            printResults6(indexList, titleList, ratingList, yearList, scoreList)
            
        # loops program back to option selection after actions are completed unless 7 is
        # entered    
        choice = getChoice()

    print("Good-bye")
        

