"""
    Develop Rectangle class with following content:
2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
One constructor with two optional parameters a and b (parameters specify rectangle sides).
Side А of a rectangle defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;

Method `get_side_a`, returning value of the side А;
Method `get_side_b`, returning value of the side В;
Method `area`, calculating and returning the area value;
Method `perimeter`, calculating and returning the perimeter value;
Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and False in another case;
Method `replace_sides`, swapping rectangle sides.


    Develop class ArrayRectangles, in which declare:
Private attribute `rectangle_array` (list of rectangles);
One constructor that creates a list of rectangles with length `n` filled with `None` and
  that receives an arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle`
  (the list must be unpacked inside the constructor so that there will be no nested arrays).
  If both objects and length are passed, at first creates a list with received objects and then add the required number of Nones to achieve the desired length.
If `n` is less than the number of received objects, the length of the list will be equal to the number of objects;

Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and returning True, or returning False, if there is no free space in the array;
Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value (numeration starts from zero);
Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value (numeration starts from zero);
Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a=4.0, b=3.0):
        """
        Constructor of Rectangle class object.
        :param a: Optional float parameter. Default = 4.0.
        :param b: Optional float parameter. Default = 3.0.
        """
        if a <= 0 or b <= 0:
            raise ValueError

        self.side_a = float(a)
        self.side_b = float(b)

    def __str__(self):
        """
        Returns string representation of class object.
        :return: side_a x side_b
        """
        return f'{self.side_a} x {self.side_b}'

    # @property
    def get_side_a(self):
        """
        Getter of side_a.
        :return: side_a
        """
        return self.side_a

    # @property
    def get_side_b(self):
        """
        Getter of side_b.
        :return: side_b
        """
        return self.side_b

    def area(self):
        """
        Returns calculated value of area of the rectangle. Formula: side_a*side_b.
        :return: area
        """
        return self.side_a * self.side_b

    def perimeter(self):
        """
        Returns calculated value of perimeter of the rectangle. Formula: 2*(side_a+side_b).
        :return: perimeter
        """
        return 2 * (self.side_a + self.side_b)

    def is_square(self):
        """
        Returns bool value whether or not rectangle is a square.
        :return: bool value
        """
        return self.side_a == self.side_b

    def replace_sides(self):
        """
        Swaps sides of rectangle.
        :return: None
        """
        self.side_a, self.side_b = self.side_b, self.side_a


class ArrayRectangles:
    def __init__(self, *args):
        """
        Constructor of rectangles array.
        Receive (n:int) -> create list of n-length of None objects.
        Receive (n:int, *args:rectangles) -> create list of given rectangles and
        if n bigger than amount of rectangles add None objects, so that length of array is n.
        Receive(*args:rectangles) -> create list of given rectangles.
        Can receive list of rectangles and unpack them into array.
        :param args: ([n:int][, *args:rectangles]) should receive at least one parameter.
        """
        self.__rectangle_array = []

        if isinstance(args[0], int):
            rectangles = args[1:]
            if not rectangles:
                self.__rectangle_array = [None] * args[0]
            else:
                for rect in rectangles:
                    if isinstance(rect, list):
                        self.__rectangle_array += rect
                    else:
                        self.__rectangle_array.append(rect)

                d = args[0] - len(self.__rectangle_array)
                if d > 0:
                    self.__rectangle_array += [None] * d
        else:
            for rect in args:
                if isinstance(rect, list):
                    self.__rectangle_array += rect
                else:
                    self.__rectangle_array.append(rect)

    def __str__(self):
        """
        Returns string representation of array of rectangles (rectangles as strings in list).
        :return: string with array
        """
        l = [str(x) for x in self.__rectangle_array]
        return str(l)

    def add_rectangle(self, r):
        """
        Adds a rectangle object to array and returns True if there is an empty place in array.
        Returns False and adds nothing if array already full.
        :type r: Object of Rectangle class.
        :return: Bool value.
        """
        if None in self.__rectangle_array:
            self.__rectangle_array[self.__rectangle_array.index(None)] = r
            return True
        else:
            return False

    def number_max_area(self):
        """
        Returns index of first rectangle with the biggest area value.
        Returns -1 if the array doesn't have rectangles.
        :return: int
        """
        l = [x.area() for x in self.__rectangle_array if x]
        if l:
            max_value = max(l)
            index = l.index(max_value)
            return index
        else:
            return -1

    def number_min_perimeter(self):
        """
        Returns the number of squares in the array of rectangles.
        :return: int
        """
        l = [x.is_square() for x in self.__rectangle_array if x]
        if l:
            min_value = min(l)
            index = l.index(min_value)
            return index
        else:
            return -1

    def number_squares(self):
        """
        Returns number of squares in the array of rectangles.
        :return: int
        """
        l = [x.is_square() if x else 0 for x in self.__rectangle_array]
        number = l.count(1)
        return number

