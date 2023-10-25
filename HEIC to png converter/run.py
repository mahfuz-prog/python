import os
import time
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def heic_to_png(working_dir):
    input_path = working_dir + '\img'
    output_path = working_dir + '\Output Image'
    os.chdir(input_path)
    total_image = len(os.listdir())
    print(f'Toatal {total_image} Images')

    for img in os.listdir():
        start_time = time.time()
        name, _ = os.path.splitext(img)
        image = Image.open(img)
        image.save(f'{output_path}\{name}.png')
        run_time = time.time() - start_time
        print(f'{name} processed in {run_time}')

if __name__ == '__main__':
    heic_to_png(os.getcwd())
