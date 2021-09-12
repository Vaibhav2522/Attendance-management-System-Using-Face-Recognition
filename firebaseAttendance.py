from csv import DictReader
import glob
import json
import pandas as pd
import os

def firebaseAttendancePost():   
    from firebase import firebase 
    firebase = firebase.FirebaseApplication("https://attendance-management-sy-59713-default-rtdb.firebaseio.com/",None);

    path="C:\\Users\\DELL\\Desktop\\Attendance-Management-system-using-face-recognition\\Attendance\\"
    for root, dirs, files in os.walk(f"C:\\Users\\DELL\\Desktop\\Attendance-Management-system-using-face-recognition\\Attendance"):
        for file in files:
            if(file=="attendance.csv"):
                temp=root
                sub=temp.replace(path,"")
                #csv file read.
                df = pd.read_csv(root+"\\"+file, delimiter=',')
                print(sub)
                #firebase m se delete karna h
                firebase.delete("/attendance/",sub)
                for data in json.loads(df.to_json(orient="records")):
                    print(data)
                    print("-----")
                    firebase.post("/attendance/"+sub, data)