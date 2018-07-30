#!/usr/bin/env python

# Import modules
from pcl_helper import *

# TODO: Define functions as required

# Callback function for your Point Cloud Subscriber
def pcl_callback(pcl_msg):

    # TODO: Convert ROS msg to PCL data

    # TODO: Voxel Grid Downsampling

    # TODO: PassThrough Filter


    # TODO: RANSAC Plane Segmentation

    # TODO: Extract inliers and outliers

    # TODO: Euclidean Clustering

    # TODO: Create Cluster-Mask Point Cloud to visualize each cluster separately

    # TODO: Convert PCL data to ROS messages

    # TODO: Publish ROS messages

for index, pts_list in enumerate(cluster_indices):
    # Grab the points for the cluster from the extracted outliers (cloud_objects)
    pcl_cluster = cloud_objects.extract(pts_list)
    # TODO: convert the cluster from pcl to ROS using helper function

    #  Extract histogram features
    # TODO: complete this step just as is covered in capture_features.py 

    # Make the prediction, retrieve the label for the result
    # and add it to detected_objects_labels list
    prediction = clf.predict(scaler.transform(feature.reshape(1,-1)))
    label = encoder.inverse_transform(prediction)[0]
    detected_objects_labels.append(label)

    # Publish a label into RViz
    label_pos = list(white_cloud[pts_list[0]])
    label_pos[2] += .4
    object_markers_pub.publish(make_label(label,label_pos, index))

    # Add the detected object to the list of detected objects.
    do = DetectedObject()
    do.label = label
    do.cloud = ros_cluster
    detected_objects.append(do)

rospy.loginfo('Detected {} objects: {}'.format(len(detected_objects_labels), detected_objects_labels))

# Publish the list of detected objects
# This is the output you'll need to complete the upcoming project!
detected_objects_pub.publish(detected_objects)



if __name__ == '__main__':

    # TODO: ROS node initialization

    # TODO: Create Subscribers

    # TODO: Create Publishers

    # Initialize color_list
    get_color_list.color_list = []

    # TODO: Spin while node is not shutdown

    # Classify the clusters!
    detected_objects_labels = []
    detected_objects = []
te
    # Create Publishers
    # TODO: here you need to create two publishers
    # Call them object_markers_pub and detected_objects_pub
    # Have them publish to "/object_markers" and "/detected_objects" with
    # Message Types "Marker" and "DetectedObjectsArray" , respectively

    # Load Model From disk
    model = pickle.load(open('model.sav', 'rb'))
    clf = model['classifier']
    encoder = LabelEncoder()
    encoder.classes_ = model['classes']
    scaler = model['scaler']


