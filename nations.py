import wand.image
import io

nations = [
    {
        'name': "Babilandia", #id 0
        'color': "#009245", #green
        'joinable': True,
        'defaultProvince': 1,
        'deJureProvinces': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    {
        'name': "Republic of Boys", #id 1
        'color': "red", #red
        'joinable': True,
        'defaultProvince': 13,
        'deJureProvinces': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    },
    {
        'name': "Balloon Kingdom", #id 2
        'color': "#0071bc", #blue
        'joinable': True,
        'defaultProvince': 25,
        'deJureProvinces': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    },
    {
        'name': "Unowned", #id 3
        'color': "#666", #grey
        'joinable': False,
        'defaultProvince': -2,
        'deJureProvinces': []
    }
]

path = "/usr/bin/"

def makeMap():
    svg_file = open(path + "Babi Island.svg", "rb")
    print (svg_file)
    with wand.image.Image(blob =svg_file.read(), format="svg") as image:
        png_image = image.make_blob("png")
    with open(path + "Babi_Island.png", "wb") as out:
        out.write(png_image)