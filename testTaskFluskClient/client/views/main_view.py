import tkinter as tk
from threading import Thread
from tkinter import ttk, Tk, Frame, Label

from client.constants import LABEL_SELECT_FOLDER_TEXT, WHITE_BACKGROUND_COLOR, FONT_STYLE, LABEL_SELECT_FOLDER_PADY, \
    BTN_SELECT_FOLDER_TEXT, BTN_SELECT_FOLDER_PADY, BTN_POST_IMAGES_ARCHIVE, LABEL_ARCHIVE_STATE_DISABLE_TEXT, \
    GRAY_BACKGROUND_COLOR, LABEL_ARCHIVE_STATE_ENABLE_TEXT, ENABLE, DISABLE


class MainPageView:

    def __init__(self):
        self.__btn_select_folder: ttk.Button = None
        self.__btn_post_images: ttk.Button = None
        self.__label_archive_state: Label = None

    @property
    def btn_select_folder(self):
        return self.__btn_select_folder

    @property
    def btn_post_images(self):
        return self.__btn_post_images

    def set_ui(self, main_page: Tk) -> None:
        if main_page is None:
            raise ValueError("main_page не может быть None")

        frame = Frame(
            master=main_page,
            bg=WHITE_BACKGROUND_COLOR)

        label_select_folder = Label(
            master=frame,
            text=LABEL_SELECT_FOLDER_TEXT,
            bg=WHITE_BACKGROUND_COLOR,
            font=FONT_STYLE
        )

        self.__btn_select_folder = ttk.Button(
            master=frame,
            text=BTN_SELECT_FOLDER_TEXT
        )

        self.__label_archive_state = Label(
            master=frame,
            text=LABEL_ARCHIVE_STATE_DISABLE_TEXT,
            bg=GRAY_BACKGROUND_COLOR,
        )

        self.__btn_post_images = ttk.Button(
            master=frame,
            text=BTN_POST_IMAGES_ARCHIVE,
            state='disable'
        )

        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        label_select_folder.pack(side=tk.LEFT, anchor=tk.NW, pady=LABEL_SELECT_FOLDER_PADY)
        self.__btn_select_folder.pack(side=tk.TOP, fill=tk.BOTH, pady=BTN_SELECT_FOLDER_PADY)
        self.__label_archive_state.pack()
        self.__btn_post_images.pack(side=tk.TOP, fill=tk.BOTH, pady=BTN_SELECT_FOLDER_PADY)

    def set_command_to_btn_select_folder(self, button: ttk.Button, command_for_button: callable) -> None:
        if button and command_for_button is not None:
            button.configure(command=command_for_button)

    def set_state_btn_post_images(self, state: str):
        if state in [ENABLE, DISABLE]:
            self.__btn_post_images.state(state)
            self.__label_archive_state.config(text=LABEL_ARCHIVE_STATE_ENABLE_TEXT)
        else:
            print("Неверное состояние")
