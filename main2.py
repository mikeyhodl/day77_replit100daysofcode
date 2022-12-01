from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    content = """<html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>
  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>
</body>
  
</html>"""
    return content


@app.route('/fstrings')
def fstrings():
    myName = "Katie"
    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    return page


@app.route('/home')
def home():
    page = """html
  
  <html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
  
</html>
  
  """
    return page


@app.route('/owino')
def owino():
    myName = "Owino"
    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)

    return page


@app.route('/mikee')
def mikee():
    myName = "Azzi"
    title = "Day 56 Solution"
    text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
    page = ""
    f = open("template/users.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    page = page.replace("{text}", text)
    page = page.replace("{title}", title)
    return page


@app.route('/77')
def seventySeven():
    return redirect(
        "https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")


app.run(host='0.0.0.0', port=81)
