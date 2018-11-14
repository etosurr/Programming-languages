from flask import Flask, request, jsonify, send_file
from pathlib import Path

app = Flask(__name__)


@app.route('/list')
def list():
    directory = Path(request.args['directory'])
    assert (directory.is_dir())
    result = []
    for i in directory.iterdir():
        result.append({
            "name": i.name,
            "directory": i.is_dir()
        })
    return jsonify(result)


@app.route('/get')
def get():
    file = Path(request.args['file'])
    return send_file(str(file), attachment_filename=file.name)


if __name__ == '__main__':
    app.run()
