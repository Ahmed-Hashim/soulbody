import requests as rq
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def save_image(url: str):
  # Get the data from the url
  image_source = rq.get(url)
  # Check if the suffix is one of the following
  filename = 'media/images/designs/'+str (url.split('/')[-1])

  # Create our output in the specified folder (wb = write bytes)
  with open(f'{BASE_DIR}/{filename}', 'wb') as file:
    file.write(image_source.content)
    print(f'Successfully downloaded: {filename}')
  return filename



