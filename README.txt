Name: spuran yarram

PACKAGES USED :
NUMPY,SKLEARN,PANDAS
Platform:
IPYTHON for the main code.

OS: Ubuntu 14.04
Python version:2.7
Miniconda 3.0
There are 3 python files attached : read_train.py,final.py,test_name.py

Step1:
Download and unzip the data file from the kaggle  which contains folders of train and test images and a csv file.
Make note of the path in which these three are present.

Step2:
Run the python file read_train.py in which you change the "path" accordingly.
This will out put a csv file "new_train11.csv".
##for the purpose of this project  presentation i have attached the csv file in which i have removed the error images which were identified and their labels##

Step3:
Run the test_name.py file to get the test ids from the images in the folder this will write these ids into a "test.csv"
Make sure you the relative_path accoridngly
##for the purpose of this project presentation i have attached the test.csv file in which the two error images have been removed##

Step4:
If you have IPYTHON then use the final1.ipnyb file or use the final.py for normal pyhton version.
Make sure you change the data_root and path accordingly

This will output two csv files submissioon1.csv and submission_label.csv please merge them.

##as the issue was when i wrote them together into a csv there was some distubance in the output in some places so i did it manually ##
## i tried using different approaches but the result was the same##

And also we need to append the two error images in the test data they were  79616.jpg ,76787.jpg.
So append the following two rows to final submission:(assiging equal probabality)
79616 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125
76787 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125







