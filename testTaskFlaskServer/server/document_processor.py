import os
import random
import time
import zipfile
import uuid

from werkzeug.datastructures import FileStorage

from server.constatnts import START_DELAY_SIMULATE_DOCUMENT_PROC, END_DELAY_SIMULATE_DOCUMENT_PROC, \
    UNZIPPED_FOLDER_NAME, PROCESSED_IMAGES_FOLDER_NAME


class DocumentProcessor:

    def __init__(self, images_archive: FileStorage):
        self.__upload_directory_name = self.__generate_random_name()
        self.__upload_directory_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                         self.__upload_directory_name)
        self.__images_archive: FileStorage = images_archive
        self.__is_processing: bool = False
        self.__images_to_processed_folder_path: str = ""

    @property
    def is_processing(self):
        return self.__is_processing

    @property
    def upload_directory_name(self):
        return self.__upload_directory_name

    def __generate_random_name(self) -> str:
        return str(uuid.uuid4())

    def simulate_document_processing(self) -> None:
        sleep_delay = random.uniform(START_DELAY_SIMULATE_DOCUMENT_PROC, END_DELAY_SIMULATE_DOCUMENT_PROC)
        time.sleep(sleep_delay)
        self.__is_processing = True

    def process_uploaded_file(self):
        if not os.path.exists(self.__upload_directory_path):
            os.makedirs(self.__upload_directory_path)
        directory_to_unzipped_images = os.path.join(self.__upload_directory_path, self.__images_archive.filename)
        self.__images_archive.save(directory_to_unzipped_images)
        self.__images_archive.close()

        with zipfile.ZipFile(directory_to_unzipped_images, 'r') as zip_ref:
            self.__images_to_processed_folder_path = os.path.join(self.__upload_directory_path, UNZIPPED_FOLDER_NAME)
            zip_ref.extractall(self.__images_to_processed_folder_path)

    def del_temp_directory(self):
        os.rmdir(self.__upload_directory_path)

    def create_zip_images_archive(self) -> str:
        files = [file for file in os.listdir(self.__images_to_processed_folder_path) if not os.path.isdir(file)]
        path_to_zip = os.path.join(self.__upload_directory_path, PROCESSED_IMAGES_FOLDER_NAME)
        with zipfile.ZipFile(path_to_zip, 'w') as zipf:
            for file_to_archive in files:
                zipf.write(self.__images_to_processed_folder_path+"\\"+file_to_archive, arcname=file_to_archive)

        return path_to_zip
