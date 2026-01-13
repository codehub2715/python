#Read a binary file and create a duplicate copy using 'rb' and 'wb'.

with open('image.png', 'rb') as f:
    content = f.read()

with open('image_copy.png', 'wb') as copy_file:
        copy_file.write(content)

