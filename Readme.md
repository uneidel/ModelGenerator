
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
[GenericTrainer.py]
(https://microsoft.sharepoint.com/teams/PDSIoTKnowledgearea/Shared Documents/SME - Advanced Analytics/GenericTrainer.py)
<https://teams.microsoft.com/l/message/19:c24afd39107c4c2681c4bca7f7149dbb@thread.skype/1539240141972?tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47&amp;groupId=8b3b19d9-31f6-4153-a3c2-3e4dee7e922f&amp;parentMessageId=1539240141972&amp;teamName=PDS IoT Knowledge Central&amp;channelName=SME - Advanced Analytics&amp;createdTime=1539240141972>