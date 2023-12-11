import os
import time
from threading import Thread
from tkinter import filedialog

import requests

from client.constants import ZIP_ARCHIVE_IMAGES_NAME, ENABLE, HOST_URL, CHECK_STATUS_URL, UPLOAD_ARCHIVE_URL, \
    DELAY_REQUEST, DOWNLOAD_ARCHIVE_URL, ZIP_ARCHIVE_PROCESSED_IMAGES
from client.controller.controller_image import ImageController
from client.models.main_page_model import MainPageModel
from client.views.main_view import MainPageView


class ControllerMain:
    def __init__(self):
        self.__main_page_model: MainPageModel = MainPageModel()
        self.__main_page_view: MainPageView = MainPageView()
        self.__image_controller: ImageController = ImageController()
        self.__arch_path = ""
        self.__folder_in_server = ""

    def start_control(self):
        self.__main_page_view.set_ui(self.__main_page_model.main_page)
        self.__main_page_view.set_command_to_btn_select_folder(self.__main_page_view.btn_select_folder,
                                                               self.__select_images_folder)
        self.__main_page_view.set_command_to_btn_select_folder(self.__main_page_view.btn_post_images,
                                                               self.__post_images)
        self.__main_page_model.main_page.mainloop()

    def __post_images(self):
        Thread(target=self.__post_images_thread).start()

    def __post_images_thread(self):
        with open(self.__arch_path, "rb") as archive:
            files = {"archive_images": archive}
            try:
                response = requests.post(f"{HOST_URL}{UPLOAD_ARCHIVE_URL}", files=files)
                if response.status_code == 200:
                    self.__folder_in_server = response.json()["folder_name"]
            except (ConnectionRefusedError, requests.exceptions.ConnectionError) as error:
                print(error)

        self.__ping_server()

    def __ping_server(self):
        while True:
            print("Получение статуса готовности обработанных изображений...")
            status = requests.get(f"{HOST_URL}{CHECK_STATUS_URL}{self.__folder_in_server}")
            if not status.json()["is_processing"]:
                print(f"Изображения в папке: {self.__folder_in_server} ещё обрабатываются."
                      f" Повторная проверка через {DELAY_REQUEST} сек...")
                time.sleep(DELAY_REQUEST)
            else:
                print("Изображения успешно обработаны.\n Запускаем скачивание архива с обработанными изображениями")
                self.__download_processed_archive()
                return True

    def __download_processed_archive(self):
        response = requests.get(f"{HOST_URL}{DOWNLOAD_ARCHIVE_URL}{self.__folder_in_server}")

        if response.status_code == 200:
            with open(ZIP_ARCHIVE_PROCESSED_IMAGES, "wb") as local_file:
                local_file.write(response.content)
            print(f"Обработанные изображения загружены в архив: {ZIP_ARCHIVE_PROCESSED_IMAGES}")
        else:
            print(f"{response.status_code} Ошибка при получении архива")

    def __select_images_folder(self):
        self.__image_controller.clear()

        self.__image_controller.images_folder_path = filedialog.askdirectory()
        if self.__image_controller.images_folder_path != "":
            self.__image_controller.check_dir_exists_images_files()

            project_root = os.path.dirname(os.path.dirname(__file__))
            self.__arch_path = os.path.join(project_root, ZIP_ARCHIVE_IMAGES_NAME)
            self.__image_controller.create_zip_images_archive(self.__arch_path)

            self.__main_page_view.set_state_btn_post_images(ENABLE)
