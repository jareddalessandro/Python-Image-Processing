from PIL import Image


def main():

    orig_image = Image.open('road.jpg')
    basicLighten(orig_image)
    

def basicLighten(orig_image):
    width, height = orig_image.size
    new_image = Image.new('RGB', (width, height))

    for x in range(0, width):
        for y in range(0, height):
            # Obtain the RGB value for a single pixel at a time
            red, blue, green = orig_image.getpixel((x, y))

            # Logic for changing RGB values per pixel
            # putpixel((tuple containing coordinates), (red value, green value, blue value))
            new_image.putpixel((x, y), (int(red * 2), int(blue * 2), int(green * 2)))
            

    new_image.save("road_basicLighten.jpg")



if  __name__ == "__main__":
    main()
