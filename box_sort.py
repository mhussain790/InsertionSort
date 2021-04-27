"""

Author: Masud Hussain
Course: CS162
Assignment: 4B

"""


class Box:
    def __init__(self, _length, _width, _height):
        self._length = _length
        self._width = _width
        self._height = _height

    def volume(self):
        return self._length * self._width * self._height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


def box_sort(a_list):
    """
    Insertion sort method to sort volume returned from Box objects in descending order.

    :param a_list:
    :return: sorted list of volume from greatest to least
    """

    for i in range(1, len(a_list)):
        value = a_list[i]

        position = i - 1

        while position >= 0 and value.volume() > a_list[position].volume():
            a_list[position + 1] = a_list[position]
            position -= 1

        a_list[position + 1] = value
