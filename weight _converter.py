{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "23902935",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "weight: 72\n",
      "(L)bs or (K)g: \n",
      "You are 159.0 pounds.\n"
     ]
    }
   ],
   "source": [
    "weight= int(input('weight: '))\n",
    "unit= input(\"(L)bs or (K)g: \") # enter L for weight in pounds and K for weight in kilos\n",
    "if unit.upper()== \"L\":\n",
    "    converted= weight * 0.45\n",
    "    print(\"You are \"+ str(converted) + \" kilos.\")\n",
    "else:\n",
    "    converted= weight // 0.45\n",
    "    print(\"You are \"+ str(converted) + \" pounds.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5176217",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25817d92",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
