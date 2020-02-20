![linguist master](language.png)
# PyParagraph Solution

The included script provides a solution to ingest a .txt file into a string variable and process the file to analyze key meta data about the document. <br/><br/>

In summary, the  follow statistics are needed about the txt file: <br/>

* An approximation of the Word Count for the ingested file.

* An approximation of the sentence count in the ingested file.

* An approximation of the average Letter Count.

* An Approximation of the average length of each sentence.

## Approach

### Modules and Libraries used
In addition to using the base python modules and libraries, I imported the **os**,**csv** and **re** modules to resolve building a file path in a platform independent manner as well as reading and processing the source txt file.<br/>

### Pseudo Code

* declare a list array for the tokenized paragraph
* declare a list array for the tokenized sentences
* declare a string variable for the clean paragraph
* set path for source file
* open source files as readonly, and instantiate a reader object
* load the sentences into the clean_paragraph String
* once we have paragraph loaded as text, determine the number of words per sentence
* initialize a counter for each character in the clean text string
* initialize a counter for numbe rof words
* loop through the clean_paragraph string letter by letter
* if we hit a space then we found another word so add 1 to the word count total
* we hit a period then it means the sentence is done, so append the word count total to a 
* reset the wordc count 
* use the regular expressions module to tokenize the paragraph into an array of words
* create and set variables needed for stats in results summary
* Print Results
