- ltran73@calpoly.edu
- vanderzw@calpoly.edu

#Lab report
lab report include all the parameters we ran
# How to run each file

pip install -r requirements.txt

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

##validation.py
- python3 validation.py (csvfile) (threshold) (k) (gain_ratio)
- csvfile --> a csv file that you want to use as input
- threshold --> what threshold to put for c45 algorithm
- k --> the number of splits across the table
- gain_ratio --> to use information gain or information gain ratio
   -- 1 is information gain ratio and 0 is information gain
   
##validationRandomForest.py
- similar to the other cross evaluation but this time it would just be 10 splits across the table automatically
- python3 validationRandomForst.py (csvfile) (threshold) (attributes) (data) (trees) (gain_ratio)
- threshold --> what threshold to put for c45 algorithm
- attributes --> how many attributes to sample out from all the attributes of that data list. This number should be less than the total amount of attributes
- data --> subset of data amount of the entire data set
- trees --> number of trees you want the random forest to have
- gain_ratio --> 1 is information gain ratio and 0 is information gain
   
##knn.py
- python3 knn.py (csvfile) (k)
- csvfile --> data set you want to use
- k --> the number of closest neighbor to use against

#Each out file threshold value (use these threshold values to yield a high percentage on the prediction)
- adult+stretch-results.out ---> threshold=.25
- adult-stretch-result.out ---> threshold=.25
- yellow-small+adult-stretch-result.out ---> threshold=.1
- yellow-small-results.out ---> threshold=.25
- agaricus-lepiota-results.out ---> threshold=.1
- nursery-results.out ---> threshold=.1 yields 99.81 % accuracy but it takes a really long time to classify this tree so it's very time consuming, while using a .25 will yields lower accuracy but better time execution

