# What is lambdata?
lambdata is a collection of data science helper functions as well as a couple class objects that can be instantiated. In addition to the helper functions and class objects there is a unit test file that can be used to run tests on squart root functions.   

Simply accessing this repo on your terminal after cloning it from GitHub will allow you to go into the respective files. 

## The Helper Functions  
The helper functions are found in lambdata_ethanmjansen, in the df_utils.py file. In a python shell type in the following code: ```from lambdata_ethanmjansen import df_utils as du```  
Once imported, use ```du.split(df)``` and ```du.ttester(df, column1, column2)``` to split a data frame or to run a ttest on two columns and give a p value.  
## The Classes  
There are two classes, Movie() and and Plant_Care() that can also be found in lambdata_ethnamjansen, in the plant_care.py and movie.py files. In a python shell type the following code: ```from lambdata_ethanmjansen import plant_care as pc```  
Once imported, you can instantiate the classes and run their respective methods. You can do the same process with movie.py.   
## The Unit Test  
The unit test can be found in tests_ds10 folder. By going into tests_ds10 you can simply type in the code: ```python sqrt_test.py```  
By doing so you will run a test on that file and see how it works. You may also choose to run a pytest on datafunctions_test.py by typing in: ```pytest datafunctions_test.py``` whih will confirm the validity of the function found in datafunctions.py.   