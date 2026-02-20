Project Overview :
    This project uses a Python script to import contact data from a csv file using the Close API, then prints out a new state-revenue contact csv file.

Script Explained :
- Reads CSV file
- Validates each contact, verifying no missing or formatted data
- Read through each row keeping count of all rows read
- Discard into discard table, any rows with empty or misformatted data
- Validate email format for cleaned csv
- Extract and normalize the key fields for output file
- Group contacts into leads by company name

Simple explanation (Non technical) :
- Open csv file or comma separated values file (spreasheet format)
- Read row by row
- Verify all necessary data is in row to add to final array
- Group contacts together by leads
- Write new csv file with new columns grouping by State and Revenue values

Eliminating invalid data :
- I tested each row of data to see if there was anything missing from the necessary columns (Company, Contact Name, Contact Emails, custom.Company Revenue, Company US State) and if there were any values missing than I discarded by adding to the invalid_data_table and invalid_data count.

Find all leads :
- I found all the leads by making sure I read through each row in the csv and placed the row in one of two tables. Either invalid_data_table or cleaned_table so that I didn't lose any of it in case there was an error in the reading of data.

Segmenting leads by state and find most revenue :
- I didn't get to this part because i ran out of time but I would have grouped the leads dictionary by state the same way I grouped contacts by company, then calculated total leads, highest revenue lead, total revenue, and median revenue per state.

Dependencies :
- I have a requirements.txt with requests for the API usage but it is currently unused because I was unable to get to it, otherwise there aren't many other dependencies needed

Thinking Along the Way :
Assumptions :
- One company = One lead
- Revenue values are just numbers
- Only emails matter, not phone numbers
- Email only needs a value with an @ symbol to be considered valid
- Every contact has a company

Tradeoffs :
- To complete the project in order and not skip around as much
- Resulting in the first part being mroe compelted than the last part and in one function rather than multiple functions
- Very simplistic validation requirements rather than more complex ones

Future Improvements with more time :
- Post a lead to Close API
- Get the leads using a date filter in the query for the users speific date request
- Group the leads together by state the same way I did the contacts by lead
- Add function that involves tracking the total number of leads, the highest revenue lead, total revenue of all leads per state, and a formula for the median revenue fro the state
- Place API key in .env file to keep it safe
- Separate these code blocks into separate functions to clean up look and simplify
- Rewrite logic for finding leads that were founded between certain dates
- In depth testing 
- More robust validation code for incoming data
- Replace one long function with more small functions to make for easier troubleshooting

