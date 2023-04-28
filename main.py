from flask import Flask, request, jsonify
from compare_image import compare_faces

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_images():
    data = request.get_json()
    image1 = data['image1']
    image2 = data['image2']
    result = compare_faces(image1, image2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)