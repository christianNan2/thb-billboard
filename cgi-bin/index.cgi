#!/usr/bin/python3

import pickle
import datetime

def get_date_or_year(option) ->str:
    now = datetime.datetime.now()

    if option == 'datetime':
        return str(now.strftime('%Y-%m-%d %H:%M:%S'))
    elif option == 'year':
        return str(now.year)
    else:
        return str("Invalid option. Please choose either 'datetime' or 'year'.")

def formated(data)->str:
  text="""
  <div id="post-container">
  """
  for i in data:
    text = text + f"""
			<div class="post">{i[0]}<p style="text-align: right;">by {i[1]} | {i[2]}</p></div>
    """
  text = text + """
  </div>
  """
  return text

def retrieve_posts(file_path) -> str:
  
  try:
    with open(file_path, 'rb') as file:
      data = pickle.load(file)
      if isinstance(data, list) and all(isinstance(item, list) for item in data):
          return formated(data)
      else:
          print("Invalid data format in pickle file. Expected a list of lists.")
  except FileNotFoundError:
          print("File not found:", file_path)
  except pickle.UnpicklingError:
          print("Error occurred while unpickling the file:", file_path)
  except Exception as e:
          print("An error occurred:", str(e))

print("Content-type: text/html")

webpage = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>THB.Billboard</title>
<link rel="stylesheet" type="text/css" href="./styles/style1.css">
</head>
<body>
	<div class="container">
		<h1> <a href="./index.cgi">THB.Billboard</a><sub><span style="font-size:small">v.0.0.1(Beta)</span></sub></h1> 
		<hr>
		<p>This is a space where you can express your mind viel spaß 😌.</p>
		<h2>All Posts</h2>
		
		<a href="./post_webpage.cgi">write a post</a>
"""

webpage = webpage + retrieve_posts("data.pickle")

webpage = webpage + f"""
  <footer>
    <hr>
    <p>Made by Thierry und Christian {get_date_or_year("year")}</p>
  </footer>
	</div>
</body>
</html>
"""

print(webpage)