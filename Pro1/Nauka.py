class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property #GETTER
    def height(self):
        print("Retrieving the Height")

        return self.__height

    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height=value
        else:
            print("Please only enter numbers for height")

    @property  # GETTER
    def width(self):
        print("Retrieving the Height")

        return self.__width

    @height.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for height")

    def getArea(self):
        return int(self.__width)*int(self.__height)

def main():
    asquare=Square()
    height=input("Enter height:")
    width=input("Enter width:")

    asquare.height=height
    asquare.width=width

    print("Height :{}".format(asquare.height))
    print("Width :{}".format(asquare.width))

    print("The Area is :{}".format(asquare.getArea()))

main()