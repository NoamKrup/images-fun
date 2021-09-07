def get_image():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    # Read Images
    img = mpimg.imread(r"C:\Users\noamk\Downloads\windows-10-2018-insider-wallpaper.jpg")
    # Output Images
    plt.imshow(img)
    return img

if __name__=='__main__':
    image = get_image()
    print(image)