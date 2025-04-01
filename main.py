import requests
#from send_email import send_email


api_key = "pub_77528381bf43230c1877b14e6739ac620b6da"

# define url as str
url = str("https://newsdata.io/api/1/"\
"news?apikey=pub_77528381bf43230c1877b14e6739ac620b6da&q=Crypto"\
"&language=en")  

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary

print(content)