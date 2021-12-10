# Modeling Overview

This modeling directory contains all of the code utilized throughout the modeling portion of this project. Within this directory there are four primary sub-directories each of which have their own unique file structure which will be explained below.

## Cross-Validation

Throughout the modeling process, we conducted a variety of cross-validation and hyper-parameter search efforts for each modeling approach within each individual region. All the code relevant to these efforts is contained within this directory. Since the modeling effort was conducted across a regional basis, within this main directory exists several subdirectories for each region. These subdirectories contain all code relevant to that specific region. Then, within these regional directories there are further subdirectories for each of the five modeling approaches applied to each region AdaBoost, Logistic Regression, Naive Bayes, Neural Networks, and Random Forests. Within each of these model subdirectories are again further subdirectories which contain the trained models’ relevant results, charts, and saved models. Each of the regional subdirectories has the same mirrored structure. The overall directory structure is as follows:


**.**\
│── **...**\
│──  **Cross-Validation**\
│    │\
│    │──  **Florida_CV**\
│    │    │\
│    │    │──  **AdaBoost:** *Contains all files relevent to the cross-validation of AdaBoost models*\
│    │    │    │\
│    │    │    │── **Charts:** *Contains all of the output modeling charts as png files*\
│    │    │    │\
│    │    │    │── **Model_Histories:** *Contains all of the output modeling cross-validation statisitics as csv files*\
│    │    │    │\
│    │    │    └── **Trained_Models:** *Contains the pickled/saved models*\
│    │    │\
│    │    │──  **Logisitic Regression:** *Contains all files relevent to the cross-validation of logistic regression models*\
│    │    │    └── **...**\
│    │    │\
│    │    │──  **Naive Bayes:** *Contains all files relevent to the cross-validation of naive Bayes models*\
│    │    │    └── **...**\
│    │    │\
│    │    │──  **Neural Networks:** *Contains all files relevent to the cross-validation of neural network models*\
│    │    │    └── **...**\
│    │    │\
│    │    │──  **Random_Forest:** *Contains all files relevent to the cross-validation of random forest models*\
│    │    │    └── **...**\
│    │    │\
│    │    └── **Modeling_Flordia_CV:** *Jupyter Notebook that implements and trains the models*\
│    │\
│    │──  **NorthCentral_CV**\
│    │    └── **...**\
│    │──  **NorthEast_CV**\
│    │    └── **...**\
│    │──  **NorthWest_CV**\
│    │    └── **...**\
│    │──  **SouthCentral_CV**\
│    │    └── **...**\
│    │──  **SouthEast_CV**\
│    │    └── **...**\
│    │──  **UpperMidwest_CV**\
│    │    └── **...**\
│    └── **West_CV**\
│        └── **...**\
└── **...**\

## Geographic Region Segmentation

Throughout the modeling process, it quickly became clear that it would be more effective both computational and form a perspective of superior results for us to segment the United States into different geographic regions, which would be modeling independently. Contained within this folder are a png and svg version of the map we utilized and prepared through the regional data segmentation process.

## Modeling Utilities

This directory contains any scripts or notebooks used within the modeling process that served as general utility functions. The primary use of these utilities was the consolidation and merging of the output modeling predictions across all regions into a single file for later use by our MySQL database.

## Production

Throughout the modeling process, there were two primary steps to our workflow. First, we tested a variety of models at the regional level and conducted cross-validation and hyper-parameter search. All of these files as mentioned above are included in the "Cross_Validation" directory. The second workflow after the cross-validation was complete, was utilizing these results and optimal hyper-parameters to train a final "production" model that would be used directly within our application. These models would also be trained on a larger percentage of the training set. Since throughout the cross-validation process it became clear that among all regions, the best models were Random Forests and Neural Networks, these would be the only types of models trained within the "production" environment. The production folder contains a subdirectory for each modeling region. Within these subdirectories lies all of the individual and unique regional models, code, and results. Each of the regional subdirectories has the same mirrored structure. The overall directory structure is as follows:


**.**\
│── **...**\
│──  **Production**\
│    │\
│    │──  **Florida_Production**\
│    │    │\
│    │    │──  **Neural_Network:** *Contains all files relevent to the production neural network model*\
│    │    │    │\
│    │    │    │── **Charts:** *Contains all of the output modeling charts as png files*\
│    │    │    │\
│    │    │    └── **Florida_Trained_NN_Production:** *Contains the pickled/saved trained tensorflow neural network model assets*\
│    │    │\
│    │    │──  **Random_Forest:** *Contains all files relevent to the production random forest model*\
│    │    │    │\
│    │    │    │── **Charts:** *Contains all of the output modeling charts as png files*\
│    │    │    │\
│    │    │    └── **Florida_Trained_NN_Production:** *Contains the pickled/saved trained sklearn random forest model assets*\
│    │    │\
│    │    └── **Modeling_Flordia_Production:** *Jupyter Notebook that implements and trains the models*\
│    │\
│    │──  **NorthCentral_Production**\
│    │    └── **...**\
│    │──  **NorthEast_Production**\
│    │    └── **...**\
│    │──  **NorthWest_Production**\
│    │    └── **...**\
│    │──  **SouthCentral_Production**\
│    │    └── **...**\
│    │──  **SouthEast_Production**\
│    │    └── **...**\
│    │──  **UpperMidwest_Production**\
│    │    └── **...**\
│    └── **West_Production**\
│        └── **...**\
└── **...**\
