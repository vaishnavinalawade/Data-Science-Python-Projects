#Create environment
conda create -n py36 python=3.6
conda config --add channels conda-forge
conda install numpy
conda install scipy
conda install dlib

pip install --no-dependencies face_recognition

#import libraries
import os
import face_recognition

#make list of all the available images
images = os.listdir('images')
#load your image
image_to_be_matched = face_recognition.load_image_file('my_image.jpg')
#encode the loaded into feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
#iterate over each image
for image in images:
    #load the image
    current_image = face_recognition.load_image.file("images/"+image)
    #encode the loaded image into feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    #match your image with the image and check if it matches
    result = face_recognition.compare_face([image_to_be_matched_encoded], current_image_encoded)
    #check if it matches
    if result[0] == True:
        print("Matched " + image)
    else:
        print("Not Matched " + image)
