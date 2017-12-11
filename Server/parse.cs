// Get the latest webcam shot from outside "Friday's" in Times Square
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
public class parse : MonoBehaviour
{
    public GameObject temp;
    public float Delay = 60f;
    private string str = string.Empty;

    IEnumerator GetDataFromWebpage(string url)
    {
        WWW webpage = new WWW(url);
        while (!webpage.isDone) yield return false;
        string content = webpage.text;
        str = content.Substring(10, 5);
        Debug.Log(content.Substring(10, 5));

    }

    void Start()
    {
        
    }

    private void Update()
    {
        StartCoroutine(GetDataFromWebpage("http://a1c7e8a6.ngrok.io/temp"));
        temp.gameObject.GetComponent<TextMesh>().text = str;
        StartCoroutine(delay());
    }

    private IEnumerator delay()
    {
        yield return new WaitForSeconds(Delay);
    }
}

