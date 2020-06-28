# VTuber-MomoseHiyori
![Live2D](https://kennardwang.github.io/ImageSource/Project/Live2D.png)
### Where does the idea come from ?
+ Recently, I do some studies on Deep Learning and Computer Vision. At the same time, I realize that I can make a VTuber model by Unity which could simulate my facial expression via computer vision. After watching some tutorials I have made a fantastic Live2D model Momose Hhiyori, and becomes a VTuber successfully !
------
### VTuber Demo

<p align = "center">
      <img src = "https://kennardwang.github.io/ImageSource/Project/VTuberDemo.gif" width = "480px" height = "360px">
</p>

+ [Watch Video Demo](https://kennardwang.github.io/ImageSource/Project/VTuberDemo.mp4)
+ Test Behavior : **Nod**, **Shake**, **Rotate**, **Eyeball Rotate**, **Blink**, **Sleepy**, **Open Mouth**
      
------
### Development Environment
+ Test System : **Windows 10 64bits**
+ Camera : **Integrated Webcam**
+ Socket Transmission : **Intranet**
+ Model Made : **Live2D Cubism Editor 4.0**
+ Engine : **Unity 2019.2.6f1** 
+ Script Language : **C#**
+ Recognition Algorithm : **Deep Learning**
+ Language : **Python 3.7 Anaconda**
+ Main Required Library : **opencv**, **dlib**, **numpy**, **matplotlib**, **torch**
------
### File Explanation
| File | Explanation |
|:---:|:---:|
| ***Recognition*** | Packed Algorithm for facial recognition |
| ***UnityAssets*** | Tutorial materials for those want to make Live2D VTuber by self |
| ***Hiyori酱~*** | Starter, quick mode to start program |
------
### How to be a VTuber ?

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
------
### Tips
If you find it doesn't recognize well, please try again as following :
+ ***Use brighter light*** : To make your face more clearly, using both natural light and point light seems perfect.
+ ***Adjust your position*** : You can start a camera demo to help you know your position by adding `--debug` at `Hiyori酱~.bat`. Run again, let the outer green boundary be larger and central but not larger than demo boundary.
+ ***Do not wear glasses*** : Glasses probably influence on the accuracy of eye recognition.
------
### UnityAssets Tutorial ***( If you don't want to know how to make Live2D VTuber, you can skip this part )***
+ ***Description*** : It is a template for all the Live2D models. Live2D is easier to make and has higher graphic quality than 3D models, which means it probably has more extensive markets
+ ***Recommend Unity Engine*** : Unity 2019.2.6f +
+ ***Before you start*** : Equip yourselves with knowledge of Unity basic operation
+ ***Prepare Live2D SDK*** : You can download SDK on [website](https://www.live2d.com/en/download/cubism-sdk/download-unity/), or use `CubismSdkForUnity-4-r.1` I download for you under `UnityAssets`
+ ***Create a new Unity project***
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial1.png" width="80%"></p>

+ ***Import Live2D SDK*** : Drag `CubismSdkForUnity-4-r.1` to `Assets` and choose to import all
<p align="center">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial3.png" width="40%">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial4.png" width="40%">
</p>

+ ***Restart*** : Do not forget this step, otherwise the SDK probably cannot work !
+ ***Import Assets*** : Delete the default scene file, drag `Momose`, `Scece` and `Script` file under `Assets`
<p align="center">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial2.png" width="40%">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial5.png" width="40%">
</p>

+ ***Import Model*** : A **prefab** will be automatically generated at `Assets/Momose/hiyori_pro_t08.prefab`. Open `Scene/MomoseHiyori` and drag **prefab** into scene
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial6.png" width="80%"></p>

+ ***Set Position*** : Select **prefab** and move Y axis (blue) ahead
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial7.png" width="80%"></p>

+ ***Initialization*** : Move control balls to initialize
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial8.png" width="80%"></p>

+ ***Bind Script***
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial9.png" width="80%"></p>

+ ***Export & Build***
<p align="center"><img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial11.png" width="80%"></p>

<p align="center">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial10.png" width="40%">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial12.png" width="40%">
</p>

+ ***Start to Test***
<p align="center">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial13.png" width="40%">
      <img src="https://kennardwang.github.io/ImageSource/Project/UnityAssetsTutorial14.png" width="40%">
</p>

+ ***Recommendation for Model Website*** : https://www.live2d.com/en/download/sample-data/
+ ***Now, enjoy making your own Live2D VTuber !!***
------
### Optimization
+ Use Live2D instead of 3D model
+ Add 2 eye events : **sleepy** and **eyeball rotation**
+ Optimize some parameters and be more accurate
+ Easy start and fix window at top without boundary, more convenient for live streaming
------
### Credits
Thanks for following blogs or projects which give me a reference :

+ [Model Parameters Adjustment](https://docs.live2d.com/cubism-sdk-tutorials/about-parameterupdating-of-model/?locale=ja)
+ [Socket Connect](https://blog.csdn.net/u012234115/article/details/46481845)
+ [EXE Window Setting](https://blog.csdn.net/qq_39097425/article/details/81664448)
+ Algorithm

  > | Project | Author | LICENSE |
  > |:---:|:---:|:---:|
  > | [VTuber_Unity](https://github.com/kwea123/VTuber_Unity) | [AI葵](https://github.com/kwea123) | [LICENSE](https://github.com/kwea123/VTuber_Unity/blob/master/LICENSE) |
  > | [head-pose-estimation](https://github.com/yinguobing/head-pose-estimation) | [Yin Guobing](https://github.com/yinguobing) | [LICENSE](https://github.com/yinguobing/head-pose-estimation/blob/master/LICENSE) |
  > | [face-alignment](https://github.com/1adrianb/face-alignment) | [Adrian Bulat](https://github.com/1adrianb) | [LICENSE](https://github.com/1adrianb/face-alignment/blob/master/LICENSE) |
  > | [GazeTracking](https://github.com/antoinelame/GazeTracking) | [Antoine Lamé](https://github.com/antoinelame) | [LICENSE](https://github.com/antoinelame/GazeTracking/blob/master/LICENSE) |
+ [Model by Artist ***kani_biimu***](https://www.live2d.jp/en/terms/live2d-free-material-license-agreement/)
------
### License
+ [MIT License](https://github.com/KennardWang/VTuber-MomoseHiyori/blob/master/LICENSE)
------
### Author
+ Kennard Wang ( 2020.6.27 )
------
