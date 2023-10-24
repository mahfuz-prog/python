import os
from PIL import Image
from pillow_heif import register_heif_opener
import sys
import time

register_heif_opener()

def heic_to_png():
    input_path = os.getcwd()+ '\img'
    output_path = os.getcwd() + '\Output Image'
    os.chdir(input_path)
    total_image = len(os.listdir())
    print(f'Toatal {total_image} Images')

    for i in os.listdir():
        start_time = time.time()
        name, _ = os.path.splitext(i)
        image = Image.open(i)
        image.save(f'{output_path}\{name}.png')
        run_time = time.time() - start_time
        print(f'{name} processed in {run_time}')

if __name__ == '__main__':
    heic_to_png()
