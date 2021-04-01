import pandas as pd
import csv, sys


#sys.argv will contain["python", "ngram_dimensionReducer.py", "output_corpus1.csv"]
if len(sys.argv) >1:
    infile =  sys.argv[1]

    #generate a dataframe from the csv
    
    df = pd.read_csv(infile, encoding='ISO-8859-1')


    writer = csv.writer(open('output_ngram_numRow.csv', 'w'))

    writer.writerow(["Ngram", "Number of rows"])

    #apply the choosen dimension threshold to the n-gram predictors
    num_sessions = len(df.iloc[:, 1:])/2
    for col in df.iloc[:, 1:]:
        sparsity_counter = 0
        for row in df.iloc[:, 1:][col]:
            if(row != 0):
                sparsity_counter += 1

        writer.writerow([col, sparsity_counter])


        if(sparsity_counter < (.5* num_sessions)): # appears in 50% or mroe of sessions: X = 50% 
            df.iloc[:, 1:].drop(col, axis = 1, inplace = True)

        # output_df = df_username_col.append(df)

    df.to_csv('output_ngramTable_Xpercent.csv')