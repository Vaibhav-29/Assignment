{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6057df1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app/api.py\n",
    "from flask_restful import Resource, Api\n",
    "from flask import request\n",
    "from werkzeug.utils import secure_filename\n",
    "\n",
    "api = Api(app)\n",
    "\n",
    "class ImageUpload(Resource):\n",
    "    def post(self):\n",
    "        # Check if the post request has the file part\n",
    "        if 'file' not in request.files:\n",
    "            return {'message': 'No file part'}, 400\n",
    "\n",
    "        file = request.files['file']\n",
    "        if file.filename == '':\n",
    "            return {'message': 'No selected file'}, 400\n",
    "\n",
    "        if file:\n",
    "            filename = secure_filename(file.filename)\n",
    "            file.save(filename)\n",
    "            return {'message': 'File uploaded successfully', 'filename': filename}, 201\n",
    "\n",
    "api.add_resource(ImageUpload, '/upload')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
