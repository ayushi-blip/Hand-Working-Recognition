# Hand-Working-Recognition

The concept of Gesture Recognition using various methods has widely been studied. This article aims to provide comprehensive research on the topic of Hand Recognition using Colour by employing the frameworks of OpenCV libraries.

It works with the concepts of image processing like background subtraction and thresholding which helps in segmenting the object that is used via our hand for gesture recognition. The main aim of this article is to provide the users with a way to operate their system in a more efficient and appealing manner. A hand gesture recognition system that requires the use of a coloured object and only a webcam can give way to many more such works making this more efficient with days to come.

Software and Hardware Required
Python 3 or above
OpenCV Libraries
PC or Laptop with an in-built webcam or external webcam
Implementation (with code)
The project broadly consists of three modules. The first module is the declaration of the grids onto the capturing scene. These grids allow for the demarcation of the boundary of the captured video, thus, helping us to register exactly where the pointer had moved. The second module is the most important module of the project, as this where background subtraction for the pointer takes place and the pointer is brought to the focus. The third and final module is where the code registers the pattern in which the grids were visited and accordingly does the required task.

MODULE 1
OpenCV is one of the most prominently used software libraries focusing on computer vision and machine learning projects. It has inbuilt libraries and algorithms which provide for the implementation of certain computer vision problems. OpenCV also provides the algorithm for creating shapes and such onto the video-captured screen. In our project, we used to same in order to create nine grids onto the screen that captured the live video. Before we can use the package for the shape creation, we need to define the boundaries of the grid. We define the point coordinates of each of the four sides of the quadrilateral, on an estimation basis and then define all the remaining grids with respect to the positioning of the first one.

Using the cv2 package or the binding generators, we can call various functions of OpenCV. We use the cv2.rectangle function to create the grids according to the boundaries provided by us. We give it a descriptive colour (red, in our case) and specify the length of the same.

Once created, we display all the rectangles (grids) onto the live-video capturing screen and use it to create patterns for the tasks to be executed.
