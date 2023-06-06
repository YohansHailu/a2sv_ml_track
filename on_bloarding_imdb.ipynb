{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/YohansHailu/a2sv_ml_track/blob/main/on_bloarding_imdb.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "id": "f2c2a5a3",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f2c2a5a3",
        "outputId": "c7a50689-bf27-4cb7-83dc-fa242dc99507"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Exception reporting mode: Minimal\n"
          ]
        }
      ],
      "source": [
        "##\n",
        "import os\n",
        "os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'\n",
        "%xmode Minimal"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "id": "8db3a3bb",
      "metadata": {
        "id": "8db3a3bb"
      },
      "outputs": [],
      "source": [
        "##\n",
        "import pandas as pd "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "7533f855",
      "metadata": {
        "id": "7533f855"
      },
      "outputs": [],
      "source": [
        "imdb_top = pd.read_csv(\"./imdb_top_1000.csv\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "id": "57314247",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 485
        },
        "id": "57314247",
        "outputId": "ae9d767a-0565-41f2-900f-7b2fbb6c7eda"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                         Poster_Link  \\\n",
              "0  https://m.media-amazon.com/images/M/MV5BMDFkYT...   \n",
              "1  https://m.media-amazon.com/images/M/MV5BM2MyNj...   \n",
              "2  https://m.media-amazon.com/images/M/MV5BMTMxNT...   \n",
              "\n",
              "               Series_Title Released_Year Certificate  Runtime  \\\n",
              "0  The Shawshank Redemption          1994           A  142 min   \n",
              "1             The Godfather          1972           A  175 min   \n",
              "2           The Dark Knight          2008          UA  152 min   \n",
              "\n",
              "                  Genre  IMDB_Rating  \\\n",
              "0                 Drama          9.3   \n",
              "1          Crime, Drama          9.2   \n",
              "2  Action, Crime, Drama          9.0   \n",
              "\n",
              "                                            Overview  Meta_score  \\\n",
              "0  Two imprisoned men bond over a number of years...        80.0   \n",
              "1  An organized crime dynasty's aging patriarch t...       100.0   \n",
              "2  When the menace known as the Joker wreaks havo...        84.0   \n",
              "\n",
              "               Director           Star1           Star2          Star3  \\\n",
              "0        Frank Darabont     Tim Robbins  Morgan Freeman     Bob Gunton   \n",
              "1  Francis Ford Coppola   Marlon Brando       Al Pacino     James Caan   \n",
              "2     Christopher Nolan  Christian Bale    Heath Ledger  Aaron Eckhart   \n",
              "\n",
              "            Star4  No_of_Votes        Gross  \n",
              "0  William Sadler      2343110   28,341,469  \n",
              "1    Diane Keaton      1620367  134,966,411  \n",
              "2   Michael Caine      2303232  534,858,444  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a8716e00-d0e6-4fc5-bb29-e15d212789e1\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Poster_Link</th>\n",
              "      <th>Series_Title</th>\n",
              "      <th>Released_Year</th>\n",
              "      <th>Certificate</th>\n",
              "      <th>Runtime</th>\n",
              "      <th>Genre</th>\n",
              "      <th>IMDB_Rating</th>\n",
              "      <th>Overview</th>\n",
              "      <th>Meta_score</th>\n",
              "      <th>Director</th>\n",
              "      <th>Star1</th>\n",
              "      <th>Star2</th>\n",
              "      <th>Star3</th>\n",
              "      <th>Star4</th>\n",
              "      <th>No_of_Votes</th>\n",
              "      <th>Gross</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>https://m.media-amazon.com/images/M/MV5BMDFkYT...</td>\n",
              "      <td>The Shawshank Redemption</td>\n",
              "      <td>1994</td>\n",
              "      <td>A</td>\n",
              "      <td>142 min</td>\n",
              "      <td>Drama</td>\n",
              "      <td>9.3</td>\n",
              "      <td>Two imprisoned men bond over a number of years...</td>\n",
              "      <td>80.0</td>\n",
              "      <td>Frank Darabont</td>\n",
              "      <td>Tim Robbins</td>\n",
              "      <td>Morgan Freeman</td>\n",
              "      <td>Bob Gunton</td>\n",
              "      <td>William Sadler</td>\n",
              "      <td>2343110</td>\n",
              "      <td>28,341,469</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>https://m.media-amazon.com/images/M/MV5BM2MyNj...</td>\n",
              "      <td>The Godfather</td>\n",
              "      <td>1972</td>\n",
              "      <td>A</td>\n",
              "      <td>175 min</td>\n",
              "      <td>Crime, Drama</td>\n",
              "      <td>9.2</td>\n",
              "      <td>An organized crime dynasty's aging patriarch t...</td>\n",
              "      <td>100.0</td>\n",
              "      <td>Francis Ford Coppola</td>\n",
              "      <td>Marlon Brando</td>\n",
              "      <td>Al Pacino</td>\n",
              "      <td>James Caan</td>\n",
              "      <td>Diane Keaton</td>\n",
              "      <td>1620367</td>\n",
              "      <td>134,966,411</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>https://m.media-amazon.com/images/M/MV5BMTMxNT...</td>\n",
              "      <td>The Dark Knight</td>\n",
              "      <td>2008</td>\n",
              "      <td>UA</td>\n",
              "      <td>152 min</td>\n",
              "      <td>Action, Crime, Drama</td>\n",
              "      <td>9.0</td>\n",
              "      <td>When the menace known as the Joker wreaks havo...</td>\n",
              "      <td>84.0</td>\n",
              "      <td>Christopher Nolan</td>\n",
              "      <td>Christian Bale</td>\n",
              "      <td>Heath Ledger</td>\n",
              "      <td>Aaron Eckhart</td>\n",
              "      <td>Michael Caine</td>\n",
              "      <td>2303232</td>\n",
              "      <td>534,858,444</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a8716e00-d0e6-4fc5-bb29-e15d212789e1')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a8716e00-d0e6-4fc5-bb29-e15d212789e1 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a8716e00-d0e6-4fc5-bb29-e15d212789e1');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "##\n",
        "imdb_top.head(3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "id": "74c2f8eb",
      "metadata": {
        "lines_to_next_cell": 2,
        "id": "74c2f8eb"
      },
      "outputs": [],
      "source": [
        "## name of the columns\n",
        "columns_names = list(imdb_top.columns)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "e72747bd",
      "metadata": {
        "id": "e72747bd"
      },
      "outputs": [],
      "source": [
        "## average rating\n",
        "rating_average = imdb_top[\"IMDB_Rating\"].mean()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "id": "0593a2a9",
      "metadata": {
        "lines_to_next_cell": 2,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0593a2a9",
        "outputId": "939f1543-bac7-4789-a7b4-f7028683a080"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0                   Drama\n",
              "1            Crime, Drama\n",
              "2    Action, Crime, Drama\n",
              "3            Crime, Drama\n",
              "4            Crime, Drama\n",
              "Name: Genre, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "##\n",
        "imdb_top[\"Genre\"].head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "id": "03cc1e03",
      "metadata": {
        "id": "03cc1e03"
      },
      "outputs": [],
      "source": [
        "## gfinal_result.to_csv(\"final_result\", index=False)\n",
        "print(\"file saved\")et all generes method-1\n",
        "uniq_genres  = set()\n",
        "for row in imdb_top[\"Genre\"]:\n",
        "    uniq_genres = uniq_genres | set(row.split(\",\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "id": "e3a018e4",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e3a018e4",
        "outputId": "3d5e73f4-edf6-4997-e179-ccc55ce36f6c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[' Action', 'Family', 'Biography', ' History', ' Sport', 'Western', ' Biography', 'Mystery', 'Fantasy', 'Crime', ' Crime', ' Thriller', 'Horror', ' Film-Noir', 'Film-Noir', 'Thriller', ' Horror', ' Fantasy', ' Family', ' Adventure', ' Drama', ' Western', 'Adventure', ' Musical', ' Music', ' Mystery', 'Action', ' Comedy', 'Comedy', ' War', 'Animation', 'Drama', ' Sci-Fi', ' Romance']\n"
          ]
        }
      ],
      "source": [
        "uniq_genres = list(uniq_genres)\n",
        "print(uniq_genres)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "id": "4c21a8a7",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "4c21a8a7",
        "outputId": "6860088b-4913-4f88-f4d6-e56e81fee98b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   rating_average                                      columns_names  \\\n",
              "0          7.9493  Poster_Link,Series_Title,Released_Year,Certifi...   \n",
              "\n",
              "                                     all_uniq_genres  \n",
              "0   Action,Family,Biography, History, Sport,Weste...  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-28ff236a-f10a-438a-954e-fa38ddb0c305\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>rating_average</th>\n",
              "      <th>columns_names</th>\n",
              "      <th>all_uniq_genres</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.9493</td>\n",
              "      <td>Poster_Link,Series_Title,Released_Year,Certifi...</td>\n",
              "      <td>Action,Family,Biography, History, Sport,Weste...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-28ff236a-f10a-438a-954e-fa38ddb0c305')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-28ff236a-f10a-438a-954e-fa38ddb0c305 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-28ff236a-f10a-438a-954e-fa38ddb0c305');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ],
      "source": [
        "rows = [rating_average, \",\".join(columns_names), \",\".join(uniq_genres)]\n",
        "columns=[\"rating_average\", \"columns_names\", \"all_uniq_genres\"]\n",
        "final_result = pd.DataFrame([rows], columns=columns)\n",
        "final_result.head()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "id": "643c64f2",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "643c64f2",
        "outputId": "74196911-a9b8-498c-b5e8-d63d91bf9b6c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "file saved\n"
          ]
        }
      ],
      "source": [
        "final_result.to_csv(\"final_result\", index=False)\n",
        "print(\"file saved\")"
      ]
    }
  ],
  "metadata": {
    "jupytext": {
      "cell_metadata_filter": "-all",
      "main_language": "python",
      "notebook_metadata_filter": "-all"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "language_info": {
      "name": "python"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}