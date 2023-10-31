# Import the necessary libraries
import datetime

# Define the input and output file names
input_file = "People-1.txt"
output_file = "userpass.txt"

# Initialize an empty list to store user data
user_data = []

# Function to calculate the year of birth
def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    return birth_year

# Function to generate email address
def generate_email(first_name, last_name):
    first_initial = first_name[0].lower()
    email = f"{first_initial}{last_name.lower()}@TCX.au"
    return email

# Function to generate password
def generate_password(first_name, last_name, age):
    first_name_lower = first_name.lower()
    last_name_upper = last_name[0].upper()
    birth_year = calculate_birth_year(age)
    password = f"{first_name_lower}{last_name_upper}_{birth_year}"
    return password

# Read data from the input file and process it
with open(input_file, "r") as file:
    for line in file:
        # Split each line of the input file into first name, last name, and age using the '|' delimiter
        first_name, last_name, age = line.strip().split('|')
        # Generate an email address by taking the first initial of the first name, making it lowercase, and appending the last name in lowercase
        email = generate_email(first_name, last_name)
        # Generate a password by converting the first name to lowercase, taking the first character of the last name and making it uppercase, and appending the birth year (calculated using the calculate_birth_year function)
        password = generate_password(first_name, last_name, int(age))  # age is converted to an integer
        # Append the email and password to the user_data list as a tuple
        user_data.append((email, password))

# Write user data to the output file
with open(output_file, "w") as file:
    for email, password in user_data:
        # Write each user's email and password to the output file in the specified format
        file.write(f"{email} | {password}\n")
