{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53f63802",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app/__init__.py\n",
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.config['SECRET_KEY'] = 'your_secret_key_here'\n"
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
