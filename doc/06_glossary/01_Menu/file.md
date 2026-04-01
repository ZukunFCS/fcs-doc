## File

Fileメニューのうち、Session（セッション）ファイルの新規作成、保存、読み込みなど、プロジェクト管理に関連するメニュー項目について説明します。  
※[File ▶ Settings](settings.md)については別ページを参照ください。  

```````{tab-set}

``````{tab-item} File

<br>

`````{grid} 1 1 2 2 
:gutter: 3
:items-align: top

````{grid-item}
:child-align: top

```{image} /images/06_glossary_Menu_File.jpg
:width: 100%
```

````

````{grid-item}

① Settion：Session(セッション)ファイル関連メニュー  

② Settings：[Settings](settings.md)参照してください。  

③ Quit：FCSを終了し「.Lockファイル」を削除  
````

`````


<br>


``````

`````{tab-item} Session ▶

<br>

Session(セッション)ファイルに関連したメニューです。  
Sessionを開く、設定の変更、新規Sessionの作成などを実行することができます。  

```{figure} /images/06_glossary_Menu_File_Session.jpg
:width: 40%
:align: center
```
<br>

① New：Sessionを新規で作成、「**Create new Session**」ウィンドウを開く  

② Open：Sessionを開く  
　・Open...：ダイアログから .yaml ファイルを選択して Session を開きます。  
　・「パス」：最近使用した Session のパスが表示されます。  

③ Info：「**Session Data**」ウィンドウを開く  

④ Export：Session をエクスポートするための「**Export Session**」ウィンドウを開く

<br>

`````


`````{tab-item} Create new Session

<br>

・Session ▶ New  
　Sessionを新規作成する際に開かれるウィンドウです。  

```{figure} /images/03_workflow_session_create_name.jpg
:width: 80%
:align: center
```

<br>

① Project Folder：FCSの作業データを置きたい場所（Root）のパス入力欄  
　【Browse...】：ダイアログを開いてプロジェクトフォルダの作成先を入力します。    
　【Create】：パス入力後、FCSのプロジェクトフォルダを作成します。  

② Actor：解析する動画のアクター（演技者）名入力欄  
　※既に該当アクターのフォルダが存在する場合、プルダウンから選択できます。  
　【+】「Create new actor」ウィンドウを起動し、アクター名のフォルダを作成します。  
　　アクター名はプルダウンに追加されます。  

③ Character：3Dモデルのキャラクター名入力欄    
　【+】「Create new character folder」ウィンドウを起動し、キャラクター名のフォルダを作成します。  
　　キャラクター名はプルダウンに追加されます。  

④ Maya Scene：3DモデルのMayaシーンのパス入力欄  
　【Browse...】：ダイアログを開いてパスを入力します。    

⑤ Maya Base：「workspace.mel」があるフォルダのパスを入力  
　【Browse...】：ダイアログを開いてパスを入力します。    

⑥ Maya Ver：3Dモデルを作成したMayaのバージョンを指定  


<br>

```{rubric} **Create new Sessionで作成されるフォルダ構造**
```

<br>

<!--start_here_folder-->

```{figure} /images/03_workflow_session_folder_structure.jpg
:width: 80%
:align: center
```

\*赤枠：Project Folderで作成されるフォルダ  
\*青枠：Actorで作成されるフォルダ  
\*緑枠：Characterで作成されるフォルダ  

- **Facial**　：動画やMayaシーンデータ等素材を保存する場所  
    - **Assets**：Mayaのプロジェクトファイル（Assets以下）を保存
    - **RecData**：ROM体操やFCSで解析したい動画を保存
    - **Scene**：アニメーション出力時のデフォルト出力先
    - **SetData**：アニメーション出力で「audio」を選択した場合のwav出力先

<br>

- **FCS**　：解析に使用するデータが保存されるプロジェクトフォルダ
    - **Actor**：Actor名（入力した名前）のフォルダ
        - **Character**：Character名（入力した名前）のフォルダ
            - **RetargetData**：作成したProfileの編集データ
            - **VideoData**：解析動画のキャッシュ
            - **.lock**：競合防止用のロックファイル
            - **fcs_session.yaml**：Session情報を保存しているファイル  

<!--end_here_folder-->

<br>

`````

`````{tab-item} Session Data

<br>

・Session ▶ info  
　右クリックメニューから内容のコピーや編集を行うことができます。  

```{figure} /images/06_glossary_Menu_File_Session_info.jpg
:width: 80%
:align: center
```

<br>

| 項目 | 説明 | 右クリックメニュー| 
|:-------------:|:--------------|:--------------|
|① Project Folder|プロジェクトフォルダのパス|パスのコピー|
|② Actor|アクター名|リネーム・コピー|
|③ Character|キャラクター名|リネーム・コピー |
|④ Maya Scene|Mayaシーンパス| パスのコピー・変更|
|⑤ Maya Base|workspace.melのパス| パスのコピー・変更|
|⑥ Maya version| Mayaバージョン|コピー・変更|
|⑦ Profile Count|セッション内のプロファイルの数|コピー|
|⑧ Video Count|セッションにインポートした動画の数 | コピー|
|⑨ Created at| セッション作成日時| コピー|
|⑩ Created by| セッション作成者| コピー|
|⑪ Last saved at| 最終保存日時| コピー|
|⑫ Last saved by| 最終保存者| コピー|

<br>

`````


`````{tab-item} Export Session

<br>

・Session ▶ Export  
　作業したSessionを出力することができます。  

Sessionのエクスポートについては[作業フロー/エクスポート](../../03_workflow/08_export.md)を参照ください。

<br>


```{include} ../../03_workflow/08_export.md
    :start-after: <!--start_here-->
    :end-before: <!--end_here-->
```

`````

```````

<br>

```{rubric} **Menu説明 目次**  
```

```{include} index.md
    :start-after: <!--start_here-->
    :end-before: <!--end_here-->
```
