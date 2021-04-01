# N_gram_Gen_Dialogue_Analysis

# Data Pre-Processing 
In order to use this scripts ensure that the chat logs have been preprocessed and the dataset contains only the following columns:
[SessionID, UserID, Speaker, Utterance, Tag] saved in a .csv file e.g. sample_corpus1.csv

# About Corpus:  
The dialogue corpus in sample_corpus1 shows a one-to-one turn-taking interaction where each speaker takes a turn and each turn is an utterance. 
The dialogue corpus in sample_corpus2 shows does not necessarily follow a one-to-one turn-taking paradigm. Each speaker can have multiple turns before their partner responses. This shows a more naturalistic exchange between two speakers. 

Note: Utterances can be split in either of the cases above to capture appropriate dialogue moves. Also, splitting dialogues in a one-to-one dialogue corpus can result in loss of the one-to-one speaker flow. 

# Step 1: Generate the n-grams for student partner exchanges (G_stu, G_par) or (G_stu, G_par, S_par).
Note: Each participant is captured as a student and a partner

//Generating n-grams (unigrams and bigrams) and assigning "_stu" and "_par"  
Assuming no error: an output file will be generated in the same directory ngram_output.csv
The ngram_output will contain the [User, Ngram, Utterance 1, Utterance 2]

In the command line: 
- Go to directory of your scripts
- Enter $ python3 ngram_gen.py sample_corpus1.csv
- click enter

    Output:
    - a csv file (output_corpus1.csv) with all generated unigrams and bigrams, and their corresponding utterances (remove block comments to generate trigrams)
    - Total number of unigrams: (48)
    - Total number of bigrams: (43)


# Step 2: Build a datatable that shows the count of n-grams for each student within their session

//Generating ngram datatable
In the command line: 
- Go to directory of your scripts
- Enter $ python3 ngram_datatable.py output_corpus1.csv
- click enter 

    Output: 
    -  a csv file (output_ngramTable.csv) of n-grams predictors 

# Step 3: Apply a threshold to intentionally include ngrams that occur in X% of converstions (test X for 10, 25, 33 and 50) to establish the most appropriate threshold for the dataset wih respect to the sample. 
Note: The resulting total number of ngrams will be used to run a generalized regression model. Best practices for running regression model encourages the number of predictors less than the sample size. However, since we are using an exhaustive best subset method, the number of ngramas can be greater than the sample size, within a reasonable threshold.

For instance, in the output_ngramTable.csv, sample size is 10, and the number of n-grams is (48+43 = 91). 
In the dimension_reducer.py, test different values of X to establish an appropriate number of ngram predictors.

In command line: 
- Go to directory of your scripts
- Enter $ python3 ngram_dimensionReducer.py output_ngramTable.csv
- click enter 

    Output: 
    - a csv file (output_ngramTable_Xpercent.csv) of X% of the n-grams predictors 
    - a csv file (output_ngram_numRow.csv) of the ngrams and the number of rows (i.e. number of sessions theuy occur in (not the number of times they occur***))

# Step 4: Statistical analysis - Generalized Regression using Best subset selection method
Go To JMP (the following is based on JMP Pro 15): 
- open the resulting reduced n-grams predictors dataset (output_ngramTable_Xpercent.csv)
- Add a new columns with outcomes measures 
- Go to Analyze -> Fit Model
    - select all predictors and add to "Construct Model Effects"
    - select outcome variable and add to "Pick Role Variables" 
- Go to "Personality"
    - select "Generalized Regression" 
    - click Run
- In Model Launch, go to  "Estimation Method" 
    - select Best Subset
    - click Go 
