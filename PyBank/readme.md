![A boss knuckle image](revenue-per-lead.png)

# PyBank Financial Analysis - Coding Solution 
The included python script provides a coding solution to analyze a Bank's Profit and Loss position on a month over month basis.

### General Approach
The solution relies on the use of the **os** and **csv** modules to import a .csv file from a specified path. The imported data is loaded into a list array and processed to analyze:<br/>

1.  Determine the number of Periods included in the analysis
2.  Month over Month Variance in the posted Profit / Loss value
3.  Month showing the Highest Increase in Profit / Loss value
4.  Month showing the Highest Decrease in Profit / Loss value
5.  The Average Variance for Profit / Loss value
6.  Overall Total for the Profit / Loss value


### PseudoCode
The following is the key steps taken to implement the coding solution:
using the imported modules: <br/>
* set path for source file
* open source files as readonly, and instantiate a reader object
* skip the header row
* loop through the remaining records and append to the budget list array we created 
#### Process Delta / Variance
* populate a list array structure with deltas 
* create a function to calculate the average profit/ loss change between periods
* create a function to return the month / period associated with a given variance
* create a function used to return both the greatest increase and decrease 
#### Generate Results
* call functions to assign variables 
* print summary with the results
* open a new text file with "write" mode.
* write the results to the text file
#### Clean-Up
* make sure the file we wrote to is closed when when we are done.