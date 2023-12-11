# -------- UI --------
MAIN_PAGE_WIDTH = 800
MAIN_PAGE_HEIGHT = 600

LABEL_SELECT_FOLDER_TEXT = "Выберите папку для чтения:"
LABEL_SELECT_FOLDER_PADY = 15
WHITE_BACKGROUND_COLOR = "#FFFFFF"
GRAY_BACKGROUND_COLOR = "#807e7e"
FONT_STYLE = ("Arial", 20)

LABEL_ARCHIVE_STATE_DISABLE_TEXT = "Архив с изображениями еще не загружен, отправить на сервер невозможно"
LABEL_ARCHIVE_STATE_ENABLE_TEXT = "Архив с изображениями загружен, можно отправить на сервер"

BTN_SELECT_FOLDER_TEXT = "Выбрать папку"
BTN_SELECT_FOLDER_PADY = 25

BTN_POST_IMAGES_ARCHIVE = "Отправить архив с изображениями"

# -------- PATHS --------
ZIP_ARCHIVE_IMAGES_NAME = "images.zip"
ZIP_ARCHIVE_PROCESSED_IMAGES = "processed_images.zip"

# -------- BUTTON_STATES --------
ENABLE = ['!disabled']
DISABLE = ["disabled"]

# -------- SERVER_URL --------
HOST_URL = "http://127.0.0.1:5000"
CHECK_STATUS_URL = "/check_status/"
UPLOAD_ARCHIVE_URL = "/upload_archive_images"
DOWNLOAD_ARCHIVE_URL = "/download_processed_images_archive_"

# -------- DELAY --------
DELAY_REQUEST = 1
