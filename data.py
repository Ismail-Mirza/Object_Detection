#!/usr/bin/env python
# coding: utf-8




# In[1]:


import cv2 #opencv
import os
import time
import uuid
import shutil


# In[2]:


IMAGES_PATH = "Tensorflow/workspace/images/collectedimages"


# In[3]:


# labels = ["hello","hey"]
# labels = ["what's up","my","name"]
# labels = ["nice","to meet you","please","thank you"]
# labels = ["excuse me","see you","later","goodbye","i love you","yes","no"]
# labels = ['no sign','no human']
# labels = [1,2,3,4,5]
#ka ,kha,g,gh
labels = ["g"]

number_imgs=15


# In[4]:


# address = "http://192.168.0.101:8080/video"
# cap.open(address)
for label in labels:
    label =  str(label)
    if os.path.exists("Tensorflow/workspace/images/collectedimages/"+label):
        shutil.rmtree("Tensorflow/workspace/images/collectedimages/"+label)
    os.mkdir("Tensorflow/workspace/images/collectedimages/"+label)
        
    
    cap = cv2.VideoCapture(0)
    print("Collecting Images for {}".format(label))
    time.sleep(3)
    for imgnum in range(number_imgs):
        
        ret,frame = cap.read()
        # frame = cv2.resize(frame,(852,480),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
        imagename = os.path.join(IMAGES_PATH,label,label+".{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow("frame",frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xff== ord("q"):
            break
    cap.release()
    


# In[ ]:




