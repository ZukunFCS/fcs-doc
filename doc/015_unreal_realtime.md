## UnrealEngineのリアルタイム通信
FCSRTは、UnrealEngineにリアルタイムでデータ送信することができます。<br> 
データ送信をするためには、FCS側とUnrealEngine側でそれぞれ操作が必要です。<br>

### UnrealEngine側の設定
UnrealEngine側では、FCSLiveLinkプラグインを使用する必要があります。<br>
FCSLiveLinkプラグインは、UnrealEngine5.3で利用可能です。<br>
FCSLiveLinkプラグインは以下からダウンロードできます。<br>

#### 接続設定
1. UnrealEngineのメインウィンドウから、[Edit]>[plugins]を選択して、プラグインウィンドウを開きます。<br>  
2. プラグインウィンドウからFCSLiveLinkにチェックを入れます。<br>
3. [Window]>[Virtual Production]>[Live Link]を選択して、LiveLinkウィンドウを開きます。<br>
4. Livelinkウィンドウ右上隅にある[+Source]を選択します。<br>
5. [FCSLiveLink]を選択し、表示されたUIからFCS入力と一致するようにIPAddress, PortNumber, SubjectNameを設定します。<br>
設定後、OKを選択します。<br>
6. Sourceが作成され、SourceType欄にFCSLiveLinkが追加されます。<br>

#### ABP設定
FCSLiveLinkを使用して、SkeletalMeshを動かすためには、AnimationBlueprintを作成する必要があります。<br>

1. コンテンツブラウザを右クリックして、[Animation]>[Animation Blueprint]を選択し、新しいAnimationBlueprintを作成します。<br>
2. 作成したAnimationBlueprintを開きます。<br>
3. EventGraphを開き、UpdateAnimationノードからEvaluateLiveLinkFrameノードを作成して接続します。<br>
4. EvaluateLiveLinkFrameノードの[Subject]プルダウンに[ControllerValues], [Role]プルダウンに[FCSLiveLinkRole]を設定します。<br>
5. [Data Result]ピンからドラッグし、[Break FCSAnimationBlueprintData]ノードを作成します。<br>
6. [Break FCSAnimationBlueprintData]ノードkar

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
