#### my client asked me to fix the size of elementor image carousel which include a lot's of images of different size. Problem here is to scale down the others images size to a minimum image size.

![carousel](Screenshot.png)

#### To achive this using python requests-html library
* From elementor carousel set the image size full.
* Run the script on google colab or local machine.
Packages:
```
Pillow==10.1.0
requests-html==0.10.0
```
* After getting minimum width and height set elementor carousel image size to minimum