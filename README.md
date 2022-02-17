# VTuber-MomoseHiyori

> Recently, Kennard did some work on Deep Learning and Computer Vision. At the same time, he realized that 
> he could make a Live2D VTuber model by Cubism and Unity which could simulate his facial expression. 
> After watching some tutorials, Kennard successfully made his first Live2D model Momose Hiyori!

------

### VTuber Demo

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/VTuberDemo.gif" width = "480px" height = "360px"/>
</p>

<br>
<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack1.gif" width = "400px" height = "210px"/>
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack2.gif" width = "400px" height = "210px"/>
</p>

<p align = "center">
    Face Behavior Test : Head shaking, Nodding, Head rotation, Eye blinking, Eye half-opening, Eyeball rotation, Mouth opening.
</p>

------

### Development Environment

|Description|Specification|
|:---:|:---:|
|System|Windows 10|
|Camera|Integrated Webcam|
|Algorithm Language|Python 3.7 (Anaconda)|
|IDE|PyCharm 2019.2.5|
|Related Libraries|**opencv**, **dlib**, **numpy**, **pytorch**|
|Model Tool|Live2D Cubism Editor 4.0|
|Unity Engine|Unity 2019.4.1f1 LTS| 
|Script Language|C#|

------

### File Specification

+ ***Recognition*** : Packed algorithm for face recognition.
+ ***UnityAssets*** : Unity materials for those who want to make Live2D VTuber by themselves.
+ ***Hiyori酱~*** : A quick start program.

------

### Usage

> 1. Download and unzip ZIP source file
> 2. Install required python libraries ( ***recommend Anaconda*** )  
>  + I do not test at other operating system, if your OS is not Windows, you'd better test it by yourself
>  + Windows
>     + There are some libraries that I use, you can use `pip install -r requirements.txt` to install as you like
>     + CPU ( ***recommend for testing*** )
>        +  Libraries Installation by `pip install -r requirements_cpu.txt`
>        +  Open ***Anaconda Prompt*** to install `dlib` by `conda install -c menpo dlib` if it doesn't work
>     + GPU
>        + Firstly, please check the your CUDA version : ***9.0 / 10.1 / 10.2 / None***
>        + Install [pytorch](https://pytorch.org/) by running corresponding command such as `conda install pytorch torchvision cudatoolkit=10.2 -c pytorch` for 10.2
>        + Install other libraries by `pip install -r requirements_gpu.txt`.
>        + If you have CUDA 10, `pip install onnxruntime-gpu` to get faster inference speed using onnx model.
> 
> 3. Download `VTuber_Hiyori.zip` and `ckpts.zip` ( If you want to use `onnxruntime` to get faster speed ) at [Release](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v1.2.0)
> 4. Unzip `ckpts` and put it under `Recognition\face_alignment` 
> 5. Unzip `VTuber_Hiyori` and start `VTuber_MomoseHiyori.exe` ( Please ***wait*** and do not start any other applications simultaneously !!! )
> 6. Run `Hiyori酱~.bat`
> 7. If **ひよりちゃん** start to simulate your facial expression, congratulations! You have been a VTuber now!
> 8. The [latest verion](https://github.com/KennardWang/VTuber-MomoseHiyori/releases) has been released, you can download and use them.

------

### Tips
The following tips may help to improve the effect:

+ ***Use brighter light*** : To make your face more clearly, using both natural light and point light seems perfect.
+ ***Adjust your position*** : You can start a camera demo to help you know your position by adding `--debug` at `Hiyori酱~.bat`. Run again, let the outer green boundary be larger and central but not larger than demo boundary.
+ ***Do not wear glasses*** : Glasses probably influence on the accuracy of eye recognition.
+ ***Show your forehead*** : Probably your hair is too long to have side effects on recognition of your eyes.

------

### Optimization
+ Use Live2D instead of 3D model.
+ Add two eye-events : **Eye Half-opening** and **Eyeball Rotation**.
+ Optimize some parameters to improve accuracy.
+ Fixed window at top without boundary, which is more convenient for live streaming.
+ Implement quick start program.

------

### References

+ [Model Parameters](https://docs.live2d.com/cubism-sdk-tutorials/about-parameterupdating-of-model/?locale=ja)
+ [TCP Socket](https://blog.csdn.net/u012234115/article/details/46481845)
+ [Window Settings](https://blog.csdn.net/qq_39097425/article/details/81664448)
+ [Live2D Model by Artist ***kani_biimu***](https://www.live2d.jp/en/terms/live2d-free-material-license-agreement/)
+ Algorithms

  > | Project | Author |
  > |:---:|:---:|
  > | [head-pose-estimation](https://github.com/yinguobing/head-pose-estimation) | [Yin Guobing](https://github.com/yinguobing) |
  > | [face-alignment](https://github.com/1adrianb/face-alignment) | [Adrian Bulat](https://github.com/1adrianb) |
  > | [GazeTracking](https://github.com/antoinelame/GazeTracking) | [Antoine Lamé](https://github.com/antoinelame) |
  > | [VTuber_Unity](https://github.com/kwea123/VTuber_Unity) | [AI葵](https://github.com/kwea123) |

------

### License
+ [MIT License](https://github.com/KennardWang/VTuber-MomoseHiyori/blob/master/LICENSE)

------

### Author
+ Kennard Wang ( 2020.6.27 )
