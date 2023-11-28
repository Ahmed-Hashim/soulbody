import requests


def uptofb(link, mes, access):
    page_ID = '104133784532614'
    post = f'https://graph.facebook.com/{page_ID}/photos?url={link}&message={mes}&access_token={access}'
    response = requests.post(post)
    return response.json()
