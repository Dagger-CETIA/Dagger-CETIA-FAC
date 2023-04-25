import jetson.inference
import jetson.utils

# load the object detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(1280, 720, "/dev/video1")
display = jetson.utils.glDisplay()
#camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2

while display.IsOpen():
	img, width, height  = camera.CaptureRGBA()
	detections = net.Detect(img, width, height)
	display.Render(img, width, height)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
