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
    print(article['title'])
    print()

    # if description is a nonetype, invent it
    if article['description'] == None:
        description = "No description available. CLick the link to read more."

    # if it's longer that 150, only show first 150 characters
    elif len( str(article['description']) ) > 150:
        description = f"{str(article['description']) [:150]}..."

    # if it's not greater that 150, show all of it
    elif len(article['description']) <= 150:
        description = str(article['description'])

    print( f"{description}" )      

    # show the link
    print(f"Link: {article['link']}")
