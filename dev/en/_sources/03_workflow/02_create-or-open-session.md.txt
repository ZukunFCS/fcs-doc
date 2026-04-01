## Sessionの作成・読み込み
FCSではアクター情報、キャラクター情報、Mayaシーン情報とその解析データを紐づけたファイルのことを「Session」と呼びます。

FCS起動後、Sessionデータへアクセスするため【New...（新規作成）】または【Open】を実行します。

```{note}
初めにSessionに関わる設定を行うことで、Mayaを別途操作することなくFCS上のボタンでスムーズに作業を開始することができます。
```

```{rubric} **Create new Sessionで作成されるフォルダ構造**
```

<br>


```{include} ../06_glossary/01_Menu/file.md
    :start-after: <!--start_here_folder-->
    :end-before: <!--end_here_folder-->
```

<br>


```{rubric} **Sessionの新規作成**
```
File &rarr; Session&rarr;New...を選択  

```{figure} /images/03_workflow_session_new_create.jpg
:width: 80%
:align: center
```

<br>
<br>

1. Project Folderの設定

    【Browse】ボタンをクリックし、Project Folderを指定するためウィンドウを起動します。  
    
    ```{figure} /images/03_workflow_session_folder_browse.jpg
    :width: 80%
    :align: center

    FCSのデータを保存したい任意のフォルダを選択
    ```
    
    <br>

    【Create】を押し、Project Folderを作成します。  

    ```{figure} /images/03_workflow_session_folder_create.jpg
    :width: 80%
    :align: center

    【Create】
    ```
    
    <br>
   
     問題なく作成できたらポップアップが表示されます。  

    ```{figure} /images/03_workflow_session_folder_close.jpg
    :width: 80%
    :align: center

    【Close】
    ```
    
    <br>

    エクスプローラーで【Facial】【FCS】のフォルダが作成されます。
    ```{figure} /images/03_workflow_session_folder_complete.jpg
    :width: 80%
    :align: center
    ```
    
    <br>
    
    ```{note}
    作成後、Project Folder&rarr;Facial&rarr;Assetsフォルダに紐付けるMayaシーンを、  
    Project Folder&rarr;Facial&rarr;Recdataフォルダに解析したい動画を  
    移動しておくことを推奨します。　※別の場所に保存していてもアクセスできます。
    ```

    ```{figure} /images/03_workflow_session_assets_folder.jpg
    :width: 80%
    :align: center

    例：Assetsフォルダ
    ```

    ```{figure} /images/03_workflow_session_recdata_folder.jpg
    :width: 80%
    :align: center
    
    例：RecDataフォルダ
    ```

    <br><br>
    
2. Actorの設定

    【+】ボタンをクリックし、ActorFolderを作成するための 【Create new actor folder】ウィンドウを起動します。  
    【Actor Name】に登録したい名前を入力し、【Create】を押します。  
    ※Actor ＝ アクター名  
    ```{figure} /images/03_workflow_session_actor_create.jpg
    :width: 80%
    :align: center
    ```

    <br>

    問題なく作成できたらポップアップが表示されます。
    ```{figure} /images/03_workflow_session_actor_close.jpg
    :width: 80%
    :align: center
    ```

    <br>

    エクスプローラーでProject Folderフォルダ直下に入力したActerフォルダが作成されます。
    ```{figure} /images/03_workflow_session_actor_folder.jpg
    :width: 80%
    :align: center
    ```

    <br><br>
    
3. Characterの設定

    【+】ボタンをクリックし、characterFolderを作成するための【Create new character Folder】ウィンドウを起動します。  
    【Character Name】の入力欄に登録したい名前を入力し、【Create】を押します。    
    ```{figure} /images/03_workflow_session_character_create.jpg
    :width: 80%
    :align: center
    ```

    <br>

    エクスプローラーでActorフォルダ直下に入力したCharacterフォルダが作成されます。
    ```{figure} /images/03_workflow_session_character_folder.jpg
    :width: 80%
    :align: center
    ```
    
    <br><br>

4. MayaSceneの設定

    【Browse】をクリックし、MayaSceneを指定するためウィンドウを起動します。  
    - MayaSceneデータのパスを指定します。
    ```{figure} /images/03_workflow_session_maya_scene_path.jpg
    :width: 80%
    :align: center
    ```

    <br><br>

5. MayaBaseの設定

   【Browse】をクリックし、MayaBaseを指定するためウィンドウを起動します。  
   workspace.melがある場所(Mayaシーンのプロジェクト設定で登録している場所)を指定してください。    
    ```{attention}
    FCS上でポップアップするウィンドウにはworkspace.melが表示されません  
    ``` 
    ```{figure} /images/03_workflow_session_maya_ver_browse.jpg
    :width: 80%
    :align: center
    ```

    <br><br>
    
6. MayaVerの設定
   
   Sceneを作成したMayaのバージョンを指定します。
    ```{figure} /images/03_workflow_session_maya_ver_select.jpg
    :width: 80%
    :align: center
    ```
    
    <br>

    全て入力を終えたら【Save】を押してください。  
    ```{figure} /images/03_workflow_session_maya_ver_save.jpg
    :width: 80%
    :align: center

    【Save】
    ```

    ```{figure} /images/03_workflow_session_create_yaml.jpg
    :width: 80%
    :align: center
    
    エクスプローラーでcharacterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。  
    ```
    <br>

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
    
    <br>

```{rubric} **既にSessionが作成されている場合**
```

履歴またはfcs_session.yamlファイルからSessionを開いてください。 

<br>

```{rubric} **履歴から開く場合**
```

以前にSessionを起動している場合、File&rarr;Session&rarr;Openの下に履歴が表示されます。  
 - 作業したいデータをクリックします。
```{figure} /images/03_workflow_session_open_log.jpg
:width: 80%
:align: center
```

<br>
<br>


```{rubric} **fcs_session.yamlファイルから開く場合**
```
 - File&rarr;Session&rarr;Open&rarr;Open...  
 OpenSessionウィンドウが開かれたらローカルとネットワークドライブが表示されます。  
 - Characterフォルダ直下にあるfcs_session.yamlファイルを選択し、開いてください。

```{figure} /images/03_workflow_session_open_yaml.jpg
:width: 80%
:align: center
```

<br>

```{warning}
Sessionの新規作成/Open後、続けて別のSession作成や起動は出来ません。  
別のSessionを開きたい場合は、現在のSessionを終了し、FCSの再起動後開きなおしてください。
```

<br>

```{rubric} **「Maya Verの設定」をしても反映されない場合**
```
Session作成時に設定した項目は File&rarr;Session&rarr;info で確認することができます。
```{figure} /images/03_workflow_maya_session_info.jpg
:width: 80%
:align: center
```

<br><br>

New Sessionで設定したMayaVerがinfoで反映されていない場合は、info画面のMaya Versionを右クリックし、Editから変更ができます。
```{figure} /images/03_workflow_maya_info_edit.jpg
:width: 80%
:align: center
```
```{figure} /images/03_workflow_maya_change_maya_ver.jpg
:width: 80%
:align: center
```

<br>

```{attention}
設定の変更後は必ずSaveボタンを押してください
```
