#!/usr/bin/python3

import pickle
import datetime

# Import modules for CGI handling 
import cgi, cgitb 


def get_date_or_year(option):
    now = datetime.datetime.now()

    if option == 'datetime':
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        return str(now.strftime('%Y-%m-%d %H:%M:%S'))
    elif option == 'year':
        return str(now.year)
    else:
        return "Invalid option. Please choose either 'datetime' or 'year'."

def store_data():

    text = form.getvalue('post-text')
    usrname = form.getvalue('post-usrname')
    datetime = get_date_or_year("datetime")
    
    new_data = [text, usrname, datetime]
    
    # Specify the path for the pickle file
    file_path = 'data.pickle'

    # Dump the data to the pickle file
    try:
        with open(file_path, 'rb') as file:
            existing_data = pickle.load(file)

        existing_data.append(new_data)

        with open(file_path, 'wb') as file:
            pickle.dump(existing_data, file)

        print("Data appended to pickle file successfully:", file_path)
        print('<meta http-equiv="refresh" content="0; URL=./index.cgi">')
    except FileNotFoundError:
        print("Existing file not found:", file_path)
    except Exception as e:
        print("An error occurred while appending data to pickle file:", str(e))

# Retrieve the form data
form = cgi.FieldStorage()

print("Content-type: text/html")
print()

webpage = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <title>Enter Post - THB.B</title>
    <link rel="stylesheet" type="text/css" href="./styles/style2.css">
</head>
<body>
    <div class="container">
        <h1><a href="./index.cgi">THB.Billboard</a><sub><span style="font-size:small">v.0.0.1(Beta)</span></sub></h1> 
        <hr>
        <p>This is a space where you can express your mind viel spass.</p>
    
        <h2>Enter a new post</h2>
        <div id="post-container">
            <form method="post">
                <label for="post-text"></label>
                <textarea id="post-text" name="post-text" style="width: 100%; height: 20vh;">Start writing...</textarea>
                <div style="text-align:center">
                    <br>
                    <label for="post-usrname"></label>
                    <input type="text" id="post-usrname" placeholder="@username" name="post-usrname" style="width: 100%"  onfocus="if (this.value === '') this.value = '@anonymous'" onblur="if (this.value === '') this.value = '@anonymous'">
                    <br><br>
                    <button type="button" onclick="window.location.href='./index.cgi'">Cancel</button>
                    <button type="submit">Submit</button>
                </div>
            </form>
        </div>
        <footer>
            <hr>
            <p>Made by Thierry und Christian {get_date_or_year("year")}</p>
        </footer>
    </div>
</body>
</html>
"""

if form.getvalue('post-text') and form.getvalue('post-usrname'):
    store_data()
else:
    print(webpage)