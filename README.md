[![Udacity - Robotics NanoDegree Program](https://s3-us-west-1.amazonaws.com/udacity-robotics/Extra+Images/RoboND_flag.png)](https://www.udacity.com/robotics)

## Project: Perception Pick & Place

## [Rubric Points](https://review.udacity.com/#!/rubrics/1067/view) Points 
1) My python code 

# My Steps:
1. I extracted features and trained an SVM model on new objects 
2. I wrote a ROS node and subscribed to `/pr2/world/points` 
3. I used filtering and RANSAC plane fittings to isolate the objects of interest from the rest of the scene.
4. I applied Euclidean clustering to create separate clusters for individual items.
5. I performed object recognition on these objects and assigned them labels (RViz).
6. I calculated the centroid (average in x, y and z) of the set of points belonging to that each object.
7. I created ROS messages containing the details of each object (name, pick_pose, etc.) and wrote these messages out to `.yaml` files, one for each of the 3 scenarios (`test1-3.world` in `/pr2_robot/worlds/`).

#### Picture Output: Yaml files that contain PickPlace request parameters: output_1.yaml, output_2.yaml, output_3.yaml.

### Pick and Place Setup

See my results:
Example - `test*.world`
Example - `pick_list_*.yaml`
 
![demo-2](https://user-images.githubusercontent.com/20687560/28748286-9f65680e-7468-11e7-83dc-f1a32380b89c.png)

Code Discussion: 
I created my code based on the Udacity curriculum. I basically followed along and created code to match each question that was asked of students. I developed the code to get the results in each step until I was finished. I learned a lot. I think my code would will work under many different circumstances.   
