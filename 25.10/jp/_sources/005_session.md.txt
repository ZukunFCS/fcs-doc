## Session作成もしくはオープン
FCSではアクター情報、キャラクター情報、Mayaシーン情報とその解析データを紐づけたファイルのことを「Session」と呼びます。

FCS起動後、Sessionデータへアクセスするため
「New...（新規作成）」または「Open（開く）」を実行します。

```{note}
初めにSessionに関わる設定を行うことで、Mayaを別途操作することなくFCS上のボタンでスムーズに作業を開始することができます。
```

### Create new Sessionで作成されるフォルダ構造  

| 色 | 内容 | 
|:-------------|:--------------:|
| 赤枠      | Project Folderで作成されるフォルダ           |
| 青枠      | Actorで作成されるフォルダ           |
| 緑枠      | Characterで作成されるフォルダ             |


```{figure} images/folder.jpg
:width: 80%
:align: center
```

| フォルダ | 内容| 説明 | 
|:-------------|:--------------:|:--------------:|
| Facial |       | 動画やMayaシーンデータ等素材を保存する場所           |
|   L   | Assets           | Mayaのプロジェクトファイル（Assets以下）を保存する場所  |
|   L   | RecData             | ROM体操やFCSで解析したい動画を保存する場所 |
|   L   | Scene             | アニメーション出力時のデフォルト出力先  |
|   L   | SetData             | アニメーション出力で「audio」を選択した場合にはwavファイルが、「Frame」「Landmark Frame」を選択した場合は連番画像が作成され、保存される    |
| FCS |       | 解析に使用するデータが保存されるプロジェクトフォルダ            |
|   L   | Assets           | Actorで作成したフォルダ。Actorで入力した名前が表記される   |
|   L   | RecData             | Characterで作成したフォルダ。Characterで入力した名前が表記される |
|   L   | Scene             | 作成したProfileの編集データ（画像や数値情報）が保存される  |
|   L   | SetData             | 解析する動画のキャッシュが保存される |
|   L   | .lock      | 競合を防ぐためのロックファイル。起動時/終了時に自動で作成/消去される               |
|   L   | fcs_session.yaml      | Session情報を保存しているファイル             |


### Sessionの新規作成   

 - File &rarr; Session&rarr;New...を選択
```{figure} images/S001.jpg
:width: 80%
:align: center
```

```{figure} images/S002.jpg
:width: 80%
:align: center
```  
| フォルダ | 説明 | 
|:-------------|:--------------:|
| Project Folder | FCSの作業データを置きたい場所を指定 | 
| Actor | モーションキャプチャアクター名    | 
| Character | 3Dモデルのキャラクター名   | 
| Maya Scene | 3DモデルのMayaシーンへのパス   | 
| Maya Base | Assets、workspace.melがあるフォルダへのパス   | 
| Maya Ver | 3Dモデルを作成したMayaのバージョンを指定 | 

1. Project Folderの設定

    Browseボタンをクリックし、Project Folderを指定するためウィンドウを起動します。  
    
    ```{figure} images/S003.jpg
    :width: 80%
    :align: center

    FCSのデータを保存したい任意のフォルダを選択
    ```

    Project Folderを作成します。  

    ```{figure} images/S004.jpg
    :width: 80%
    :align: center

    Create
    ```

    問題なく作成できたらポップアップが表示されます。  

    ```{figure} images/F001.jpg
    :width: 80%
    :align: center

    Close
    ```

    エクスプローラーで「Facial」「FCS」のフォルダが作成されます。
    ```{figure} images/F003.jpg
    :width: 80%
    :align: center
    ```

    ```{note}
    Project Folder作成後、Project Folder&rarr;Facial&rarr;Assetsフォルダに紐付けるMayaシーンをProject Folder&rarr;Facial&rarr;Recdataフォルダに解析したい動画を移動しておくことを推奨します。  
    ※別の場所に保存していてもアクセスできます。
    ```

    ```{figure} images/F004.jpg
    :width: 80%
    :align: center

    Example assets folder
    ```

    ```{figure} images/F005.jpg
    :width: 80%
    :align: center
    
    Example RecData folder
    ```


2. Actorの設定

    「+」ボタンをクリックし、ActorFolderを作成するための 「Create new actor folder」ウィンドウを起動します。

    - 「Actor Name」に登録したい名前を入力  
    - 「Actor」＝モーションキャプチャアクター名  

    - Create
    ```{figure} images/S006.jpg
    :width: 80%
    :align: center
    ```

    問題なく作成できたらポップアップが表示されます。  
    - close
    ```{figure} images/F006.jpg
    :width: 80%
    :align: center
    ```

    エクスプローラーでProject Folderフォルダ直下に入力したActerフォルダが作成されます。
    ```{figure} images/F007.jpg
    :width: 80%
    :align: center
    ```

3. Characterの設定

    「+」ボタンをクリックし、characterFolderを作成するための「Create new character Folder」ウィンドウを起動します。  
    - 「Character Name」の入力欄に登録したい名前を入力

    - Create
    ```{figure} images/S008.jpg
    :width: 80%
    :align: center
    ```

    エクスプローラーでActorフォルダ直下に入力したCharacterフォルダが作成されます。
    ```{figure} images/F008.jpg
    :width: 80%
    :align: center
    ```


4. MayaSceneの設定

    Browseボタンをクリックし、MayaSceneを指定するためウィンドウを起動します。  
    - MayaSceneデータのパスを指定
    ```{figure} images/S009.jpg
    :width: 80%
    :align: center
    ```

5. MayaBaseの設定

    Browseボタンをクリックし、MayaBaseを指定するためウィンドウを起動します。  
    - workspace.melがある場所(Mayaシーンのプロジェクト設定で登録している場所)を指定  
    ```{attention}
    FCS上でポップアップするウィンドウにはworkspace.melが表示されません  
    ``` 
    ```{figure} images/S010.jpg
    :width: 80%
    :align: center
    ```

6. MayaVerの設定

    ```{figure} images/S011.jpg
    :width: 80%
    :align: center

    Sceneを作成したMayaのバージョンを指定
    ```

    全て入力を終えたらSaveボタンを押してください。  
    ```{figure} images/S012.jpg
    :width: 80%
    :align: center

    Save
    ```


    
    ```{figure} images/F009.jpg
    :width: 80%
    :align: center
    
    エクスプローラーでcharacterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。  
    ```

    ```{note}
    .lockファイルは
    作業中にほかの人からのアクセスを防ぐためのものです。  
    正常に終了した際には自動で削除されます。
    ```

    ```{note}
    不正に終了するなどして.lockファイルが残ってしまった場合、  
    FCSの起動時にポップアップから削除するか、  
    .lockファイルをエクスプローラーで直接削除してください。
    ```

### 既にSessionが作成されている場合

履歴またはfcs_session.yamlファイルからSessionを開いてください。 

#### 履歴から開く場合

以前にSessionを起動している場合、File&rarr;Session&rarr;Openの下に履歴が表示されます。  
 - 作業したいデータをクリック
```{figure} images/P16_Session_log.jpg
:width: 80%
:align: center
```

#### fcs_session.yamlファイルから開く場合

 - File&rarr;Session&rarr;Open&rarr;Open...  
OpenSessionウィンドウが開かれたらローカルとネットワークドライブが表示されます。  

 - Characterフォルダ直下にあるfcs_session.yamlファイルを選択し、開く
```{figure} images/S017.jpg
:width: 80%
:align: center
```

### Seesionを開く際の注意

#### Sessionの同時起動について

```{warning}
Sessionの新規作成/Open後、続けて別のSession作成や起動は出来ません。  
別のSessionを開きたい場合は、現在のSessionを終了し、FCSの再起動後開きなおしてください。
```

#### 「Maya Verの設定」をしても反映されない場合

Session作成時に設定した項目は File&rarr;Session&rarr;info で確認することができます。
```{figure} images/S014.jpg
:width: 80%
:align: center
```

New Sessionで設定したMayaVerがinfoで反映されていない場合は、info画面のMaya Versionを右クリックし、Editから変更ができます。
```{figure} images/S015.jpg
:width: 80%
:align: center
```
```{figure} images/S016.jpg
:width: 80%
:align: center
```

```{attention}
設定の変更後は必ずSaveボタンを押してください
```
