#!/usr/bin/env python3

import cgi
import pickle

# Set the content type to HTML
print("Content-Type: text/html\n\n")
def get_date_or_year(option):
    now = datetime.datetime.now()

    if option == 'datetime':
        return now.strftime('%Y-%m-%d %H:%M:%S')
    elif option == 'year':
        return now.year
    else:
        return "Invalid option. Please choose either 'datetime' or 'year'."

# Retrieve the form data
form = cgi.FieldStorage()

# Get the value from the 'name' field of the form
text = form.getvalue('post-text')
usrname = form.getvalue('post-usrname')
datetime = form.getvalue(get_date_or_year("datetime"))

# Create a dictionary to store the data
new_data = [text, usrname, datetime]

# Specify the path for the pickle file
file_path = 'data.pickle'

# Dump the data to the pickle file
try:
    with open(file_path, 'rb') as file:
        existing_data = pickle.load(file)

    combined_data = existing_data + list(new_data)

    with open(file_path, 'wb') as file:
        pickle.dump(combined_data, file)

    print("Data appended to pickle file successfully:", file_path)
except FileNotFoundError:
    print("Existing file not found:", file_path)
except Exception as e:
    print("An error occurred while appending data to pickle file:", str(e))
