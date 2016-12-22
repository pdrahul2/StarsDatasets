# StarsDatasets

## What is this project ?
During the implementation of object detection frameworks, often experiments with multiple datasets are required. This involves
accessing bounding box groundtruth annotations of different object categories in different datasets. This is a simple-looking 
task that is made a little challenging by varying formats in which different datasets organize their groundtruth annotations.

This project provides a framework to quickly read bounding box annotations of different datasets without having to worry about 
the actual details of native storage formats. This project has been initialized with a codebase using which a number of 
major pedestrian detection datasets can be easily read. It will be regularly updated to include other pedestrian and 
non-pedestrian datasets as well.

## Pre-requisites
### For users
For a user there are just two pre-requisites :
1.  Make sure that a class corresponding to the dataset exists in the project.
2.  Make sure that you have downloaded and stored the dataset inside a specific parent folder (we call it *base_path*)

*NOTE:* If [1.](https://github.com/ujjwal-researcher/StarsDatasets/README.md#L16) is not true, please look down at 
[pre-requisites for developers](https://github.com/ujjwal-researcher/StarsDatasets/README.md#L21).
### For developers
