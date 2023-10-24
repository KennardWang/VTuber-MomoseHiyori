using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Start : MonoBehaviour
{
    // Initialization
    public InputField input;
    public int num;

    public void initVtuber()
    {
        // Default port
        int port_number = 14514;

        // If text is not empty
        if (!input.text.Equals(""))
        {
            // The port number must be an integer
            if (int.TryParse(input.text, out num)){

                // Valid port number is 0~65535
                if(num >= 0 && num <= 65535) 
                { 
                    port_number = num;
                    Debug.Log("Port number: " + port_number);
                }
                else
                {
                    Debug.Log("Invalid port number: " + num);
                }
            }
            else
            {
                Debug.Log("Port number is not an integer!");
            }
        }

        // Save port number 
        PlayerPrefs.SetInt("port", port_number);
        PlayerPrefs.Save();

        // Jump to next scene
        SceneManager.LoadSceneAsync(1);
    }
}
