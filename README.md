# VTuber-MomoseHiyori
![Live2D](https://kennardwang.github.io/ImageSource/Project/Live2D.png)
### Where does the idea come from ?
+ Recently, I do some studies on Deep Learning and Computer Vision. At the same time, I realize that I can make a VTuber model which could simulate my facial expression via computer vision. After watching some tutorials I have made a fantastic Live2D model Momose Hhiyori, and becomes a VTuber successfully !
------
### VTuber Demo

<p align = "center">
      <img src = "https://kennardwang.github.io/ImageSource/Project/VTuberDemo.gif" width = "480px" height = "360px">
</p>

+ [Video Demo](https://kennardwang.github.io/ImageSource/Project/VTuberDemo.mp4)

------
### Development Environment
+ Test System : **Windows 10 64bits**
+ Model Made : **Live2D Cubism Editor 4.0**
+ Engine : **Unity 2019.2.6f1** 
+ Script Language : **C#**
+ Recognition Algorithm : **Deep Learning**
+ Language : **Python 3.7 Anaconda**
+ Main Required Library : **opencv**,**dlib**,**numpy**,**matplotlib**,**torch**
+ Socket Transmission : **Intranet**
------
### File Explanation
| File | Explanation |
|:---:|:---:|
| ***Recognition*** | Packed Algorithm for facial recognition |
| ***Unity Assets*** | Tutorial materials for those want to make Live2D VTuber by self |
| ***Hiyori酱~*** | Starter, quick mode to start program |
------
### How to be a VTuber ?

> 1. Download and unzip ZIP source file to the Desktop
> 2. Install required python libraries ( ***recommend Anaconda*** )  
>  + I do not test at other operating system, if your OS is not Windows, you'd better test it by yourself
>  + Windows
>     + There are some libraries that I use, you can use `pip install -r requirements.txt` to install as you like
>     + CPU ( ***recommend for testing*** )
>        +  Libraries Installation by `pip install -r requirements_cpu.txt`
>        +  Open **Anaconda Prompt** to install `dlib` by `conda install -c menpo dlib` if it doesn't work
>     + GPU
>        + Firstly, please check the your CUDA version : **9.0 / 10.1 / 10.2 / None**
>        + Install [pytorch](https://pytorch.org/) by running corresponding command such as `conda install pytorch torchvision cudatoolkit=10.2 -c pytorch` for 10.2
>        + Install other libraries by `pip install -r requirements_gpu.txt`.
>        + If you have CUDA 10, `pip install onnxruntime-gpu` to get faster inference speed using onnx model.
> 
> 3. Download **VTuber_Hiyori** and **ckpts** ( If you want to use `onnxruntime` to get faster speed ) by clicking [here](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v1.2.0)
> 4. Unzip **ckpts** and put it under `Recognition\face_alignment` 
> 5. Unzip **VTuber_Hiyori** to the Desktop and start `VTuber_MomoseHiyori.exe` ( Please do not start any other applications simultaneously !!! )
> 6. Run **Hiyori酱~.bat**
> 7. If **ひよりちゃん** start to simulate your facial expression, congratulations! You have been a VTuber now!
------
### Unity Asset Tutorial
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
