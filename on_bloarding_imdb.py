##
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
%xmode Minimal

##
import pandas as pd 

imdb_top = pd.read_csv("./imdb_top_1000.csv")

##
imdb_top.head(3)

## name of the columns
columns_names = list(imdb_top.columns)


## average rating
rating_average = imdb_top["IMDB_Rating"].mean()

##
imdb_top["Genre"].head()


## get all generes method-1
uniq_genres  = set()
for row in imdb_top["Genre"]:
    uniq_genres = uniq_genres | set(row.split(","))

uniq_genres = list(uniq_genres)
print(uniq_genres)

## another method clever here
#genre_rows = imdb_top["Genre"].str.split(",")
#uniq_geners = set().union(*genre_rows)
#uniq_genres 

## saving the uniq column names to csv

rows = [rating_average, ",".join(columns_names), ",".join(uniq_genres)]
columns=["rating_average", "columns_names", "all_uniq_genres"]
final_result = pd.DataFrame([rows], columns=columns)
final_result.head()
##
final_result.to_csv("final_result", index=False)
print("file saved")


