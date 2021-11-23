import os
from PIL import Image

src = 'images'
dst = '/opt/icons'

for file in os.listdir(src):
    # Name the new image
    f, _ = os.path.splitext(file)
    outfile = os.path.join(dst, f + '.jpeg')
    if outfile != file:
        try:
            with Image.open(os.path.join(src,file)) as img:
                # Rotate the image 90° clockwise
                # Resize the image from 192x192 to 128x128, and
                # Save the image to a new folder in .jpeg format
                # BUT check the image mode first! SEE
                # https://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.transpose(Image.ROTATE_90).resize((128, 128)).save(outfile)
        except OSError as e:
            print("Cannot create", outfile)