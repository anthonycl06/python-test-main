from flask import Flask, request
from flask import jsonify
from configobj import ConfigObj
import os

app = Flask(__name__)

@app.route('/api/v1/Python-test/count-files', methods=['GET'])
def get_elements():
  path = r"C:\Users\PCC\Desktop\python-test-main"
  dir_list = os.listdir(path)
  response = {"countFiles": f"{len(dir_list)}"}
  return jsonify(response)

@app.route('/api/v1/Python-test/properties', methods=['PUT'])
def change_properties():
  try:
    content = request.json

    config = ConfigObj("application.properties")
    config.filename = "application.properties"
    config[f"application.title"] = content['title']
    config[f"application.date"] = content['date']
    config[f"application.description"] = content['description']
    config[f"application.author"] = content['author']
    config.write()
    
    response = {"message": "campo actualizado con éxito"}

    return jsonify(response)
  except:
    return jsonify({"message": "algo salió mal"})

@app.route('/api/v1/Python-test/delete', methods=['DELETE'])
def delete_file():
  try:

    response = {"message": "Archivo eliminado con exito"}

    return jsonify(response)
  except: 
    return jsonify({"message": "algo salió mal"})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000)