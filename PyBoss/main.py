# import packages
import os, csv, datetime

#list of states and state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

 
# function that splits name into first name / last name
def parseName(fullname):
  name_tokens = fullname.split(' ')
  return name_tokens

# function that converts DOB into new format
def convertDOBFormat(dob):
  dob_tokens = dob.split('-')
  return dob_tokens[1] + '/' + dob_tokens[2] + '/' + dob_tokens[0]

# function that masks first 5 characters of SSN
def maskSSN(ssn):
  masked_ssn = '***-**' + ssn[6:]
  return masked_ssn

# declare a list array that will contain the employee data to be ingested
employees = []

# define the path and open the csv file using a reader object
csvpath = os.path.join("data", "employee_data.csv")

with open(csvpath, 'r', newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  # skip the header row
  next(csvreader)

  # append the data to our employee list structure
  for row in csvreader:
    employees.append(row)

# open a new csv file with "write" mode to generate new format for employees data.
file = open("results\\employees.csv", "w")

# write the header row to the file
file.write(f"Emp ID,First Name,Last Name,DOB,SSN,State\n")

# looping through the data - apply formatting using the functions we created
for row in employees:
  first_name = parseName(row[1])[0]
  last_name = parseName(row[1])[1]
  file.write(f"{row[0]},{first_name},{last_name},{convertDOBFormat(row[2])}, {maskSSN(row[3])}, {us_state_abbrev[row[4]]}\n")

# close the file once we have done writing to it
file.close()
