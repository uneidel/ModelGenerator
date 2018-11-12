#!/usr/bin/env python3

# pip install six numpy 
# pip install azure-cognitiveservices-vision-customvision

from six.moves import urllib
#import urllib
import urllib.request
import numpy as np
import os
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

import time



def train(trainer,project):
    print ("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status != "Completed"):
        iteration = trainer.get_iteration(project.id, iteration.id)
        print ("Training status: " + iteration.status)
        time.sleep(1)

    # The iteration is now trained. Make it the default project endpoint
    trainer.update_iteration(project.id, iteration.id, is_default=True)
    print ("Done!")

def predict(prediction_key,test_img_url):
    # Now there is a trained endpoint that can be used to make a prediction
    predictor = prediction_endpoint.PredictionEndpoint(prediction_key)   
    results = predictor.predict_image_url(project.id, iteration.id, url=test_img_url)
    for prediction in results.predictions:
        print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))

def LoadAndStore(project, tagInfo):
    cvTag = trainer.create_tag(project.id, tagInfo["Tag"])
    baseurl="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + tagInfo["StartIndex"]
    store_raw_images(tagInfo["Url"], tagInfo["ImageMax"], project, cvTag)

def store_raw_images(link, maxcount,project, tag):
    image_urls = urllib.request.urlopen(link).read().decode()
    pic_num = 1

    while(pic_num < maxcount):
        for i in image_urls.split('\n'):
            try:
                print("url: %s" %(i))
                request = urllib.request.urlopen(i, timeout=10)
                trainer.create_images_from_urls(project.id, [ ImageUrlCreateEntry(url=i, tag_ids=[ tag.id ] ) ])
                pic_num += 1
            except Exception as e:
                print(str(e))

#################################### MAIN FUNCTION ###################################################################

# Replace with a valid key
training_key = "e0a55341a4ee40b79acdba9c40a7d13a"
prediction_key = "7bcd17626bc94087b566b73e751475fc"
prjName="birdorfish"
train=[
    {"StartIndex": 'n01503061',"ImageMax" : 871,"Tag" : "Bird"},
    {"StartIndex": 'n02512053',"ImageMax" : 617,"Tag" :  "Fish"}
]

# Create a new project
trainer = training_api.TrainingApi(training_key)
print ("Creating project %s..." % (prjName))
project = trainer.create_project(prjName)
for tag in train:
    LoadAndStore(project, tag)

train(trainer, project)
#predict(prediction_key, "http://somefancylinktoimage")
