from PIL import Image

f_name = "secret_map.txt"
png_fname = "247ctf_flag.png"

class myPixel():
    max_x = 0
    max_y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.update_max_pixel(x,y)
    @classmethod
    def update_max_pixel(cls, var_x, var_y):
        if var_x > cls.max_x:
            cls.max_x = var_x
        if var_y > cls.max_y:
            cls.max_y = var_y
    @classmethod
    def get_pixelmax_x(cls):
        return cls.max_x
    @classmethod
    def get_pixelmax_y(cls):
        return cls.max_y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

# methods start here
def open_file(file_name):
    try:
        f = open(file_name, "r")
        return f
    except Exception as e:
        print("File %s does not exist" % file_name)
        print(Exception)
        return 0

# open file and define pixel array
file_data = open_file(f_name)
pixel_array = []

# read lines from file and split on values
for tmp_line in file_data:
    l = tmp_line.split(" ")
    a = int(l[0], 0)
    b = int(l[1], 0)
    pixel_array.append(myPixel(a, b))

# define png resolution
img_resolution_x = myPixel.get_pixelmax_x() + 15
img_resolution_y = myPixel.get_pixelmax_y() + 15
# create new png
img = Image.new(mode='RGB', size=(img_resolution_y, img_resolution_x), color="white") # Create a new white image
pixels = img.load()

# mark black pixels from pixel array to png file
for p in pixel_array:
    x = p.get_x()
    y = p.get_y()
    img.putpixel((y,x),(0, 0, 0))

# safe png and show png buffer
img.save(png_fname, format="png")
img.show()
