{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPVxPZJ/Agvvyt36XxBoqPZ",
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
        "<a href=\"https://colab.research.google.com/github/pari1691/PYTHON-DSLAB/blob/main/1)Deletion_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self, data=None):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class SLinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def Atbegining(self, data_in):\n",
        "        NewNode = Node(data_in)\n",
        "        NewNode.next = self.head\n",
        "        self.head = NewNode\n",
        "\n",
        "    def RemoveNode(self, Removekey):\n",
        "        HeadVal = self.head\n",
        "\n",
        "        if HeadVal is not None:\n",
        "            if HeadVal.data == Removekey:\n",
        "                self.head = HeadVal.next\n",
        "                HeadVal = None\n",
        "                return\n",
        "\n",
        "        while HeadVal is not None:\n",
        "            if HeadVal.data == Removekey:\n",
        "                break\n",
        "\n",
        "            prev = HeadVal\n",
        "            HeadVal = HeadVal.next\n",
        "\n",
        "        if HeadVal is None:\n",
        "            return\n",
        "\n",
        "        prev.next = HeadVal.next\n",
        "        HeadVal = None\n",
        "\n",
        "    def LListprint(self):\n",
        "        printval = self.head\n",
        "\n",
        "        while printval:\n",
        "            print(printval.data)\n",
        "            printval = printval.next\n",
        "\n",
        "\n",
        "llist = SLinkedList()\n",
        "\n",
        "llist.Atbegining(\"Mon\")\n",
        "llist.Atbegining(\"Tue\")\n",
        "llist.Atbegining(\"Wed\")\n",
        "llist.Atbegining(\"Thu\")\n",
        "\n",
        "llist.RemoveNode(\"Tue\")\n",
        "\n",
        "llist.LListprint()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wvEa0ikJaM7Y",
        "outputId": "e07f014f-2bd5-4a69-bd98-cc0d71122908"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Thu\n",
            "Wed\n",
            "Mon\n"
          ]
        }
      ]
    }
  ]
}
