# anomaly-detection
a repo to detect anomalies via unsupervised method

File: anomaly.py
------------------------
Description: 
Detect anomalies via unsupervised method

How to run:
- d / --dataset : path to calibration dataset (create dataset by taking pictures of calibration board using camera)
- i / --image    : image to remove distortion
- t / --type     : Type of board, 0 = chessboard | 1 = aruco | 2 = charuco 
```
$ python calibrate.py -d path/dataset -i imageToUndistort.jpg -t 0
```


To Do:
------------------------
  - [ ] combine aruco, charuco and chessboard all in one file
  - [ ] Convert code to C++
  - [ ] remove need for svgfig dependency in create_chessboard.py
