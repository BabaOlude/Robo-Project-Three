[![Udacity - Robotics NanoDegree Program](https://s3-us-west-1.amazonaws.com/udacity-robotics/Extra+Images/RoboND_flag.png)](https://www.udacity.com/robotics)

# RoboND-Perception-Exercises
These exercises are part of the perception lessons in the [Udacity Robotics Nanodegree Program](https://www.udacity.com/robotics) In these exercises, you will perform object segmentation on 3D point cloud data using `python-pcl` to leverage the power of the [Point Cloud Library](http://pointclouds.org/).  In Exercise 1, you'll get some practice performing filtering and RANSAC plane segmentation, and in Exercise-2 you'll write a ROS node to perform those functions as well as Euclidean Clustering for object segmentation! Once you have cloned or downloaded this repo in the provided VM, you can follow the steps given below for installation.


## Project: Perception Pick & Place


# Required Steps for a Passing Submission:
1. Extract features and train an SVM model on new objects (see `pick_list_*.yaml` in `/pr2_robot/config/` for the list of models you'll be trying to identify). 
2. Write a ROS node and subscribe to `/pr2/world/points` topic. This topic contains noisy point cloud data that you must work with.
3. Use filtering and RANSAC plane fitting to isolate the objects of interest from the rest of the scene.
4. Apply Euclidean clustering to create separate clusters for individual items.
5. Perform object recognition on these objects and assign them labels (markers in RViz).
6. Calculate the centroid (average in x, y and z) of the set of points belonging to that each object.
7. Create ROS messages containing the details of each object (name, pick_pose, etc.) and write these messages out to `.yaml` files, one for each of the 3 scenarios (`test1-3.world` in `/pr2_robot/worlds/`).  [See the example `output.yaml` for details on what the output should look like.](https://github.com/udacity/RoboND-Perception-Project/blob/master/pr2_robot/config/output.yaml)  
8. Submit a link to your GitHub repo for the project or the Python code for your perception pipeline and your output `.yaml` files (3 `.yaml` files, one for each test world).  You must have correctly identified 100% of objects from `pick_list_1.yaml` for `test1.world`, 80% of items from `pick_list_2.yaml` for `test2.world` and 75% of items from `pick_list_3.yaml` in `test3.world`.


# Extra Challenges: Complete the Pick & Place
7. To create a collision map, publish a point cloud to the `/pr2/3d_map/points` topic and make sure you change the `point_cloud_topic` to `/pr2/3d_map/points` in `sensors.yaml` in the `/pr2_robot/config/` directory. This topic is read by Moveit!, which uses this point cloud input to generate a collision map, allowing the robot to plan its trajectory.  Keep in mind that later when you go to pick up an object, you must first remove it from this point cloud so it is removed from the collision map!


11. If everything was done correctly, when you pass the appropriate messages to the `pick_place_routine` service, the selected arm will perform pick and place operation and display trajectory in the RViz window
12. Place all the objects from your pick list in their respective dropoff box and you have completed the challenge!


## [Rubric](https://review.udacity.com/#!/rubrics/1067/view) Points

![demo-1](https://user-images.githubusercontent.com/20687560/28748231-46b5b912-7467-11e7-8778-3095172b7b19.png)

#### Rubric Points 
1) All your python code (make sure to add comments at appropriate places in your code)
2) Three output yaml files that contain PickPlace request parameters: output_1.yaml, output_2.yaml, output_3.yaml.
3) Writeup report (md or pdf file)

### Pick and Place Setup

See my results:
Example - `test*.world`
Example - `pick_list_*.yaml`
 
![demo-2](https://user-images.githubusercontent.com/20687560/28748286-9f65680e-7468-11e7-83dc-f1a32380b89c.png)

Code Discussion: 
I created my code based on the Udacity curriculum. I basically followed along and created code to match each question that was asked of students. I developed the code to get the results in each step until I was finished. I learned a lot. I think my code would will work under many different circumstances.   



