## FCSRT
FCSRTは、リアルタイム通信用のソフトウェアです。<br>
UnityやUnrealEngineなどゲームエンジンと接続すると、コントローラの値をリアルタイムで送信することができます。<br>

### UI説明   
![](images/fcsrt_01.png)<br><br>
左がコントロールパネル、右がカメラ・動画表示エリアです。<br>
- Rendererタブ<br>
    - Host: 接続先のIPアドレス<br>
    - SendPort: TCP接続用のポート番号<br>
    - UDPPort: UDP接続用のポート番号<br>
    - Status: 接続状態を表示します。<br>
    - LastUpdate: 最後に送信されたデータの時間を表示します。<br><br>
- Srcタブ<br>
    - Source: ソースの種類を選択(LiveCamera, VideoFile)<br>
        - LiveCamera<br>
            Camera Device: カメラデバイスを選択<br>
        - VideoFile<br>
            File Name: 動画ファイルのフルパス<br>
    - Rotate: 表示するカメラ画面の回転<br>
    - Preview: プレビュー表示<br>
    - Open: カメラ・動画映像を表示します。値の取得も同時に開始します。<br><br>
- PostProcessingタブ<br>
    - Detect: 検出方法を選択します。<br>
    - Solver Load: ファイルからソルバーをロードします。<br><br>
- Visタブ: コントローラの一覧<br>

### 操作説明 
**コントローラ値送信までの手順**<br>
1. FCSRTを起動します。<br>
2. SendPortを指定します。このポート番号は接続先で設定したポート番号と同じにする必要があります。<br>
  接続先のポート設定を確認後、Setup broadcastingをクリックします。<br>
3. 接続先との通信が確立された場合、StatusとLastUpdateがConnectedに変わります。<br>
  また、Start broadcastingが非表示になり、Resetボタンが表示されます。<br>
![](images/fcsrt_02.png)<br><br>
4. Camera Deviceから使用するカメラを選択、または VideoFileに動画ファイルパスを指定して、Openをクリックします。<br>
  右側のエリアにカメラからの映像、または指定した動画ファイルの映像が表示されます<br>
5. RendererタブのStartをクリックし、コントローラ値の送信を開始します。<br>

**接続後の操作**<br>
- StartボタンとStopボタンはトグルになっており、Stopボタンを押すことで送信を一時停止することができます。<br>
- Resetボタンをクリックすると、コントローラ値の送信を停止し、接続先との通信を切断します。<br>

**送信するコントローラの変更について**<br>
PostProcessingタブ内のLoadからFCSから出力したSolverをダウンロードすることができます。<br>
正常にSolverがロードされた場合、Visタブにロードしたコントローラが表示されます。<br>

### 詳細説明
**通信プロトコルについて**<br>
FCSRTの通信プロトコルは、TCPとUDPを用いています。<br>
TCP通信は、コントローラ値とUDP用のポート番号をクライアントへ確実に送信するために使用します。<br>
UDP通信は、コントローラ値をリアルタイムで送信するために使用します。<br>
このため、通信の流れは以下のようになります。<br><br>
![](images/fcsrt_03.png)<br><br>
- UDPのポート番号は、クライアントがTCPで接続するたびに変更されます。<br>
- UDPの終了通知として、コントローラ値が-1の配列が送信されます。<br><br>

クライアントの実装は、以下の実装が必要になります。
  - TCP通信で接続してコントローラ値とUDPポート番号をFCSRTから取得する処理<br>
  - 取得したUDPポートを使ってUDPクライアントを作成し、FCSRTからコントローラ値を受信する処理<br>
  
