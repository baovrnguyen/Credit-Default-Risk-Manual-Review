{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMOtya63XFKMoPVUEFEF+bE",
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
        "<a href=\"https://colab.research.google.com/github/baovrnguyen/Credit-Default-Risk-Manual-Review/blob/main/fetch_data_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install ucimlrepo pandas numpy scikit-learn"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6NTaAol0-vmw",
        "outputId": "6815465f-34bd-4271-9419-aa4c30df7174"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting ucimlrepo\n",
            "  Downloading ucimlrepo-0.0.7-py3-none-any.whl.metadata (5.5 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.13/dist-packages (2.2.3)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.13/dist-packages (2.4.6)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.13/dist-packages (1.6.1)\n",
            "Requirement already satisfied: certifi>=2020.12.5 in /usr/local/lib/python3.13/dist-packages (from ucimlrepo) (2026.10.23)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.13/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.13/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.13/dist-packages (from pandas) (2026.6)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.13/dist-packages (from scikit-learn) (1.16.3)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.13/dist-packages (from scikit-learn) (1.6.0)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.13/dist-packages (from scikit-learn) (3.7.0)\n",
            "Requirement already satisfied: cloudpickle>=3.0 in /usr/local/lib/python3.13/dist-packages (from joblib>=1.2.0->scikit-learn) (3.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.13/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Downloading ucimlrepo-0.0.7-py3-none-any.whl (8.0 kB)\n",
            "Installing collected packages: ucimlrepo\n",
            "Successfully installed ucimlrepo-0.0.7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qfBfN88T-SVB",
        "outputId": "50ce3505-c20e-4779-8341-2ed2ebd8eb27"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fetching UCI Default of Credit Card Clients dataset...\n",
            "Dataset saved to: data/credit_default.csv\n",
            "Rows: 30,000\n",
            "Columns: 24\n"
          ]
        }
      ],
      "source": [
        "# Fetch UCI Default of Credit Card Clients Dataset\n",
        "\n",
        "from pathlib import Path\n",
        "import pandas as pd\n",
        "from ucimlrepo import fetch_ucirepo\n",
        "\n",
        "\n",
        "DATA_DIR = Path(\"data\")\n",
        "DATA_FILE = DATA_DIR / \"credit_default.csv\"\n",
        "\n",
        "\n",
        "def fetch_data():\n",
        "    DATA_DIR.mkdir(exist_ok=True)\n",
        "\n",
        "    if DATA_FILE.exists():\n",
        "        print(f\"Dataset already exists: {DATA_FILE}\")\n",
        "        return\n",
        "\n",
        "    print(\"Fetching UCI Default of Credit Card Clients dataset...\")\n",
        "\n",
        "    credit_default = fetch_ucirepo(id=350)\n",
        "\n",
        "    X = credit_default.data.features.copy()\n",
        "    y = credit_default.data.targets.copy()\n",
        "\n",
        "    df = pd.concat([X, y], axis=1)\n",
        "    df.to_csv(DATA_FILE, index=False)\n",
        "\n",
        "    print(f\"Dataset saved to: {DATA_FILE}\")\n",
        "    print(f\"Rows: {len(df):,}\")\n",
        "    print(f\"Columns: {df.shape[1]}\")\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    fetch_data()"
      ]
    }
  ]
}
