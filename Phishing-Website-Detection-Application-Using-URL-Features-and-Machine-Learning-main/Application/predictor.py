import feature_extraction as fe
import database as db
import pickle

import os
cwd= os.getcwd()
# model_filename = os.path.join(cwd,"Application\RandomForestClassifier.sav") 

model_filename = r"C:\Users\Manoj\Downloads\Phishing-Website-Detection-Application-Using-URL-Features-and-Machine-Learning-main\Phishing-Website-Detection-Application-Using-URL-Features-and-Machine-Learning-main\Application\RandomForestClassifier.sav"
# Load model to predict new data
with open(model_filename, 'rb') as f:
    rfc = pickle.load(f)

# Classify URL input
def classifyURL(url):
    if db.search_URL(url):
        return "Phishy"
    else:
        df = fe.featureExtraction(url)
        # print(int(rfc.predict([df])))
        # return rfc.predict([df])


        res = int(rfc.predict([df]))
        if res:
            db.addURL_MongoDB(url)
            return "Phishy" 
        return "Legitimate"    
        
# df = fe.featureExtraction(url)
# print(classifyURL("https://btinternetxxx.github.io/btinternetxx/load.html"))

