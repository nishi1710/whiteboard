from ultralytics import YOLO

#load model 
model = YOLO("yolov8n.yaml") # yolov8 nano
model = YOLO("yolov8n.pt")
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

#use the model
results = model.train(data="data.yaml", epochs=5 ,imgsz = 640) #train the model
results = model.predict(source=r"C:\Users\Nishita Gopi\Documents\capstone\project1\images\val", save=True)
