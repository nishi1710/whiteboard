from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load an official model
model = YOLO(r"C:\Users\Nishita Gopi\Documents\capstone\project1\runs\detect\train4\weights\best.pt")  # load a custom model

# Predict with the model
results = model(r"C:\Users\Nishita Gopi\Documents\capstone\project1\testing_w_s_tog.jpg")  # predict on an image