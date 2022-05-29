# openCV study

# 환경 

## python version
python version = 3.7.7

## opencv version
pip install opencv-python==4.1.0.25

### face_detector_model (Single Shot MultiBox Detector(SSD)) download 
• Caffe(FP16): https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel

• TensorFlow(uint8): https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180220_uint8/opencv_face_detector_uint8.pb

위 두모델의 blobFromImage 파라미터 
scale_factor= 1, size = (300,300) , mean(104, 177, 123)

### face_detector_config_file download
• https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector
deploy.prototxt, opencv_face_detector.pbtxt -> file download
