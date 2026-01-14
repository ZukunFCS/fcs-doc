## Mayaの起動  

```{warning}
FCSとMayaを接続するためには、必ずFCSのメニューからMayaを起動する必要があります。  
```

```{figure} images/M001.png
:width: 80%
:align: center

```  

- Open Scene：Mayaシーンを開く  
- Launch：Mayaの起動+Mayaシーンを開く   
- Sync：FCS上での操作をMayaと連動させる   


```{note}
 - Open Sceneをクリックすると、設定したMaya Sceneを開き直すことができます  
 - Launchをクリックすると、session作成時に設定したMaya Sceneが自動で起動します  
```
  

 - Maya&rarr;Launch&rarr;Mayaバージョンの選択でMayaを起動  
例：今回キャラクターデータを作成したMayaのバージョンはMaya2020なので2020を選択しています。
```{figure} images/M002.png
:width: 80%
:align: center
```
  
```{note}
Mayaバージョンの誤クリックを防ぐため、Session作成時に設定したMaya Version以外はクリックできないように、ブラックアウトしています。
```
  
### トラブルシューティング  

#### Launchで指定したMayaバージョンが開けない場合  


```{figure} images/S014.png
:width: 80%
:align: center

session作成時に設定した項目は File&rarr;Session&rarr;info で確認することができます。  

```

```{figure} images/S015.png
:width: 80%
:align: center

New Sessionで設定したMaya Verがinfoで反映されていない場合は、info画面のMaya Versionを右クリックし、Editから変更ができます。
```

```{figure} images/S016.png
:width: 80%
:align: center

プルダウンからMaya Versionを設定してください。
```
  
```{attention}
設定の変更後は必ずSaveボタンを押してください
```
