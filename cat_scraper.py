#%%
from selenium import webdriver
import urllib.request
# from aws_upload import download_file
# from aws_upload import upload_file
# import tempfile
from tqdm import tqdm
import os
if not os.path.exists('cats'):
    os.makedirs('cats')
#%%
# Define the driver
ROOT = 'https://all-free-download.com/free-photos/cute-cat-jpg.html'
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(ROOT)

# Get the list of cat images
elem = driver.find_element_by_class_name('imgcontainer')
if elem:
    img_list = elem.find_elements_by_class_name('img-responsive')
    if img_list:
        src_list = []
        for src in img_list:
            try:
                src_list.append(src.get_attribute('src'))
            except:
                print('No source found')
        # Create a temporary directory, so you don't store images in your local machine
        # with tempfile.TemporaryDirectory() as temp_dir:
        for i, scr in enumerate(tqdm(src_list)):
            urllib.request.urlretrieve(scr, f'cats/cat_{i}.png')
                # upload_file(f'{temp_dir}/cat_{i}.png', 'aicoretestcats', f'cats/cat_{i}')
driver.quit()
# %%
