using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System;
using System.Text;
using System.Threading;
using System.Net;
using System.Net.Sockets;

// Reference: https://blog.csdn.net/u012234115/article/details/46481845

public class SocketTest : MonoBehaviour
{
    // basic setting
    Socket clientSocket;
    Socket serverSocket;
    const string IP = "127.0.0.1";
    const int PORT = 14514;

    // Data
    byte[] recData = new byte[1024];

    void init()
    {
        // Socket initialization
        serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        IPEndPoint ipEndPoint = new IPEndPoint(IPAddress.Parse(IP), PORT);
        serverSocket.Bind(ipEndPoint);
        serverSocket.Listen(100);

        // start a new thread to update parameters
        Thread connect = new Thread(new ThreadStart(DataReception));
        connect.Start();
    }

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Start");
        init();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void SocketConnect()
    {     
        if (clientSocket != null) { clientSocket.Close(); }
        clientSocket = serverSocket.Accept();
        Debug.Log("Connect");
    }

    void DataReception()
    {
        SocketConnect();

        while (true)
        {
            recData = new byte[1024];
            int len = clientSocket.Receive(recData);

            if (len == 0)
            {
                SocketConnect();
                continue;
            }

            // change data type to string, then to float
            string str = Encoding.ASCII.GetString(recData, 0, len);
            string[] para = str.Split(' ');  // parameters group

            float v = Convert.ToSingle(para[5]);  
            Debug.Log(v);
        }
    }
}
