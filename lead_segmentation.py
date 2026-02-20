import csv

"""
    Reads a CSV file of company/contact data,
    validates required fields,
    groups contacts into leads by company,
    and writes a structured output file.
"""

def segment_leads(input_file, output_file):
    
    total_rows = 0              # Tracks total rows processed
    invalid_data = 0            # Tracks number of invalid rows discarded
    invalid_data_table = []     # Stores invalid rows for potential logging
    cleaned_table = []          # Stores validated rows

    leads = {}                  # Dictionary to group contacts by company name

    # Required fields necessary to create new output_file
    required_fields = ["Company", "Contact Name", "custom.Company Revenue", "Company US State"]

     # Open and read input CSV file
    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)

        # Iterate through each row in the CSV
        for row in reader:
                total_rows += 1

                # Validate required fields (must exist and not be empty)
                if any(not row[field] or row[field].strip() == "" for field in  required_fields):
                    invalid_data += 1
                    invalid_data_table.append(row)
                    continue

                # Read email value in csv
                email = row.get("Contact Emails")

                # Validate email format (basic validation)
                if not email or "@" not in email or email.strip() == "":
                    invalid_data_table.append(row)
                    invalid_data += 1
                    continue

                # Row is valid, extract and normalize key fields
                else :
                    contacts = row["Company"].strip() 
                    state = row["Company US State"].strip()
                    revenue = float(row["custom.Company Revenue"])

                    #  # Group this contact under its company (lead)
                    if contacts not in leads:
                        leads[contacts] = []

                    # Add row to new table
                    leads[contacts].append(row)

                    # Store valid rows
                    cleaned_table.append(row)

        

          # Write the state-level summary report
        with open(output_file, "w", newline="") as f:
            fieldnames=["US State", "Total Number of leads", 
                        "The lead with the most revenue", 
                        "Total revenue", "Median Revenue"]
            write = csv.DictWriter(f, fieldnames=fieldnames)
            write.writeheader()
            write.writerows() # replace with new revenue and state table

     
    # Print summary for debugging/testing
    #print("Total rows counted:", total_rows)
    #print("Total invalid rows:", invalid_data)
    #print(leads[contacts])

# Main function to run 
def main():

    segment_leads("company_leads.csv", "output_file.csv")

    
if __name__ == "__main__":
    main()
