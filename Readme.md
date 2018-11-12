
Please use the following to train your own Model Classifier  with Custom Vision in 1min  - NO NEED to Prelabel data:

## Action
1) Go To https://customvision.ai      
2) Export your Keys to some Temp Storage    
3) Open a new Tab with http://image-net.org/  and search for your favourite Tags eg. Bird

![](https://github.com/uneidel/ModelGenerator/raw/master/Images/imagenet.jpg)
rightClick on Bird and copy the Link > http://image-net.org/synset?wnid=n01503061   and store the Number of Pictures : 871
Repeat Step 3 and 4 for all required Tags        
4) Open the Attached Script and modify the the required Variables
So http://image-net.org/synset?wnid=n01503061 -> n01503061, Number of Pictures: 871 , TagName: Bird

```
training_key = "<COPY FROM STEP2>"
prediction_key = "<COPY FROM STEP2>"
prjName="<SomeFANCYPROJECTNAME>"
train=[
    {"StartIndex": 'n01503061',"ImageMax" : 871,"Tag" : "Bird"},
    {"StartIndex": 'n02512053',"ImageMax" : 617,"Tag" :  "Fish"}
]

````
Save the Script and run it with python generictrainer.py       
Either uncomment the predict Function or go to the portal to Evaluate        
This are a Setup for WorkerSafety Demo: (HardHat Detection)      
```
train=[
    {"StartIndex": 'n07942152',"ImageMax" : 1500,"Tag" : "NoHat"},
    {"StartIndex": 'n03492922',"ImageMax" : 500,"Tag" :  "ConstructionHelmet"}
]
````
