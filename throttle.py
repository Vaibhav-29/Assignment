{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf674bbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app/api.py\n",
    "from flask_limiter import Limiter\n",
    "\n",
    "limiter = Limiter(app, key_func=lambda: request.headers.get('Authorization'))\n",
    "\n",
    "# Rate limit to 5 requests per minute\n",
    "@limiter.request_filter\n",
    "def rate_limit_exempt():\n",
    "    return False\n",
    "\n",
    "@limiter.limit(\"5 per minute\")\n",
    "class ThrottleTest(Resource):\n",
    "    def get(self):\n",
    "        return {'message': 'API call within throttle limit'}\n",
    "\n",
    "api.add_resource(ThrottleTest, '/throttle-test')\n"
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
