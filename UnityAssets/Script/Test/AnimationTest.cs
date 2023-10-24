using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using Live2D;
using Live2D.Cubism.Core;
using Live2D.Cubism.Framework;

// Reference: https://docs.live2d.com/cubism-sdk-tutorials/about-parameterupdating-of-model/?locale=ja

public class AnimationTest : MonoBehaviour
{
    private CubismModel Momose;
    private CubismParameter parameter;
    private float _t;  // time controller

    void Start()
    {
        Momose = this.FindCubismModel();
        _t = 0;
    }

    void Update()
    {
        _t += (Time.deltaTime * 4f); 
        float value = Mathf.Sin(_t) * 30f;  // amplitude
        parameter = Momose.Parameters[2];  // head angle Z
        
        parameter.Value = value;  // set value
        Debug.Log(parameter.Value);
    }
}
