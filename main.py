import requests
#from send_email import send_email

api_key = "pub_77528381bf43230c1877b14e6739ac620b6da"

# define url as str
url = str("https://newsdata.io/api/1/"\
"news?apikey=pub_77528381bf43230c1877b14e6739ac620b6da&q=Crypto"\
"&language=en")  

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary

# access the value of 'results' key
articles = content['results']

# iterate over all elements in the 'articles' list
for index, article in enumerate(articles):
    print()
    print(f"{index+1}. ARTICLE")

    # article title
    title = article['title'] 
    print(title)
    print()

    ad = article['description']
    # if description is a nonetype, invent it
    if ad == None:
        description = "No description available. CLick the link to read more."

    # if it's longer that 150, only show first 150 characters
    elif len(str(ad)) > 150:
        description = f"{str(ad) [:150]}..."

    # if it's not greater that 150, show all of it
    elif len(ad) <= 150:
        description = str(ad)

    print(description)      

    # show the link
    link = article['link']
    print(f"Link: {link}")
