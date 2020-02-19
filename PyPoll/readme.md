![A boss knuckle image](Vote_counting.png)

# PyPoll Voting Results - Coding Solution 
The included python script provides a coding solution to analyze the results of an election. Voters cast votes for one of four candidates. The script provides a mechanism to determine the winner whom received the most votes of all teh candidates.

### General Approach
The solution relies on the use of the **os** and **csv** modules to import a .csv file from a specified path. The imported data is loaded into a list array and processed to analyze and provide:<br/>

1.  Overall number of votes casted in teh election
2.  Number of votes received by each candidate
3.  The percentage of overall votes received by the candidate
4.  The ranked order (Highest to Lowest) to determine the order results should be posted
5.  Posting of the results on screen with formatting to improve readability of the results 
6.  A declaration of the winner
7.  Text file capturing the summary results which contain the same format as displayed on screen

### PseudoCode
The following is the key steps taken to implement the coding solution:
using the imported modules: <br/>
* set path for source file
* open source files as readonly, and instantiate a reader object
* skip the header row
#### Process Votes
* loop through the remaining records and calculate overall votes and votes per candidate
* write the results to a dictionary array
* sort the array in descending order to get ranking (most votes, second most votes etc.)
* get the percentages for each candidate
* format the results to get the approrpiate display (i.e. decimal places and display format)
#### Generate Results
* open a new text file with "write" mode to write Election Results.
* populate variables and generate election results
* print formatted summary of the election results
* write the formatted summary of results to the Election Results text file
#### Clean-Up
* make sure to close the file we are writing the Election Results
