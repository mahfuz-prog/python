import os
import time
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def heic_to_png(working_dir, format):
    input_path = working_dir + '\img'
    output_path = working_dir + '\Output Image'
    os.chdir(input_path)
    total_image = len(os.listdir())
    print(f'Toatal {total_image} Images')

    for img in os.listdir():
        start_time = time.time()
        name, _ = os.path.splitext(img)
        image = Image.open(img)
        image.save(f'{output_path}\{name}.{format}')
        run_time = time.time() - start_time
        print(f'{name} processed in {run_time}')

if __name__ == '__main__':
    format = input('png, jpg, jpeg supported: ')
    try:
        heic_to_png(os.getcwd(), format=format)
    except Exception as e:
        print(e)
