# VTuber-MomoseHiyori

<div align="center">
  <img src="https://img.shields.io/github/stars/KennardWang/VTuber-MomoseHiyori" />
  <img src="https://img.shields.io/github/forks/KennardWang/VTuber-MomoseHiyori" />
  <img src="https://img.shields.io/github/license/KennardWang/VTuber-MomoseHiyori" />
  <img src="https://img.shields.io/badge/maintenance-No-red" />
</div>

<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/VTuberDemo.gif" width = "480px" height = "360px"/>
</p>

<br>

Hello,👋 I am Momose Hiyori, a Live2D VTuber from Japan. I am really good at mimicking people's facial expressions and actions, my makeup is designed by Cubism and Unity, while my ability to mimic is based on OpenCV and deep learning. It is a pleasure to meet you all and I look forward to being good friends!❤

<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack1.gif" width = "400px" height = "210px"/>
    &nbsp;
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack2.gif" width = "400px" height = "210px"/>
</p>

<p align = "center">
    I can mimic: shaking head, nodding, head rotation, blinking eyes, half-opening eyes, eyeballs rotation, opening mouth.
</p>



## Table of Contents

- [Development Environment](#development-environment)
- [Install](#install)
- [Usage](#usage)
- [Highlights](#highlights)
- [File Description](#file-description)
- [References](#references)
- [Releases](#releases)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)



## Development Environment

|      <!-- -->      |             <!-- -->              |
| :----------------: | :-------------------------------: |
|       System       |            Windows 10 x64         |
|      Language      |       Python 3.7 Anaconda (algorithm) / C# (Live2D model)     |
|        IDE         |         PyCharm 2019.2.5 (algorithm) / Live2D Cubism Editor 4.0 (Live2D model) / Unity 2019.4.1f1 LTS (Live2D model)   |



## Install

1. Install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) and Python 3.7 (recommend [Anaconda](https://www.anaconda.com/products/individual)).
2. Download [ckpts](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/dependency) model, unzip and place it as `Recognition\face_alignment\ckpts`.
3. Download [VTuber_MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0) application folder.
4. There are 2 types of running environments, please choose the correct one based on individual conditions.
   + CPU env
       + Install **dlib v19.22.0**
     
         ```
         conda install -c conda-forge dlib
         ```
         
    + GPU env
        + Install [CUDA v10.2 & CUDNN v8.3.1](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/environment).
        + Install [Pytorch](https://pytorch.org/).

          ```
          pip3 install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
          ```

5. Install related dependencies.

   ```
   git clone https://github.com/KennardWang/VTuber-MomoseHiyori.git
   cd Recognition
   pip install -r requirements.txt
   ```



## Usage

**Step 1 : Test camera**

If it runs normally, you can see your face, and press `q` to quit.

+ CPU env
  
  ```
  python main.py --debug --cpu
  ```
  
+ GPU env
  
  ```
  python main.py --debug
  ```

<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/cpu.gif" width = "400px" height = "230px"/>
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/gpu.gif" width = "400px" height = "230px"/>
</p>

<p align = "center">
    CPU env (left) has higher FPS but lower accuracy, and it cannot recognize well if some parts of the face are covered.
</p>
<p align = "center">
    GPU env (right) has higher accuracy, better fluency and consecutiveness but lower FPS by virtue of busier data IO.
</p>

<br>

**Step 2 : Connect Unity**

1. Click `VTuber_MomoseHiyori.exe` to run.
2. Execute the command according to your env.
   + CPU env
     
     ```
     python main.py --debug --cpu --connect
     ```
     
   + GPU env
  
     ```
     python main.py --debug --connect
     ```


**Tips to improve the effect**

+ Use spotlight: Try to make your face look brighter, the spotlight probably shows a better effect than the natural light.
+ Adjust the face position: The debug mode of the camera may help you to know the position of your face. Try to make the green frame larger and central but not over the boundary.
+ Do not wear glasses: Wearing glasses may influence the accuracy of eye recognition.
+ Show your forehead: If your hair is so long that covers your eyes, it will have side effects on the accuracy of eye recognition.



## Highlights
- [x] Develop a Live2D model.
- [x] Add two eye events: half-opening eyes and eyeballs rotation.
- [x] Optimize some parameters to improve accuracy.
- [x] Design a multi-functional display window that is more convenient and feasible for live streaming.



## File Description

+ **Recognition**: Packed algorithm for face recognition.
+ **UnityAssets**: Unity materials for those who want to make Live2D VTuber by themselves. Here is the [tutorial](https://github.com/KennardWang/VTuber-MomoseHiyori/issues/3).



## References

+ [Live2D model](https://www.live2d.jp/en/terms/live2d-free-material-license-agreement/) by kani_biimu.
+ [How to update Live2D model parameters](https://docs.live2d.com/cubism-sdk-tutorials/about-parameterupdating-of-model/?locale=ja).
+ [Write a TCP socket script](https://blog.csdn.net/u012234115/article/details/46481845).
+ [How to make a display window](https://blog.csdn.net/qq_39097425/article/details/81664448).
+ [VTuber Unity project](https://github.com/kwea123/VTuber_Unity) by AI葵.
+ [Headpose estimation](https://github.com/yinguobing/head-pose-estimation) by Yin Guobing.
+ [Face alignment](https://github.com/1adrianb/face-alignment) by Adrian Bulat.
+ [GazeTracking](https://github.com/antoinelame/GazeTracking) by Antoine Lamé.



## Releases

[The latest version](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0).



## Maintainers

[@KennardWang](https://github.com/KennardWang).



## Contributing

Feel free to [open an issue](https://github.com/KennardWang/VTuber-MomoseHiyori/issues) or submit [PRs](https://github.com/KennardWang/VTuber-MomoseHiyori/pulls).



## License

[MIT](LICENSE) © Kennard Wang. ( 2020.6.27 )
