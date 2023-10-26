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
  <img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/Dlib-008000?logo=dlib&logoColor=fff&style=for-the-badge" />
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

👋 Hello, I am Momose Hiyori, a Live2D VTuber from Japan. My parents are Cubsim and Unity, my teachers are OpenCV and Deep Learning. I am really good at mimicking faces including poses and expressions, it is a pleasure to meet you all and look forward to being good friends~ ❤️🧡🩷🩵💟💗🥰💕

<br>

<p align = "center">
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack1.gif" width = "400px" height = "210px"/>
    &nbsp;
    <img src = "https://kennardwang.github.io/ImageSource/VTuber-MomoseHiyori/FaceTrack2.gif" width = "400px" height = "210px"/>
</p>

- [x] Head: 6 degrees of freedom.
- [x] Eyes: opening, half-opening, glare, closing, blinking, eyeballs rotation.
- [x] Eyebrows: raising.
- [x] Mouth: opening and closing, grinning and pouting.



## Table of Contents

- [Development Environment](#development-environment)
- [Install](#install)
- [Usage](#usage)
- [File/Folder Description](#filefolder-description)
- [Calibration Algorithms](#calibration-algorithms)
- [References](#references)
- [Releases](#releases)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)



## Development Environment

| <!-- --> |                                                   <!-- -->                                                   |
| :------: | :----------------------------------------------------------------------------------------------------------: |
|  System  |                                                Windows 10 x64                                                |
| Language |                                    Python 3.8 (algorithm), C# (Unity Script)                                 |
|   IDE    |     PyCharm 2019.2.5 (algorithm), Live2D Cubism Editor 4.0 (Live2D model), Unity 2019.4.1f1 LTS (Engine)     |



## Install

1. Install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows), [Unity](https://unity.com/releases/editor/whats-new/2019.4.1) and Python 3.8 (recommend [Anaconda](https://www.anaconda.com/products/individual)).
2. Download the executable file from the latest [release](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v3.1.0).
3. Environment configuration.

    ```
    git clone https://github.com/KennardWang/VTuber-MomoseHiyori.git
    cd VTuber-MomoseHiyori
    conda env create -f environment.yml
    ```
   
4. Activate environment and install dependencies.

    ```
    conda activate l2d-vtb
    pip install -r requirements.txt
    ```
   
5. There are 2 types of running environments, please choose the correct one based on individual conditions.
   + CPU env
       + Install **dlib**, my version is v19.24.2.
     
         ```
         conda install -c conda-forge dlib
         ```
         
    + GPU env
        + Install **scipy** with version > 0.16, using `conda` is faster than `pip`.

          ```
          conda install scipy
          ```
  
        + Windows
            + Install [CUDA v10.2 & CUDNN v8.3.1](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/environment).
            + Install [Pytorch](https://pytorch.org/).

              ```
              pip install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
              ```
  
        + MacOS (ARM) with Apple M1
            + Install [Pytorch](https://pytorch.org/).
         
              ```
              conda install pytorch torchvision torchaudio -c pytorch-nightly
              ```
  
        + (Optional) Download models in [ckpts](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/dependency), unzip and place it at `face_alignment/ckpts`. If not, it will automatically download from the site.



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
    CPU env (left) has higher FPS that may perform better in VTuber, but lower robostness that cannot recognize well if some parts of the face are covered.
</p>
<p align = "center">
    GPU env (right) has higher robostness, better fluency and consecutiveness but lower FPS because of busier data IO.
</p>

<br>

**Step 2 : Connect Unity**

1. Run the Unity executable file.
2. Run the command according to your env.
   + CPU env
     
     ```
     python main.py --debug --connect
     ```
     
   + GPU env
  
     ```
     python main.py --debug --gpu --connect
     ```

**Optional : Set Parameters**

There are some parameters you can change. The default port number is 14514, you could set another port number via `--port=PORT_NUMBER`, but keep it the same as that in the Unity client. Moreover, you can set the camera via `--cam=CAM_INDEX` if you have more than one camera, the default camera index is 0. Please check the guidance of all parameters by using `python main.py --help`.

<br>

**Tips : Improve Performance**

+ Use spotlight: Try to make your face look brighter, the spotlight probably shows a better effect than the natural light.
+ Adjust face position: The debug mode of the camera may help you to know the position of your face. Try to put your face in a central position, and let the frame extend but not reach the boundary.
+ No glasses: Wearing glasses may influence the accuracy of recognition on eyes.
+ Show forehead: If your hair is so long that covers your eyes, it may also cause side effects on the recognition of eyes.



## File/Folder Description

| File / Folder | Description                                                                                                                                                   |
| :---------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| UnityAssets | Unity materials for those who want to make Live2D VTuber by themselves, please visit [tutorial](https://github.com/KennardWang/VTuber-MomoseHiyori/issues/3). |
| face_alignment | Module for face detection and landmarks by a powerful face alignment network (FAN), has better performance under GPU env. |
| face_pose | Module for face pose detection, contains the pose estimator and stabilizer. |
| tests | Test folder for GitHub Action. |
| main.py | Main program. |
| sock.py | File with Socket class. |
| utils.py | File with utility functions. |



## Calibration Algorithms

Obviously, the position of landmarks is meaningless. In most cases, we focus on the ratio (or aspect ratio) which could describe the size, because in Unity, we use a scrolling bar to control actions or events. However, the ratio is mostly not perfect correspondence with the bar value. An interesting question is how to calibrate and map the ratio to the bar value. There are some feasible methods I implement in this project:

```python
# Copyright 2023 © Yuyang (Kennard) Wang.

# For some values with distinct boundaries, e.g., eyeballs, we can use linear transformation.
def calibrate_param1(param1):
    """Calibrate parameter1"""
    return (param1 + a) * b


# For some values with overlapping boundaries but main body has significant differences,
# e.g., eyeOpen, eyebrow, we can set return as discrete values instead of continuous values.
def calibrate_param2(param2, last_state_value):
    """Calibrate parameter2"""
    flag = False  # jump out of current state

    # values of state 1, 2, ..., N are from small to large
    if last_state_value == state1_value:
        if param2 > jump_threshold1:
            flag = True
    elif last_state_value == state2_value:
        if abs(param2 - central_point) > jump_threshold2:
            flag = True
    elif ... :
        if ... :
            flag = True
    else:
        if param2 < jump_thresholdn:
            flag = True

    if flag:
        # state_threshold1 is between state1 and state2, less than jump_threshold1
        if param2 <= state_threshold1:
            current_state_value = state1_value
        # state_threshold2 is between state2 and state3
        elif param2 > state_threshold1 and param2 <= state_threshold2:
            current_state_value = state2_value
        elif ... :
            current_state_value = state..._value
        else:
            current_state_value = stateN_value
    else:
        current_state_value = last_state_value

    return current_state_value


# If you want a smooth effect, you can use a piecewise function to replace discrete states, e.g., mouthWidth
def calibrate_param3(param3):
    """Calibrate parameter3"""
    if param3 <= threshold1:
        bar_value = bar_value_min
    elif param3 > threshold1 and param3 <= threshold2:
        bar_value = k * param3 + b
    elif ... :
        bar_value = ...
    else:
        bar_value = bar_value_max

    return bar_value
```


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

[![badge](https://img.shields.io/badge/release-v3.1.0-FF7700)](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v3.1.0) [![badge](https://img.shields.io/badge/release-v2.0.0-FF5500)](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v2.0.0) [![badge](https://img.shields.io/badge/release-v1.2.0-FF3300)](https://github.com/KennardWang/VTuber-MomoseHiyori/releases/tag/v1.2.0)



## Maintainers

![badge](https://img.shields.io/badge/maintenance-Maybe-EF2D5E) [@KennardWang](https://github.com/KennardWang)



## Contributing

Feel free to [open an issue](https://github.com/KennardWang/VTuber-MomoseHiyori/issues) or submit [PRs](https://github.com/KennardWang/VTuber-MomoseHiyori/pulls). Be careful that the submitted code needs to pass format tests and pytests by GitHub Actions, please self-check before pulling requests.

+ flake8 format test (Windows, Mac and Linux) [![1](https://github.com/KennardWang/VTuber-MomoseHiyori/actions/workflows/flake8.yml/badge.svg)](https://github.com/KennardWang/VTuber-MomoseHiyori/actions/workflows/flake8.yml)

  ```
  flake8 --exclude=face_alignment,face_pose --ignore=E501 .
  ```

+ pytest (Windows, Mac and Linux) [![2](https://github.com/KennardWang/VTuber-MomoseHiyori/actions/workflows/pytest.yml/badge.svg)](https://github.com/KennardWang/VTuber-MomoseHiyori/actions/workflows/pytest.yml)

  ```
  pytest tests/test_win.py
  pytest tests/test_mac.py
  pytest tests/test_linux.py
  ```



## License

[![license](https://img.shields.io/github/license/KennardWang/VTuber-MomoseHiyori)](LICENSE) © Kennard Wang ( 2020.6.27 )
