def sendData(subject, date, attendanceArr):
    from firebase import firebase
    import json
    import datetime 
    
    
    
    
    firebase = firebase.FirebaseApplication("https://attendance-management-sy-59713-default-rtdb.firebaseio.com/",None);

    
    for item in attendanceArr:
        data={"Enrollment":None, "Name":None , "Date":None}
        data['Enrollment']=item['Enrollment']
        data['Name']=item['Name'][0]        
        now =datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        data["Date"]=now
        # sendData ={
        #     now:data
        # }
        # print(sendData)
        result=firebase.post("/attendance-management-sy-59713-default-rtdb/"+subject, data);
        print(result)
