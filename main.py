import requests
from send_email import send_email

api_key = "pub_77528381bf43230c1877b14e6739ac620b6da"

# define url as str
url = str("https://newsdata.io/api/1/"\
"news?apikey=pub_77528381bf43230c1877b14e6739ac620b6da&q=Crypto"\
"&language=en")  

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary

# access the value of 'results' key
articles = content['results']

# create a body and a subject
body = "Subject: Latest News"

# iterate over all elements in the 'articles' list
for index, article in enumerate(articles):

    # article title
    title = str(article['title']) 

    ad = str(article['description'])
    # if description is a nonetype, invent it
    if ad == "None":
        description = "No description available. Click the link to read more."

    # if it's longer that 150, only show first 150 characters
    elif len(ad) > 150:
        description = f"{ad[:150]}..."

    # if it's not greater that 150, show all of it
    elif len(ad) <= 150:
        description = ad

    # show the link
    link = article['link']

    # add extracted data to the existing body
    body += "\n" + title + "\n" + description\
          + "\n" + f"Link: {link}" + 2*"\n"
    
print(body)

body = body.encode("utf-8")
send_email(message=body)