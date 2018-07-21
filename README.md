[![Udacity - Robotics NanoDegree Program](https://s3-us-west-1.amazonaws.com/udacity-robotics/Extra+Images/RoboND_flag.png)](https://www.udacity.com/robotics)

This is my submission for project three of the Udacity RoboND. I will be using active and passive sensors and an RGB-D camera in a simulated environment to demonstrate a PR2 robot picking and placing objects into bins.

In this repo you'll find the files needed in order to perform the project. You can find the output messages in the yaml files.

Rubric Points:

Exercise 1 - The pcl_callback() function within the template Python script has been filled out to include filtering and RANSAC plane fitting.

Exercise 2 - Steps for cluster segmentation have been added to the pcl_callback() function in the template Python script.

Exercise 3 - Both compute_color_histograms() and compute_normal_histograms() functions have been filled out and SVM has been trained using train_svm.py. Please see below for a snapshot of my normalized confusion matrix (output from train_svm.py in your writeup / README. Object recognition steps have been implemented in the pcl_callback() function within template Python script.

This repo contains the writeup.md file and the following documents:

    object_recognition.py
    capture_features.py
    train_svm.py
    output_1.yaml, output_2.yaml, and output_3.yaml
    
In order to setup the project I followed the instructions in the three perception exercises. I order to perform the project I followed the instructions in the perception project from the curriculum.

Once those steps were complete I was ready to go. I had the sensor_stick and pr2_robot packages installed. At this point I copied my object_recognition.py script to my scripts directory in catkin. Then I copied features.py to my sensor stick directory in catkin. The instructions then allowed me to train my model and do object recognition.

After the creation of the perception pipeline I instituted the object recognition. The main part of the project was running the pick lists from the yaml files and demonstrating the object recognition. 

In order to fulfill the requirements in the curriculum my code recognized 100% of the object in test1.world, 80% of the objects in test2.world, and 75% of the objects in test3.world. My code created the output files output_1.yaml, output_2.yaml, and output_3.yaml. 


# Project Pictures

Setup:



![demo-1](https://user-images.githubusercontent.com/20687560/28748231-46b5b912-7467-11e7-8778-3095172b7b19.png)

Gazebo world:
- Robot

- Table arrangement

- Three target objects on the table

- Dropboxes on either sides of the robot




Robot and a partial collision map displayed:

![demo-2](https://user-images.githubusercontent.com/20687560/28748286-9f65680e-7468-11e7-83dc-f1a32380b89c.png)


