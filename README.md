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

|    Description     |           Specification           |
| :----------------: | :-------------------------------: |
|       System       |            Windows 10             |
|       Camera       |         Integrated Webcam         |
| Algorithm Language |       Python 3.7 (Anaconda)       |
|        IDE         |         PyCharm 2019.2.5          |
| Related Libraries  | **opencv**, **dlib**, **pytorch** |
|     Model Tool     |     Live2D Cubism Editor 4.0      |
|    Unity Engine    |       Unity 2019.4.1f1 LTS        |
|  Script Language   |                C#                 |

------

### Folder Specification

+ ***Recognition*** : Packed algorithm for face recognition.
+ ***UnityAssets*** : Unity materials for those who want to make Live2D VTuber by themselves. Here is the [tutorial](https://github.com/KennardWang/VTuber-MomoseHiyori/issues/3).

------

### Usage

**Step 0 : Reparation**

1. Prepare Python IDE (recommend [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)) and install Python 3.7 (recommend [Anaconda](https://www.anaconda.com/products/individual)).
2. Download [ckpts](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/dependency) model, unzip and place it as `Recognition\face_alignment\ckpts`.
3. Download [VTuber_MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0) application folder.
4. Clone the repository by `git clone https://github.com/KennardWang/VTuber-MomoseHiyori.git`.
5. Enter the root by `cd Recognition`.

<br>

**Step 1 : Test Camera**

There are 2 types of running environments, please choose the correct one based on individual conditions. At the beginning, please install related dependencies by `pip install -r requirements.txt`.

+ CPU env
  1. Install `dlib v19.22.0` by `conda install -c conda-forge dlib`.
  2. Finally, run `python main.py --debug --cpu` to test.
  3. If it runs normally, you can see your face, and press `q` to end up.

+ GPU env
  1. Download and install [CUDA v10.2 & CUDNN v8.3.1](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/environment).
  2. Install [pytorch](https://pytorch.org/) by `pip3 install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html`.
  3. Finally, run `python main.py --debug` to test.
  4. If it runs normally, you can see your face, and press `q` to end up.

<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/cpu.gif" width = "400px" height = "230px"/>
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/gpu.gif" width = "400px" height = "230px"/>
</p>

<p align = "center">
    CPU env (left) has the higher FPS but the lower accuracy. (It cannot recognize well if some parts of the face are covered.)
</p>
<p align = "center">
    GPU env (right) has the higher accuracy, the better fluency and consecutiveness but the lower FPS by virtue of the busier data IO.
</p>

<br>

**Step 2 : Connect Unity**

1. Click `VTuber_MomoseHiyori.exe` to run.
2. In CPU env, run `python main.py --debug --cpu --connect`.
3. In GPU env, run `python main.py --debug --connect`.

------

### Tips
The following tips may help to improve the effect:

+ ***Use spotlight*** : Try to make your face look brighter, the spotlight probably shows better effect than the natural light.
+ ***Adjust the face position*** : The debug mode of the camera may help you to know the position of your face. Try to make the green frame larger and central but not over the boundary.
+ ***Do not wear glasses*** : Wearing glasses may influence the accuracy of eye recognition.
+ ***Show your forehead*** : If your hair is so long that covers your eyes, it will have side effects on the accuracy of eye recognition.

------

### Optimization
+ Use the Live2D model.
+ Add two eye events : **Eye Half-opening** and **Eyeball Rotation**.
+ Optimize some parameters to improve accuracy.
+ The multi-functional of window display is more convenient and feasible for live streaming.

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
