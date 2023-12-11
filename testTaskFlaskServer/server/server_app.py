from threading import Thread

from flask import Flask, request, jsonify, send_file
from server.document_processor import DocumentProcessor

app = Flask(__name__)
doc_processor: DocumentProcessor = None


@app.route('/upload_archive_images', methods=['POST'])
def upload_file():
    if 'archive_images' not in request.files:
        return jsonify({'error': 'No file part'}), 500

    global doc_processor
    images = request.files['archive_images']
    doc_processor = DocumentProcessor(images)
    doc_processor.process_uploaded_file()
    Thread(target=run_processing_images_thread).start()
    return jsonify({'error': 'No', 'folder_name': f'{doc_processor.upload_directory_name}'}), 200


@app.route('/check_status/<folder_name>', methods=['GET'])
def check_status(folder_name):
    global doc_processor
    if doc_processor is not None:
        if doc_processor.is_processing:
            message = jsonify({"is_processing": None if doc_processor is None else doc_processor.is_processing}), 200
        else:
            message = jsonify({"is_processing": None if doc_processor is None else doc_processor.is_processing}), 500
        return message


@app.route("/download_processed_images_archive_<folder_name>", methods=["GET"])
def download_processed_archive(folder_name):
    global doc_processor
    if doc_processor.is_processing:
        try:
            processed_images_archive_path = doc_processor.create_zip_images_archive()
            return send_file(processed_images_archive_path, as_attachment=True,
                             download_name=doc_processor.upload_directory_name)
        except Exception:
            return jsonify({"error": "True, Ошибка при скачивании архива"}), 500
    else:
        return jsonify({"error": "Архив не обрабатывался"}), 404


def run_processing_images_thread():
    global doc_processor
    if doc_processor is not None:
        doc_processor.simulate_document_processing()



