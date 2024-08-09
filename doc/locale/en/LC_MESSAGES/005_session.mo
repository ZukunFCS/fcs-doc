��    "      ,              <     =     R  �  g       �     6   �  �   �  [   �  �   �    �  �   �     g	  "   �	     �	  �   �	  %   �
  .   �
  {   �
     h     �     �     �     �  �   �  �   \  l   �  �   S  �   9     �  S      +   T  @   �  	  �  Z  �     &     ;  �  P     �  �   �  .   �  �   �  ?   A  d   �  �  �  �   �  $   �  -   �     �  �   �     �  .   �  o   �     N     i     ~     �     �  r   �  s   0  W   �  �   �  �   �  !   1  3   S  %   �  5   �    �   ![](images/F004.png) ![](images/F005.png) ![](images/S002.png)   ①Project Folder：FCSの作業データを置きたい場所を指定    ②Actor：モーションキャプチャアクター名    ③Character：3Dモデルのキャラクター名   ④Maya Scene：3DモデルのMayaシーンへのパス   ⑤Maya Base：Assets、workspace.melがあるフォルダへのパス   ⑥Maya Ver：3Dモデルを作成したMayaのバージョンを指定 ![](images/S010.png) .lockファイルは 作業中にほかの人からのアクセスを防ぐためのものです。   正常に終了した際には自動で削除されます。 Create new Sessionで作成されるフォルダ構造 FCSではアクター情報、キャラクター情報、Mayaシーン情報とその解析データを紐づけたファイルのことを「Session」と呼びます。 FCS上でポップアップするウィンドウにはworkspace.melが表示されません FCS起動後、Sessionデータへアクセスするため 「New...（新規作成）」または「Open（開く）」を実行します。 Facial：動画やMayaシーンデータ等素材を保存する場所   　- Assets：Mayaのプロジェクトファイル（Assets以下）を保存する場所   　- RecData：ROM体操やFCSで解析したい動画を保存する場所   　- Scene：アニメーション出力時のデフォルト出力先   　- SetData：アニメーション出力で「audio」を選択した場合にはwavファイルが、   　　「Frame」「Landmark Frame」を選択した場合は連番画像が作成され、保存される NewSessionで設定したMayaVerがinfoで反映されていない場合は、info画面のMayaVersionを右クリックし、Editから変更ができます。 ![](images/S015.png) ![](images/S016.png) Seesionを開く際の注意 Sessionの同時起動について Sessionの新規作成 Sessionの新規作成/Open後、続けて別のSession作成や起動は出来ません。   別のSessionを開きたい場合は、現在のSessionを終了し、FCSの再起動後開きなおしてください。 Session作成もしくはオープン fcs_session.yamlファイルから開く場合 session作成時に設定した項目は File▶Session▶info で確認することができます。 ![](images/S014.png) ①Project Folderの設定 ③Characterの設定 ④MayaSceneの設定 ⑤MayaBaseの設定 ⑥MayaVerの設定 エクスプローラーでActorフォルダ直下に入力したCharacterフォルダが作成されます。 ![](images/F008.png) エクスプローラーでcharacterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。   ![](images/F009.png) エクスプローラーで「Facial」「FCS」のフォルダが作成されます。 ![](images/F003.png) 不正に終了するなどして.lockファイルが残ってしまった場合、   FCSの起動時にポップアップから削除するか、   .lockファイルをエクスプローラーで直接削除してください。 初めにSessionに関わる設定を行うことで、Mayaを別途操作することなくFCS上のボタンでスムーズに作業を開始することができます。 履歴から開く場合 履歴またはfcs_session.yamlファイルからSessionを開いてください。 既にSessionが作成されている場合 設定の変更後は必ずSaveボタンを押してください 赤枠：Project Folderで作成されるフォルダ<br> 青枠：Actorで作成されるフォルダ<br> 緑枠：Characterで作成されるフォルダ<br> .lock/fcs_session.yaml：sessionをSaveした後に作成されるファイル<br> ![](images/folder.jpg) Project-Id-Version: FCS 24.07 Manual
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2024-08-09 15:18+0900
PO-Revision-Date: 2024-07-27 18:48+0900
Last-Translator: 
Language: en
Language-Team: 
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.9.1
 ![](images/F004.png) ![](images/F005.png) ![](images/S002.png)   1. Project Folder: Select the location where you want to save the FCS project data   
 2. Actor: Motion capture actor name   
3. Character: 3D model character name   
 4. Maya Scene: Path to the 3D model Maya scene   
 5. Maya Base: Path to the folder where Assets and workspace.mel are located  
6. Maya Ver: Select the version of the data created in the scene ![](images/S010.png) The .lock file is used to prevent others from accessing the file while you are working on it.   They are automatically deleted when you finish your work properly. Folder structure created by Create new Session In FCS, a file that links actor information, character information, Maya scene information, and analysis data is called a “Session.” “workspace.mel” is not displayed in the popup window in FCS After starting FCS, go to “New…(Create new Session)” or “Open” to access the Session data. Facial: folder to save materials (i.e., HMC videos and Maya scene data)  
 - Assets: folder to save Maya project file (containing assets)  
 - RecData: folder to save the videos you want to analyze with ROM and FCS  
 - Scene: default output destination for animation output  
 - SetData：For animation output, wave files will be saved when you select `audio`. Sequential numbered image files will be created and saved when you select “frame” or `landmark frame'. If the MayaVersion setting in NewSession is not reflected in info, right-click MayaVersion on the info screen and select Edit so that you can edit the details.![](images/S015.png) ![](images/S016.png) Cautions regarding opening a Session How to startup multiple sessions concurrently Creating a new Session  While creating/opening a new Session, you cannot create or start another Session.   To open another session, close the current session, restart FCS, and reopen it. Create or open a Session How to open Session from fcs_session.yaml file You can check the setting details when you create the session under File▶Session▶info. ![](images/S014.png) ①Project Folder settings ③Setting Character ④Setting Maya Scene ⑤Setting Maya Base ⑥Setting Maya Ver The Character folder you entered will be created directly under the Actor folder in Explorer. ![](images/F008.png) fcs_session.yaml (FCS file) will be created directly under the character folder in Explorer.   ![](images/F009.png) Folders for “Facial” and “FCS” will be created in Explorer.![](images/F003.png) If the .lock file remains because of incorrect shut down, etc, please delete the file from the popup when you are starting FCS or delete the file directly in Explorer. By settings details for a Session at the beginning, you can start working with the buttons on FCS without having to operate Maya separately. How to open Session from history  Open Session from history or fcs_session.yaml file. If a Session has already been created Please click the Save button after changing settings. Red: Folders created when setting up a new project<br> Blue: Folders created when setting up a new actor<br> Green: Folders created when setting up a new character<br> .lock/fcs_session.yaml: File create after setting up a new session<br> ![](images/folder.jpg) 