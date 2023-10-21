# VTuber-MomoseHiyori

<div align="center">
  
  [![description](https://img.shields.io/badge/project-Individual-1F1F1F?style=for-the-badge)](https://github.com/KennardWang/VTuber-MomoseHiyori)
  &nbsp;
  [![stars](https://img.shields.io/github/stars/KennardWang/VTuber-MomoseHiyori?style=for-the-badge&color=FDEE21)](https://github.com/KennardWang/VTuber-MomoseHiyori/stargazers)
  &nbsp;
  [![forks](https://img.shields.io/github/forks/KennardWang/VTuber-MomoseHiyori?style=for-the-badge&color=white)](https://github.com/KennardWang/VTuber-MomoseHiyori/forks)
  &nbsp;
  [![contributors](https://img.shields.io/github/contributors/KennardWang/VTuber-MomoseHiyori?style=for-the-badge&color=8BC0D0)](https://github.com/KennardWang/VTuber-MomoseHiyori/graphs/contributors)
  
  <img src="https://img.shields.io/badge/windows-0078D6?logo=windows&logoColor=white&style=for-the-badge" />
  &nbsp;
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  &nbsp;
  <img src="https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/Unity-100000?style=for-the-badge&logo=unity&logoColor=white" />
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
|        IDE         |     PyCharm 2019.2.5 (algorithm) / Live2D Cubism Editor 4.0 (Live2D model) / Unity 2019.4.1f1 LTS (Live2D model)   |



## Install

1. Install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) and Python 3.7 (recommend [Anaconda](https://www.anaconda.com/products/individual)).
2. Download models in [ckpts](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/dependency), unzip and place it at `face_alignment/ckpts`.
3. Download folder [VTuber_MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0) which contains the executable file.
4. Environment configuration.

    ```
    git clone https://github.com/KennardWang/VTuber-MomoseHiyori.git
    cd VTuber-MomoseHiyori
    conda env create -f environment.yml
    ```
   
5. Activate environment and install dependencies.

    ```
    conda activate live2d_vtb
    pip install -r requirements.txt
    ```
   
6. There are 2 types of running environments, please choose the correct one based on individual conditions.
   + CPU env
       + Install **dlib**, my version is v19.22.0.
     
         ```
         conda install -c conda-forge dlib
         ```
         
    + GPU env
        + Install **scipy** with version > 0.16.

          ```
          pip install scipy>0.16
          ```
          
        + Install [CUDA v10.2 & CUDNN v8.3.1](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/environment).
        + Install [Pytorch](https://pytorch.org/).

          ```
          pip install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
          ```



## Usage

**Step 1 : Test camera**

If it runs normally, you can see your face, and press `q` to quit.

+ CPU env
  
  ```
  python main.py --debug
  ```
  
+ GPU env
  
  ```
  python main.py --debug --gpu
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

1. For Windows OS, click `VTuber_MomoseHiyori.exe` to run.
2. Execute the command according to your env.
   + CPU env
     
     ```
     python main.py --debug --connect
     ```
     
   + GPU env
  
     ```
     python main.py --debug --gpu --connect
     ```


**Tips to improve the effect**

+ Use spotlight: Try to make your face look brighter, the spotlight probably shows a better effect than the natural light.
+ Adjust face position: The debug mode of the camera may help you to know the position of your face. Try to put your face in a central position, and let the frame extend but not reach the boundary.
+ No glasses: Wearing glasses may influence the accuracy of recognition on eyes.
+ Show forehead: If your hair is so long that covers your eyes, it may also cause side effects on the recognition of eyes.



## Highlights
- [x] Develop a Live2D model.
- [x] Add two events about eyes: half-opening and eyeball rotation.
- [x] Optimize some parameters to improve recognition performance.
- [x] Design a multi-functional display window which is more convenient and feasible for live streaming.



## File Description

| File/Folder | Description |
| :---: | --- |
| UnityAssets | Unity materials for those who want to make Live2D VTuber by themselves, please visit [tutorial](https://github.com/KennardWang/VTuber-MomoseHiyori/issues/3). |



## References

+ [Head pose estimation](https://github.com/yinguobing/head-pose-estimation) by Yin Guobing.
+ [Face alignment](https://github.com/1adrianb/face-alignment) by Adrian Bulat.
+ [Gaze tracking](https://github.com/antoinelame/GazeTracking) by Antoine Lamé.
+ [VTuber Unity project](https://github.com/kwea123/VTuber_Unity) by AI葵.
+ [Live2D model](https://www.live2d.jp/en/terms/live2d-free-material-license-agreement/) by kani_biimu.
+ [How to update parameters of Live2D model in Unity](https://docs.live2d.com/cubism-sdk-tutorials/about-parameterupdating-of-model/?locale=ja).
+ [TCP socket in C#](https://blog.csdn.net/u012234115/article/details/46481845).
+ [How to create a display window](https://blog.csdn.net/qq_39097425/article/details/81664448).



## Releases

[![badge](https://img.shields.io/badge/release-v2.0.0-FF7800)](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0)



## Maintainers

![badge](https://img.shields.io/badge/maintenance-YES-EF2D5E) [@KennardWang](https://github.com/KennardWang)



## Contributing

Feel free to [open an issue](https://github.com/KennardWang/VTuber-MomoseHiyori/issues) or submit [PRs](https://github.com/KennardWang/VTuber-MomoseHiyori/pulls).



## License

[![license](https://img.shields.io/github/license/KennardWang/VTuber-MomoseHiyori)](LICENSE) © Kennard Wang ( 2020.6.27 )
