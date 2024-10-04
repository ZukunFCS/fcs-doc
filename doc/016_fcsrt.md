## FCSRT
FCSRTは、リアルタイム用のソフトウェアです。
UnityやUnrealEngineなどゲームエンジンと接続すると、コントローラの値をリアルタイムで送信することができます。<br>

**UI説明**   
1. FCSRT.exeを実行して起動します。 
![](images/fcsrt_01.png)<br><br>
Rndererタブ<br>
　Host: 接続先のIPアドレス<br>
　SendPort: TCP接続用のポート番号<br>
  UDPPort: UDP接続用のポート番号<br>
　Status: 接続状態を表示します。<br>
　LastUpdate: 最後に送信されたデータの時間を表示します。<br><br>
Srcタブ<br>
  Source: ソースの種類を選択(LiveCamera, VideoFile)<br>
  LiveCamera<br>
    Camera Device: カメラデバイスを選択<br>
  VideoFile<br>
    File Name: 動画ファイルのフルパス<br>
  Rotate: 表示するカメラ画面の回転<br>
  Preview: プレビュー表示<br>
  Open: カメラ・動画映像を表示します。値の取得も同時に開始します。<br>
PostProcessingタブ<br>
  Detect: <br>
  Solver: <br>
  Load: <br><br>
Visタブ: コントローラの一覧<br>

**操作説明** 
コントローラ値送信までの手順<br>
1. FCSRTを起動します。<br>
2. SendPortを指定します。このポート番号は接続先で設定したポート番号と同じにする必要があります。<br>
　 接続先のポート設定を確認後、Setupbroadcastingをクリックします。<br>
3. 接続先との通信が確立された場合、Status,LastUpdateがConnectedに変わります。<br>
![](images/fcsrt_02.png)<br><br>
4. Camera Deviceから使用するカメラを選択、または VideoFileに動画ファイルパスを指定して、Openをクリックします。<br>
5. RendererタブのStartをクリックし、コントローラ値の送信を開始します。<br>

接続後の操作<br>
StartボタンとStopボタンはトグルになっており、Stopボタンを押すことで送信を一時停止することができます。<br>
Start broadcastingを実行後、Resetボタンが表示されます。このボタンをクリックすると、コントローラ値の送信を停止し、接続先との通信を切断します。<br>

送信するコントローラの変更について<br>
postprocessingタブのLoadからSolverをダウンロードすることができます。正常にロードされた場合、Visタブにロードしたコントローラが表示されます。<br>

**詳細説明**
通信プロトコルについて<br>
　FCSRTの通信プロトコルは、TCPとUDPを用いています。<br>
　TCPは、コントローラ値とUDP用のポート番号をクライアントに確実に送信するために使用します。UDPは、コントローラ値をリアルタイムで送信するために使用します。<br>
　このため、通信の流れは以下のようになります。<br>
![](images/FCSRTPython_protocol.png)<br><br>
　UDPのポート番号は、クライアントがTCPで接続するたびに変更されます。<br>
  UDPの終了通知として、コントローラ値が-1の配列が送信されます。<br>
　クライアントの実装は、TCPで接続してコントローラ値とUDPポート番号を取得する処理と取得したUDPポートを使ってコントローラ値を受信する処理の実装が必要となります。<br>
  
