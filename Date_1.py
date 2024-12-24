{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPOXckT4bZ/II0mfX5R6NwN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Saipradeep456/PYTHON-500-CODE/blob/main/Date_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O01gr4t58mB_",
        "outputId": "2dd8792d-9182-46c3-821e-6fefa1c8ca72"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "negative\n"
          ]
        }
      ],
      "source": [
        "##Python Program to check if a Number Is Positive Or Negative\n",
        "#Given an integer input, the objective is check whether the given integer is Positive or Negative.\n",
        "\n",
        "num = -123\n",
        "if num > 0:\n",
        "  print(\"positive\")\n",
        "elif num < 0:\n",
        "  print(\"negative\")\n",
        "else:\n",
        "  print(\"null\")\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Python Program to Check Whether a Number is Even or Odd\n",
        "#Given an integer input the objective is to write a Python code to Check Whether a Number is Even or Odd. To do so the main idea is to divide the number by 2 and check if it’s divisible or not. It’s an Even number is it’s perfectly divisible by 2 or an Odd number otherwise.\n",
        "\n",
        "num = int(input(\"enter a number:\"))\n",
        "if num%2 == 0:\n",
        "  print(\"it is even number\")\n",
        "else:\n",
        "  print(\"it is odd number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mK23Codh-Hnx",
        "outputId": "9efa816e-78c7-4ca9-da14-9325ad843aeb"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number:6\n",
            "it is even number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Python Program to Find the Sum of First N Natural Numbers\n",
        "#Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. To do so we can use different approaches to write the Python code and some such methods are mentioned below\n",
        "\n",
        "\n",
        "sai = 96\n",
        "\n",
        "sum = 0\n",
        "for i in range(sai+1):\n",
        "  sum+= i\n",
        "  print(sum)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w0i7HHpi_5sk",
        "outputId": "ecb1ea5d-7afd-479d-f1f0-65cf590f2840"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "3\n",
            "6\n",
            "10\n",
            "15\n",
            "21\n",
            "28\n",
            "36\n",
            "45\n",
            "55\n",
            "66\n",
            "78\n",
            "91\n",
            "105\n",
            "120\n",
            "136\n",
            "153\n",
            "171\n",
            "190\n",
            "210\n",
            "231\n",
            "253\n",
            "276\n",
            "300\n",
            "325\n",
            "351\n",
            "378\n",
            "406\n",
            "435\n",
            "465\n",
            "496\n",
            "528\n",
            "561\n",
            "595\n",
            "630\n",
            "666\n",
            "703\n",
            "741\n",
            "780\n",
            "820\n",
            "861\n",
            "903\n",
            "946\n",
            "990\n",
            "1035\n",
            "1081\n",
            "1128\n",
            "1176\n",
            "1225\n",
            "1275\n",
            "1326\n",
            "1378\n",
            "1431\n",
            "1485\n",
            "1540\n",
            "1596\n",
            "1653\n",
            "1711\n",
            "1770\n",
            "1830\n",
            "1891\n",
            "1953\n",
            "2016\n",
            "2080\n",
            "2145\n",
            "2211\n",
            "2278\n",
            "2346\n",
            "2415\n",
            "2485\n",
            "2556\n",
            "2628\n",
            "2701\n",
            "2775\n",
            "2850\n",
            "2926\n",
            "3003\n",
            "3081\n",
            "3160\n",
            "3240\n",
            "3321\n",
            "3403\n",
            "3486\n",
            "3570\n",
            "3655\n",
            "3741\n",
            "3828\n",
            "3916\n",
            "4005\n",
            "4095\n",
            "4186\n",
            "4278\n",
            "4371\n",
            "4465\n",
            "4560\n",
            "4656\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Python Program to Find the Sum of First N Natural Numbers\n",
        "#Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. To do so we can use different approaches to write the Python code and some such methods are mentioned below\n",
        "#formula -> num*(num+1)/2\n",
        "\n",
        "num = 9\n",
        "print(num*(num+1)/2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_zX7ik_uA2Ja",
        "outputId": "a11b27c2-8a38-4a91-b461-423021884169"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "45.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Python program to print sum of N natural numbers\n",
        "#Given an integer value the objective of the code is to sum up all the numbers until the input integer number. To do so we usually use iteration, we iterate through the numbers until the input number is reached while appending the number to the sum variable. Here are some methods to solve the above mentioned problem\n",
        "                          #OR\n",
        "                          #Formula -> num*(num+1)/2\n",
        "\n",
        "\n",
        "num, sum = 6,0\n",
        "for i in range (num+1):\n",
        "  sum+= i\n",
        "  print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uVEdWkt2BSx-",
        "outputId": "0f591120-a07f-436e-b811-2b333e1bf318"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "3\n",
            "6\n",
            "10\n",
            "15\n",
            "21\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Find the Sum of Numbers in a given Range in Python\n",
        "#Given two integer inputs as the range [low , high], the objective is to find the sum of all the numbers that lay in the given integer inputs as interval. In order to do so we usually iterate through the the numbers in the given range and keep appending them to the sum variable. Here are few methods to solve the above mentioned problem in Python Language.\n",
        "\n",
        "num1,num2 = 3,6\n",
        "sum = 0\n",
        "for i in range(num1,num2+1):\n",
        "  sum+=i\n",
        "  print(sum)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FRM1WeCoCIEm",
        "outputId": "accbd7b0-34fe-4129-8b1d-e2373f9b774e"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "7\n",
            "12\n",
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Find the Sum of Numbers in a given Range in Python\n",
        "#Given two integer inputs as the range [low , high], the objective is to find the sum of all the numbers that lay in the given integer inputs as interval. In order to do so we usually iterate through the the numbers in the given range and keep appending them to the sum variable. Here are few methods to solve the above mentioned problem in Python Language.\n",
        "\n",
        "                        # FORMULA#\n",
        "\n",
        "\n",
        "  #Formula to Find the Sum of Numbers in an Interval\n",
        "\n",
        "#The formula to find the sum of n natural numbers is:\n",
        "#Sum = n * ( n + 1 ) / 2\n",
        "\n",
        "#Therefore in order to find the sum in a given interval we'll minus the sum of the numbers until the lower range from the whole sum and add an offset as the lowest bound is itself included in the summation. Hence the final formula is :\n",
        "#Sum = b * ( b + 1 ) / 2 – a * ( a + 1 ) / 2 + a .\n",
        "\n",
        "num1, num2 = 3, 6\n",
        "sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)\n",
        "print(sum)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9IFcKYs6DvXT",
        "outputId": "781d0641-3732-4e9d-d47d-5ce76aa2b622"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Find the Greatest of Two Numbers in Python\n",
        "#Given two integer inputs, the objective is to find the largest number among the two integer inputs. In order to do so we usually use if-else statements to check which one’s greater. Here are some of the Python methods to solve the above mentioned problem.\n",
        "\n",
        "num1 ,num2 = 3,9\n",
        "if num1>num2:\n",
        "  print(num1)\n",
        "else:\n",
        "  print(num2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZF97eD2ZGMeR",
        "outputId": "4c0daf1a-a5dd-454c-9b31-ca2ef79d63d5"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Find the Greatest of Two Numbers in Python\n",
        "#Given two integer inputs, the objective is to find the largest number among the two integer inputs. In order to do so we usually use if-else statements to check which one’s greater. Here are some of the Python methods to solve the above mentioned problem.\n",
        "\n",
        "num1, num2 = 30 , 59\n",
        "print(max(num1,num2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j-0r0tE9Gtw-",
        "outputId": "d7472168-d17a-447a-987a-ef58587f434f"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "59\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Find the Greatest of the Three Numbers​ in Python\n",
        "#Given three integers as inputs the objective is to find the greatest among them. In order to do so we check and compare the three integer inputs with each other and which ever is the greatest we print that number. Here are some methods to solve the above problem.\n",
        "\n",
        "num1, num2, num3 = 10, 3456,30\n",
        "if num1>num2 and num1>num3:\n",
        "  print(num1)\n",
        "elif num2> num1 and num2 >num3:\n",
        "  print(num2)\n",
        "else:\n",
        "  print(num3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZK5qCzXKHQNb",
        "outputId": "e141e607-faaf-43d5-8b98-5829de3341b8"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3456\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Leap Year Program in Python\n",
        "\n",
        "#Check Whether a Year is a Leap Year or Not in Python\n",
        "#Given an integer input as the year, the objective is to Check if a Year is a Leap Year or Not in Python Language. To do so we’ll check each condition mentioned below in the blue box. It either of the conditions is satisfied, the year is a leap year. It’s not otherwise. Here are some methods to check whether or not it’s a leap year\n",
        "\n",
        "leap = 2024\n",
        "if leap%4 == 0 and leap%100!= 0:\n",
        "  print(\"it is leap year\")\n",
        "else:\n",
        "  print(\"it is not leap year\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PMAg-vQSIElr",
        "outputId": "8aee4039-a53d-4d2d-867a-c639785f2a16"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "it is leap year\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Leap Year Program in Python\n",
        "\n",
        "#Check Whether a Year is a Leap Year or Not in Python\n",
        "#Given an integer input as the year, the objective is to Check if a Year is a Leap Year or Not in Python Language. To do so we’ll check each condition mentioned below in the blue box. It either of the conditions is satisfied, the year is a leap year. It’s not otherwise. Here are some methods to check whether or not it’s a leap year\n",
        "\n",
        "import calendar\n",
        "year = int(input(\"enter a year leap:\"))\n",
        "if calendar.isleap(year):\n",
        "  print( \"it is a leap year\")\n",
        "else:\n",
        "  print(\"it is not leap year\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a2s1zioyI9LP",
        "outputId": "a00a6c98-3de7-42b0-cd58-a1658c8b7f7d"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a year leap:2024\n",
            "it is a leap year\n"
          ]
        }
      ]
    }
  ]
}