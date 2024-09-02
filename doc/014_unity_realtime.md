## Unityとのリアルタイム通信
FCSは、Unityにリアルタイムでデータ送信する機能を持っています。  
この機能を使うためには、FCS側とUnity側でそれぞれ操作が必要です。  

### Unity側の設定
1. FCS_RealtimeFaceAnim.csをUnityにインポートします。<br>
![](images/unityrealtime_01.png)<br><br>
2. インポートしたスクリプトを動作させたいGameObjectにアタッチします。<br>
![](images/unityrealtime_02.png)<br><br>
3. インスペクターから、Faceを選択します。<br>
   選択するObjectは、顔のObject(BlendShapesが設定されているObject)であればOKです。<br>
![](images/unityrealtime_03.png)<br><br>

### FCS側の設定
1. なんか設定して送信します。