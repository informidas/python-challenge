![A boss knuckle image](boss.jpg)
# PyBoss HR Solution

## Overview
The included script provides a solution to ingest a csv file into a list array structure and process the file to generate cahnges to the structure of the data. <br/><br/>

In summary, the required conversions to the csv input file are as follows: <br/>

* The Name column should be split into separate First Name and Last Name columns.

* The DOB data should be re-written into MM/DD/YYYY format.

* The SSN data should be re-written such that the first five numbers are hidden from view.

* The State data should be re-written as simple two-letter abbreviations.

## Approach
--
### General
My approach to developing a solution was to create some utility functions that could perform each of the requisite data transformations. This allows us to bring in the source csv in its original format and apply the transformations on the output csv file generated as a last step in the code.<br/>

*** Modules and Libraries used
In addition to using the base python modules and libraries, I imported the **os** and **csv** modules to resolve building a file path in a platform independent manner as well as reading and processing the source csv file.<br/>

### Pseudo Code

* import needed packages
* get a list of states and state abbreviations
* create a function that splits name into first name / last name
* create a function that converts DOB into new format
* create a function that masks first 5 characters of SSN

#### Process Employee csv file
* declare a list array that will contain the employee data to be ingested
* define the path and open the csv file using a reader object
* skip the header row
* append the data to our employee list structure
* open a new csv file with "write" mode to generate new format for employees data.
* write the header row to the file
* looping through the data - apply formatting using the functions we created
* close the file once we are done writing to it