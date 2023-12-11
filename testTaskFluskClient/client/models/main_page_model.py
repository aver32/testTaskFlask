from tkinter import *

from client.constants import MAIN_PAGE_HEIGHT, MAIN_PAGE_WIDTH


class MainPageModel:
    __window_height: int = MAIN_PAGE_HEIGHT
    __window_width: int = MAIN_PAGE_WIDTH

    def __init__(self):
        self.__main_page: Tk = Tk()
        self.__create_page_geometry()

    @property
    def main_page(self):
        return self.__main_page

    @property
    def window_height(self):
        return self.__window_height

    @property
    def window_width(self):
        return self.__window_width

    def __create_page_geometry(self) -> None:
        screen_width = self.__main_page.winfo_screenwidth()
        screen_height = self.__main_page.winfo_screenheight()

        x = (screen_width - self.__window_width) // 2
        y = (screen_height - self.__window_height) // 2

        self.__main_page.geometry(f"{self.__window_width}x{self.__window_height}+{x}+{y}")

