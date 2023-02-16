# SignLanguageRecognition
Around 95 million people in the world are deaf and dumb, and it is difficult for people to understand and
communicate with them. Communication plays a significant role in human interaction and knowledge
sharing. In order to remove those barriers we are willing to create a sign language recognition and
sentence formation software.
Sign languages are of various types that include American sign language,Indian Sign language, Chinese
sign language,French sign language etc. Sign Language is basically divided into 2 categories
1. Static sign language
2. Dynamic sign language
METHODOLOGY:
Gesture recognition and sentence formation are 2 major aspects of the project, Gesture
recognition is done by capturing the image and extracting the hand (ROI) from the image, then the
gesture is predicted using the CNN model, and the predicted output is used to generate a sentence using RNN.
Filtering techniques, Object Detection techniques, CNN, and RNN are used for the training of the model.
Video Capture → Hand Recognition → Image segmentation→ Gesture Classification
(Classifier) → LSTM → Sequence Prediction → Sentence
DATASET:
Two datasets are used in this project both the datasets relate to american sign language,The first
data set is a kaggle American sign language dataset of images of 26 alphabets and 9 numbers.
The second data set is a custom built dataset used for training the model with words such as
Thankyou,Hello,etc
