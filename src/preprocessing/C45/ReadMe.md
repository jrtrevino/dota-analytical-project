- ltran73@calpoly.edu
- vanderzw@calpoly.edu

#Lab report
lab report include all the parameters we ran
# How to run each file

pip install -r requirements.txt

##main.py
```bash
python3 main.py 
output: an input file for InduceC45.py to generate a decision tree
```

###players_rating_prediction.py
```bash
python3 players_rating_prediction.py
output: a confusion matrix of prediction for predicting match outcome based purely on player's rating
```


##InduceC45.py
- python3 InduceC45.py (csvfile) (threshold) (gain_ratio) (optional.txt)
- csvfile ---> it's an input file for instance nursery.csv
- threshold ---> a value between 0 to 1
- gain_ratio ---> a value of 0 or 1, with 1 being using the infoGainRatio to determine the attribute and 0 is just informationGain
- optional.txt ----> a file of "0" or "1" indicating which attributes to omit. Remember that the class variable must always be '1'

-- output of tree will be 'filename-results.out' file (filename without the .csv)
##classify.py 
- make sure the InduceC45 is ran first to generate a tree!
- python3 classify.py (csvfile) (output.json)
- csvfile ---> must make sure it's the same csvfile as the generated tree!
- output.json ---> this is the imported tree, if this argument is left out, it will use filename-results.out (filename without csv) as a default

-- output will be in console displaying how many are accurately printed
