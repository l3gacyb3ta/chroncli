import requests, os

# Get the posts from the chronicles api
data = requests.get("http://chronicles.zephyr/api/posts/").json()


def display(post):
    """Dispay a given post"""
    print(post["id"], "-", post["User"]["name"])
    print(post["text"])

    # Create image url
    url = "http://chronicles.zephyr" + post["attachments"]

    # get the extension of the file
    extension = "." + post["attachments"].split(".")[-1]

    # Download the image and save it to disk to then display it
    os.system('wget -q "' + url + '" -O image' + extension)
    os.system("viu -h 35 image" + extension)


for post in data[-6:-2]:
    display(post)
