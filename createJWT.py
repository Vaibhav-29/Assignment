{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af3b371c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app/auth.py\n",
    "import jwt\n",
    "from flask import request, current_app\n",
    "\n",
    "def create_token(user_id):\n",
    "    return jwt.encode({'user_id': user_id}, current_app.config['SECRET_KEY'], algorithm='HS256')\n",
    "\n",
    "def verify_token(token):\n",
    "    try:\n",
    "        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])\n",
    "        return payload['user_id']\n",
    "    except jwt.ExpiredSignatureError:\n",
    "        return 'Token expired'\n",
    "    except jwt.InvalidTokenError:\n",
    "        return 'Invalid token'\n",
    "\n",
    "# Add JWT token generation and verification to your authentication system.\n"
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
