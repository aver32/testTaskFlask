import os
import zipfile

from PIL import Image


class ImageController:
    def __init__(self):
        self.__images_folder_path: os.path = ""
        self.__images_files_paths: list[str] = []

    @property
    def images_folder_path(self):
        return self.__images_folder_path

    @images_folder_path.setter
    def images_folder_path(self, value: str):
        if os.path.isdir(value):
            self.__images_folder_path = value
        else:
            print("Неверный путь для папки")

    def check_file_is_image(self, file_name: str) -> bool:
        try:
            img = Image.open(os.path.join(self.__images_folder_path, file_name))
            img.close()
            return True
        except (FileNotFoundError, ValueError, TypeError, IOError):
            return False

    def check_dir_exists_images_files(self) -> None:
        files_images_paths = [file_path for file_path in os.listdir(self.__images_folder_path) if
                              os.path.isfile(os.path.join(self.__images_folder_path, file_path))]
        if files_images_paths is None:
            print("В этой папке нету файлов")
            return

        for file_name in files_images_paths:
            if self.check_file_is_image(file_name):
                self.__images_files_paths.append(os.path.join(self.__images_folder_path, file_name))

        if not self.__images_files_paths:
            print("В данной папке нету файлов с изображениями")
        else:
            print("Файлы изображений прочитаны успешно")

    def create_zip_images_archive(self, archive_path: str) -> None:
        if not self.__images_files_paths:
            raise ValueError("list images files is None")
        if archive_path is None:
            return

        with zipfile.ZipFile(archive_path, 'w') as zipf:
            for file_to_archive in self.__images_files_paths:
                file_path = os.path.basename(file_to_archive)
                zipf.write(file_to_archive, arcname=file_path)

    def clear(self):
        self.__images_folder_path = ""
        self.__images_files_paths = []
