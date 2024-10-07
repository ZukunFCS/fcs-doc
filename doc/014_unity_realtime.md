## Unityとのリアルタイム通信
FCSRTは、Unityにリアルタイムでデータ送信することができます。  
データ送信をするためには、FCS側とUnity側でそれぞれ操作が必要です。  

### Unity側の設定
1. FCS_RealtimeFaceAnim.cs, FCSReceiveController.csをUnityにインポートします。<br>
![](images/unityrealtime_01.png)<br><br>
2. インポートしたスクリプトを動作させたいGameObjectにアタッチします。<br>
![](images/unityrealtime_02.png)<br><br>
3. アタッチしたFCS_RealtimeFaceAnimのインスペクターでFaceを設定します。<br>
   選択するObjectは、顔のObject(BlendShapesが設定されているObject)であればOKです。<br>
![](images/unityrealtime_03.png)<br><br>
4. アタッチしたFCSReceiveControllerのインスペクターでIPAddressとPortを設定します。<br>
   IPAddressとPortは、FCSRT側の設定と同じIPAddressとPortを指定します。<br>
5. FCSRT側のSetup終了後、ゲーム再生を実行します。<br>

### FCSRT側の設定
1. FCSRTを起動します。<br>
![](images/fcsrt_01.png)<br><br>
2. SendPortを指定します。このポート番号はUnity側で設定したポート番号と同じにする必要があります。<br>
   Unity側のポート設定を確認後、Setupbroadcastingをクリックします。<br>
3. Unity側との通信が確立された場合、StatusとLastUpdateがConnectedに変わります。<br>
  また、Start broadcastingが非表示になり、Resetボタンが表示されます。<br>
![](images/fcsrt_02.png)<br><br>
4. Srcタブ内のCamera Deviceから使用するカメラを選択し、Openをクリックします。<br>
  右側のエリアにカメラからの映像、または指定した動画ファイルの映像が表示されます<br>
5. Rendererタブ内のStartをクリックし、コントローラ値の送信を開始します。<br>


