# Menu
ここではFCSの各メニュー項目について説明します。

<img width="386" height="29" alt="image" src="https://github.com/user-attachments/assets/853c25f2-ec90-4ca9-9886-5c786e96172c" />

## File
Session(セッション)ファイルに関連したメニューです。<BR>
セッションを開く、設定の変更、新規セッションの作成などを実行することができます。

<img width="381" height="196" alt="image" src="https://github.com/user-attachments/assets/38d2e654-a72b-4c2a-84a0-b06022bc4a6a" />


### Session ▶
#### New…
セッションを新規で作成します。Create new Sessionウィンドウを開きます。

![CreateNewSession](https://github.com/user-attachments/assets/0aa461c3-0db5-4335-85a0-d930d7da465e)

##### Create new Sessionウィンドウ

| 項目 | ボタン |説明| 
|:-------------:|:--------------:|:--------------|
|Project Folder||FCSの作業データを置きたい場所（Root）のパス入力欄|
||Browse...|ダイアログを開いてプロジェクトフォルダの作成先を入力します。|
||Create|FCSのプロジェクトフォルダを作成します。|
|Actor||解析する動画のアクター（演技者）名入力欄<BR>既に該当アクターのフォルダが存在する場合、プルダウンから選択できます。|
||+|「Create new actor」ウィンドウを起動して、アクター名のフォルダを作成します。<BR>アクター名はプルダウンに追加されます。|
|Character||3Dモデルのキャラクター名入力欄|
||+|「Create new character folder」ウィンドウを起動して、キャラクター名のフォルダを作成します。<BR>キャラクター名はプルダウンに追加されます。|
|Maya Scene||3DモデルのMayaシーンのパス入力欄|
||Browse...|ダイアログを開いてパスを入力します。|
|Maya Base||「workspace.mel」があるフォルダのパス入力欄|
||Browse...|ダイアログを開いてパスを入力します。|
|Maya Ver||3Dモデルに対応するMayaのバージョン入力欄|
||▼|2018 - 2026の範囲のバージョンを選択できます。|
|Save||入力した内容で新規Session(セッション)を作成します。|
||Save|characterフォルダ直下にfcs_session.yaml(FCSファイル)が作成されます。<BR>現在開いているセッションを閉じ、新しいセッションを開きます。<BR>FCSの再起動が完了するまでしばらくお待ちください。|

##### Create new Sessionで作成されるフォルダ構造  

| 色 | 内容 | 
|:-------------:|:--------------:|
|赤枠|Project Folderで作成されるフォルダ|
|青枠|Actorで作成されるフォルダ|
|緑枠|Characterで作成されるフォルダ|

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/26da13c1-8cbf-46f3-856a-5975adeb040d" />

| フォルダ | 子フォルダ | 説明 | 
|:-------------:|:--------------:|:--------------|
| Facial |       | 動画やMayaシーンデータ等の素材を保存するフォルダ|
|     | Assets  |モデル・テクスチャなど、Mayaのプロジェクトファイル(Assets以下)を保存するフォルダ |
|     | RecData | ROM動画やFCSで解析・出力したい動画を保存するフォルダ |
|     | Scene   |  FCSでアニメーションを出力する際のMayaシーンのデフォルト出力先|
|     | SetData | FCSでアニメーションを出力する際のwavファイルや連番画像の出力先|
| FCS |          | Project Folderで作成したフォルダ<BR>解析に使用するデータが保存されるプロジェクトフォルダ|
|     | Actor    | Actorで作成したフォルダ<BR>Actorで入力した名前がフォルダ名になる   |
|     | Character| Characterで作成したフォルダ<BR>Characterで入力した名前がフォルダ名になる |
|     | RetargetData（IMG/PARAM）| 作成したProfileの編集データ（画像や数値情報）が保存されるフォルダ|
|     | VideoData| 解析する動画のキャッシュファイルが保存されるフォルダ |
|     | VideoData \ .lock      | 作業の競合を防ぐためのロックファイル<BR>セッションの起動・終了時に、自動で作成・消去される|
|     | VideoData \ fcs_session.yaml      | セッション情報を保存しているファイル |

```{note}
エクスプローラーからフォルダ名を直接変更してしまうと、FCSは各フォルダ内のデータをうまく取得できません。<BR>
フォルダ名を変更したい場合、File＞Session▶＞Info…から各項目の設定を変更してください。入力確定後、フォルダ名は自動的に変更されます。
```
<BR>

#### Open▶
##### Open…
ダイアログから.yamlファイルを選択してセッションを開きます。
##### [パス]
最近使用したセッションのパスが表示されます。

<BR>

#### Info
Session Dataウィンドウが開きます。
<img width="1151" height="478" alt="image" src="https://github.com/user-attachments/assets/d30863da-b3c2-4971-8b30-108ca4043546" />
##### Session Dataウィンドウ
右クリックメニューから内容のコピーや編集を行うことができます。

| 項目 | 説明 | 右クリックメニュー| 
|:-------------:|:--------------|:--------------|
|Project Folder|プロジェクトフォルダのパス|パスのコピー|
|Actor|アクター名|リネーム・コピー|
|Character|キャラクター名|リネーム・コピー |
|Maya Scene|Mayaシーンパス| パスのコピー・変更|
|Maya Base|workspace.melのパス| パスのコピー・変更|
|Maya version| Mayaバージョン|コピー・変更|
|Profile Count|セッション内のプロファイルの数|コピー|
|Video Count|セッションにインポートした動画の数 | コピー|
|Created at| セッション作成日時| コピー|
|Created by| セッション作成者| コピー|
|Last saved at| 最終保存日時| コピー|
|Last saved by| 最終保存者| コピー|

<BR>

#### Save ▶
<!--
##### Session\
*セッションを保存するとは?*保存される内容が特にないため削除したいが渡すバージョンにはあるため記述25/11/11
-->
##### Session
セッションデータを保存します。随時操作の度に保存されているため基本的には使用しません。

##### Profiles
Editウィンドウのプロファイルを保存します。

##### Controller
コントローラーウィンドウの表を保存します。

<BR>

#### Export
Export Sessionウィンドウが開きます。
<img width="795" height="322" alt="image" src="https://github.com/user-attachments/assets/00fb49e7-d1f5-47d7-9478-7120e0ddf660" />
##### Export Sessionウィンドウ
| 項目 |プルダウン内容| 説明 | 
|:-------------:|:--------------:|:--------------|
|Project Folder||エクスポート先のプロジェクトフォルダパス入力欄（フルパスで指定）|
|Actor||エクスポート後のアクター名入力欄|
|Character||エクスポート後のキャラクター名入力欄|
|Profile ☑||プロファイルを含めて出力するかどうかを指定|
|Videos|▼|出力先に動画ファイルをコピーするかを指定|
||No video|動画データをコピーしない|
||Associated video|関連する動画のみコピー|
||All files|Recdata内のすべての動画データをコピー|
|Facial/Assets Folder ☑||出力先にFacial/Assets以下のフォルダー・ファイルをコピーするかを指定|

```{note}
Project Folderの項目ではエクスポート先のプロジェクトフォルダのパスを指定します。
このときプロジェクトフォルダ以下のフォルダ構造が存在しない場合は新しくフォルダが作成されるので、
例えばE:\test\FCS\testActor\testCharacterと同じ階層にtestCharacter2をエクスポートしたい場合には
Project Folderの項目に「E:\test」を指定し、Characterの項目に「testCharacter2」と入れてください。
```
<BR><BR>

### Settings
FCS全般の設定メニューです。
#### ▼ UI
<img width="781" height="458" alt="image" src="https://github.com/user-attachments/assets/4654b5ab-ff4e-4148-9caf-66d6e3059fd2" />

##### Settings > UI

|対象| 項目 |デフォルト| 説明 |
|:--------------|:--------------|:--------------:|:--------------|
|Global|Font Size|25|文字の大きさ|
||Language|en|言語設定|
|Gallery|Thumbnail width|200|ギャラリーに表示されるプロファイル画像の横幅|
||Default Cols|3|ギャラリーのデフォルトの列数|
|Video Player|Cache Frame Max|2000|メモリにキャッシュするフレームの最大値|
||Default Tags||デフォルトで付与するタグ名|
|Video Library| Skip rotation prompt|☐|Videoインポートで回転処理の設定画面を表示するかどうか|
||Default Rotation|0|Videoインポートの際のデフォルトの回転値（0で回転しない）|

```{note}
Cache Frame Maxは数値を上げるほど多くのメモリ容量を消費します。<BR>
FullHDサイズだと10000fごとに約64GB使用される目安です。<BR>
-1を指定すると無制限にキャッシュを保存します。この設定は十分なメモリがある場合のみ使用してください。
```
#### ▼Output
<img width="1091" height="421" alt="image" src="https://github.com/user-attachments/assets/0618dda2-88c4-4a0f-85ea-7c88bef60d93" />

##### Settings > Output

|対象| 項目 |デフォルト| 説明 |
|:--------------|:--------------|:--------------:|:--------------|
|Default output options|Default Folder|Facial/Scenes/_Outputs/<BR>%Y%m%d_%H%M%S_{user}|デフォルトの出力先フォルダ|
||Default Filename|{video}|デフォルトのファイル名||
||Default Filename (Batch)|{video}|バッチ出力時のデフォルトファイル名||
||Default Maya scene format|.mb|デフォルトのMaya保存形式||
|Playblast|Encoder|H.265/HEVC|プレイブラストのエンコード設定|
||Width|1920|プレイブラストの横幅|
||Height|1080|プレイブラストの立幅|
||Quality|100|プレイブラストの画質|
||Percent|100|プレイブラストの解像度|

#### ▼Keyboard Shortcuts
同時押しはキー1種+修飾キー2種の3ボタンまで登録可能です。

<img width="928" height="668" alt="image" src="https://github.com/user-attachments/assets/4374192f-be47-4b9f-a8e2-b00092e35d1e" />

##### Settings > Keyboard Shortcuts
|対象|項目 | デフォルト |説明|
|:--------------|:--------------|:--------------:|:--------------|
|・Timeline|Next Frame|.+Alt|次のフレームへ|
||Previous Frame|,+Alt|前のフレームへ|
||Next ROM|.|次のプロファイルへ|
||Previous ROM|,|前のプロファイルへ|
||Play / Pause Timeline|v+Alt|タイムラインの再生 / 一時停止|
||Add current frame to ROM|Q|現在のフレームをプロファイルとして追加|
||Open profile on timeline|E|*タイムラインのプロファイルを開く*確認|
|・Editor|Save ROM edits|S+Ctrl|プロファイルの保存|
||From Maya|V+Ctrl|表情の値をMayaから読み込み|
||To Maya|C+Ctrl|表情の値をMayaへ送信|
|・Layout|Active Pickup|1+Ctrl|Pickupのプリセットレイアウトに変更|
||Active Process|2+Ctrl|Processのプリセットレイアウトに変更|
||Active Register|3+Ctrl|Registerのプリセットレイアウトに変更|
||Active Retarget|4+Ctrl|Retargetのプリセットレイアウトに変更|

#### ▼Maya
<img width="938" height="280" alt="image" src="https://github.com/user-attachments/assets/f96e06e8-7fb1-4828-a06d-e62b1b09318c" />

##### Settings > Maya
|項目| デフォルト |説明|再起動不要|
|:--------------|:--------------:|:--------------|:--------------:|
|CommandPort|42069|Mayaとの接続に使用するコマンドポート||
|SliderSyncPort|42070|Mayaのタイムラインを取得するコマンドポート||
|Open maya scene at launch|☑|Launch Maya時に登録したMayaシーンも開く|〇|
|Use gallery character preview|☑|ギャラリーウィンドウのキャラクター表示切替機能を使用する|〇|
|Image Plane|imagePlane|イメージプレーン名|〇|
|Camera|fcs_cam|カメラ名|〇|
|Install path|C:/Program Files/Autodesk/|Mayaのインストール先|〇|

#### ▼Misc
<img width="783" height="178" alt="image" src="https://github.com/user-attachments/assets/0bd70e1e-8fba-4116-962f-8fba63743aab" />

#### Settings > Misc
|項目| デフォルト |説明|
|:--------------|:--------------:|:--------------|
|Keep max N video in memory|1|*確認*|
|Backend|cpu|データの処理方法|
|Update Channel|Patch|アップデート通知設定|
||All|メジャーバージョンアップ・マイナーバージョンアップ両方のアップデート通知を受け取る|
||Patch|マイナーバージョンアップ通知のみ受け取る|
||None|バージョンアップ通知を受け取らない|
|Use Beta|☐|ベータ版機能を使用する|

#### Save

設定を保存します。設定は基本的にFCSを再起動することで反映されます。

#### Restore　

設定をデフォルトに戻し、FCSを再起動します。

#### Import　
他のバージョンなどから設定をインポートします。C:\Users\[ユーザー名]\.fcs\Cortado\[FCSバージョン]にあるmy_conf.yamlを読み込んでください。

<BR><BR>

### Quit

FCSを終了します。「.Lockファイル」を削除します。UI設定なども

<BR><BR><BR>

## Window
ウィンドウを表示するメニューです。ここでは各ウィンドウの説明を行います。

### Videos
Videosウィンドウが開きます。<BR>
Videosウィンドウでは読み込んだHMC動画を一覧で表示します。読み込んだ動画に対しての処理も右クリックから可能です。

![videos](https://github.com/user-attachments/assets/9efd43b0-5951-4b55-9050-0449e1ee2d33)

|| 項目 |説明|
|:--------------|:--------------:|:--------------|
①|Filter入力欄|動画名を文字列でフィルターします。|
②|Importボタン|ダイアログを開いて新しい動画をインポートします。シフトキーで複数選択が可能です。|
③|Video表見出し|右クリックメニューから表示する内容を変更することができます。|
④|選択ON/OFF|バッチ処理の対象にするかどうか切り替えます。|
⑤|動画名|動画名を右クリックでメニューが表示されます。メニューから単体のアニメーション出力などを行うことができます。|
⑥|選択ON/OFF(全)|Videosウィンドウのすべての動画に対して選択のON/OFFを切り替えます。|
⑦|Removeボタン|Remove Videos and Sequencesウィンドウを表示します。|

#### Videos 右クリックメニュー
<img width="207" height="183" alt="image" src="https://github.com/user-attachments/assets/f8394235-8334-430d-b575-39d0daf818f0" />

|項目|説明|
|:--------------:|:--------------|
|動画名||
|Open| 動画を開く（PlayerとTimelineに表示されます）|
|Remove|Remove Videos and Sequencesウィンドウを表示します。|

<img width="612" height="280" alt="image" src="https://github.com/user-attachments/assets/b97ca6a0-5d4b-4727-942a-48eefe0da38e" />

##### Remove Videos and Sequencesウィンドウ
オプションを指定して動画をFCSから削除します。

|項目| プルダウン |説明|
|:--------------|:--------------:|:--------------|
|Video||動画名|
|Delete caches option：||キャッシュデータについて|
|☑ SetData||セットデータ内のファイル（音声・静止画連番）も削除するかどうか|
|☑ Tracking Sequence||動画のトラッキングデータも削除するかどうか|
|Profiles|▼|削除対象の動画から追加したプロファイルについて|
||Keep|プロファイルはそのまま維持します|
||Keep but unlink|プロファイルは維持しますが、動画との関連付けは削除します*確認*|
||Delete|すべて削除します|
|Execute||実行|
|Cancel||キャンセル|

##### ▼Process
![Process](https://github.com/user-attachments/assets/03c9170b-9c75-4ede-896a-6c109dd82f47)

||項目|説明|
|:--------------:|:--------------|:--------------|
||☑ Reprocess|キャッシュが既に存在する場合も一から解析します|
Sequence Options|Sequence Name|シーケンスの名前を設定します|
Upload Options|☑ Animation|アニメーションデータを出力します|
||☑ Audio|音声データをMayaに読み込みます|
||☑ Frames|動画の連番画像を出力、Mayaのイメージプレーンに読み込みます|
||☑ LM Frames|ランドマーク付の連番画像を生成、Mayaのイメージプレーンに読み込みます（+パイプラインでは使用不可）|
Export Options|☑ Playblast|プレイブラストをmov形式の動画で出力、保存します|
||☑ Scene|Mayaシーンを出力、保存します|
||Start processing|上記の設定で処理を実行します|

##### Copy
<img width="206" height="141" alt="image" src="https://github.com/user-attachments/assets/27c39e0a-c523-454d-91db-fdf57206003e" />

|項目|説明|
|:--------------|:--------------|
Filename|動画のファイル名をクリップボードにコピーします|
Full path|動画のフルパスをクリップボードにコピーします|
Parent|動画の親ディレクトリのパスをクリップボードにコピーします|

<BR>

### Processer
Processerウィンドウが開きます。<BR>
Processerウィンドウでは複数の動画を一括で処理するバッチ機能が使用できます。VideosウィンドウでチェックボックスがONになっている動画が処理の対象になります。

![Processer](https://github.com/user-attachments/assets/725a26ec-501c-4c05-b730-a8583014b603)


||項目|説明|
|:--------------:|:--------------|:--------------|
|①|Output Folder|出力先を指定します|
|②|Output Targets|出力する内容を指定します|
||☑ Animation|アニメーションデータを出力する|
||☑ Audio|音声データをMayaに読み込む|
||☑ Frames|動画の連番画像を出力、Mayaのイメージプレーンに読み込む|
||☑ Landmark Frames|ランドマーク付の連番画像を生成、Mayaのイメージプレーンに読み込む（+パイプラインでは使用不可）|
||☑ Playblast|プレイブラストをmov形式の動画で出力、保存する|
||☑ Scene|Mayaシーンを保存する|
||Format|出力するMayaの保存形式(.mb / .ma)|
||☑ Distribute|配布用YAMLファイルを出力する？、出力ファイル名|
|③|Advanced||詳細な設定を行います|
||☑ Reprocess|キャッシュが既に存在する場合も一から解析する|
||Output Filename|出力されるデータ名|
|④|Start|アニメーションの出力を開始する|
|⑤|プログレスバー|処理状況の表示をします|
|⑥|Log|処理状況のログが表示されます|

##### フォルダ名・動画名を指定するパラメータについて
|項目|説明|
|:--------------:|:--------------|
|{solver}|solverの名前|
|{video}|ビデオのファイル名|
|{user}|windowsユーザ名|
|{project}|案件フォルダ名|
|{chara}|キャラクター名|
|{actor}|役者名|
|{%Y%m%d}|年 月 日|
|{%H%M%S}|時間 分 秒|

```{note}
%Y%m%d_%H%M%S_{user}では「年月日_時間分秒_ユーザー名」が、{video}のみにすると動画名単体が指定されます。
```

<BR>

### Controller
コントローラーの登録を行うためのウィンドウです。

<img height="668" alt="image" src=https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_controller01.png>


##### Controllerウィンドウ

|項目|内容|説明|
|:--------------:|:--------------|:--------------|
|Filter||入力したコントローラー名でコントローラー表にフィルターをかけます。|
|all▼|all / null / upper / lower / gaze / eyelid |指定した項目（Region）を絞り込んで表示します。|
|save||コントローラー設定を登録・保存します。|


|　|項目|説明|
|:--------------|:--------------:|:--------------|
|Maya|Add selected|選択したコントローラーを登録します。|
||☑ Sync|表の数値の操作をMayaと同期させます。|
|▼Value|▼Min / Max / Default|☑ を入れたコントローラーのどの値に対しての処理か指定します。|
||0.000|入力する数値|
||Apply|実行ボタン|
|▼Region|Upper / Lower / Gaze / Eyelid|☑ を入れたコントローラーのRegionを設定します。|
||Remove|☑ を入れたコントローラーを表から削除します。|
||Select All/Unselect All|controller上に表示されているコントローラーすべての ☑ / □ を切り替えます。|
|▼Advanced|Remove empty|Regionが登録されていないコントローラー(null)を表から削除します。|
||Delete all|登録したコントローラー情報をすべて削除します。|
||Reset|以前Saveした際のデータの状態に戻します。|
||Rearrange|コントローラー表の順番をドラッグ＆ドロップで変更できるようにします。|


```{note}
プルダウンメニューについて：
- Region名 … 現在登録しているRegionのコントローラーが表示されます。プルダウンがRegionの状態でAdd Selectedを押すと、コントローラーをそのRegionに設定された状態で読み込むことができます。
- all … すべてのRegionのコントローラーが表示されます。allの状態でコントローラーを読み込むとRegionにはnull(リージョン未設定)が設定されます。
- null … リージョンが設定されていないコントローラーが表示されます。
コントローラー表に一つでもnullがあると登録したコントローラーを保存できないため、Save前にリージョンがnullになっているコントローラーがないか確認してください。
```
```{note}
最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい。
```
```{Warning}
数値ではない(True/False)アトリビュートがあると正常に動作しないため、登録から除外してください。
```

### Profiles
#### Gallery
プロファイルの一覧が表示されるウィンドウです。

<img alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_gallery01.png">

| 項目 |プルダウン内容| 説明 | 
|:-------------:|:--------------:|:--------------|
|Count||現在表示されているプロファイル数を表示します。|
|[  ]|▼|フィルターをかけます。|
||Enabled|Enabled状態のプロファイルを表示します。|
||Disabled|Disabled状態のプロファイルを表示します。|
||Default|数値未設定含む、すべてのRegionがデフォルトの値のプロファイルを表示します。|
||Not Default|デフォルトの値ではないプロファイルを表示します。|
||Neutral|ニュートラルのプロファイルを表示します。|
||No Tags|タグのついていないプロファイルを表示します。|
||[Region名] Enabled|そのRegionに値が登録されているプロファイルを表示します。|
|Sync timeline||選択したプロファイルが含まれる動画を開いている場合、そのプロファイルのフレームに移動します。|
|Adbanced||詳細機能を表示します。（今授業では使用しません）|

####  Misc
|項目| デフォルト |説明|
|:--------------|:--------------:|:--------------|
|Hide Tooltip|□|登録されているRegionの図の表示 / 非表示を切り替えます。|
|Display Mode|Image|プロファイルをアクターの写真で表示します。|
||Render|プロファイルをキャラクターモデルのスクリーンショットで表示します。|
|Refresh Renders||Display Mode＞Render表示用にスクリーンショットを現在のMayaの設定で再出力します。|

#### Editor
プロファイルを登録するウィンドウです。<BR>
画像に対応する表情をMayaで作成し、FCSに読み込みます。

<img height="668" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor01.png">

##### Editorウィンドウ

|項目|内容|説明|
|:--------------|:--------------:|:--------------|
|No Sync▼||数値の操作をMayaと同期させるかどうかの設定です。|
||To Maya|FCSのスライダー上でのプロファイルの数値変更をMayaに転送します。|
||From Maya|saveボタンを押す際にMaya上での表情データを取得しFCSに反映させてから登録します。|
||Both|「To Maya」と「From Maya」をどちらも行い、FCSとMayaを双方向で同期させます。|
||No Sync|FCSとMayaを同期させません。|
|Neutral||Neutral表情かどうかを設定します。|
|Enabled||このプロファイルを表情推定の計算に含めるかどうか設定します。|
|Controller▼||プロファイル画像右のスライダー表記を切り替えます。|
||controller|スライダーにコントローラー名を表示します。|
||Value|スライダーに値を表示します。|
|Name||プロファイル名を表示します。任意の名前に変更することも可能です。|
|save||現在の設定でプロファイルを登録・保存します。|

```{note}
コントローラーウィンドウ右部のスライダーはCtrl＋クリックで直接数値を入力することが可能です。
```

##### Region
|Region|Utils|Filter|Reset|Tracking|Tags|Info|
|:--------------|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------|
|<img width="206" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor10.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor04.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor05.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor06.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor07.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor08.png">|<img width="200" alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Profiles_Editor09.png">|

||項目|デフォルト|説明|
|:--------------|:--------------:|:--------------:|:--------------|
|Region▶|Upper/ Lower / Gaze / Eyelid|☑|このプロファイルにどのRegionの表情が含まれるか指定します。|
|Utils▶|To Maya||FCSのプロファイルの値をMayaのコントローラーに送信します。|
||From Maya||Mayaのコントローラーの値をFCSのプロファイルに送信します。|
||Predict||プレディクト機能でプロファイルの表情を推定します。|
||LM|□|顔のランドマークを表示します。デフォルトのパイプラインでは使用しません。|
||Image|☑|プロファイルの画像を表示します。|
|Filter▶|Upper/ Lower / Gaze / Eyelid / all |all|対応するRegionのコントローラーのみ表示します。|
|Reset▶|Upper/ Lower / Gaze / Eyelid / all||対応するコントローラーの値を0にリセットします。|
|Tracking▶|||この機能は今授業では使用しません。|
|Tags▶|||プロファイルにタグを追加します。|
|Info▶|Video/Frame/Time/Create/Create||各情報を表示します。|

<!--
|Tracking▶|Edit in Maya||今授業では使用しません。|
||Save Edited||*確認*|
-->

### Solver
アニメーション出力についての設定を行うウィンドウです。
基本的にはデフォルトの設定のまま使用します。

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Solver01.png">

|対象|項目| デフォルト |説明|
|:--------------|:--------------:|:--------------:|:--------------|
|▼Global|Fisheye|☑||
||Processing Pipeline|RP＋|動画を処理するためのパイプラインを指定します。|
|▼Denoising|Type|Smoothing|スムージング機能の設定を行います。|
||Weight|-2|スムージングの強さ|
||Reps|5|スムージングの回数|
|▼Denoising Preview|Raw|☑|スムージングをかけた後のカーブの形状を推測します。|
||Raw / Denoising|☑|スムージング前 / スムージング後|
|Save current denoising profile|||現在のスムージング設定をプリセットとして保存します。|
|▼Post processing|Gaze Freezing|☐|今授業では使用しません。|
||Prioritize profile|☐|プロファイルのあるフレームでプロファイル表情を100％使用します。|
||Clamp mode|Hard Clamp|アニメーションカーブにクランプをかけます。|
|Train|||Solverの計算を実行します。通常はアニメーション出力の際に自動で計算されるため、このボタンを敢えて押す必要はありません。|
|Delete cache|||キャッシュを削除します。今授業では使用しません。|

### Log
ログが表示されます。
最新のログは常にFCS上部に表示されるため、普段はあまり使用しません。

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Log01.png">

|項目|説明|
|:--------------:|:--------------|
|INFO|インフォメーションログを表示します。|
|WARNING|警告ログを表示します。|
|ERROR|エラーログを表示します。|

<BR>
```{note}
以下のウィンドウは初めから表示されており、メニューの中に含まれません。
```
<BR>

### Player
現在開いている動画を表示します。

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_player01.png">

### Timeline
タイムラインの操作を行います。

![timeline](https://github.com/user-attachments/assets/62133ecb-7d53-4850-b039-9b2eef91c878)


||項目|説明|
|:--------------:|:--------------:|:--------------|
|①|[0]/[3933]|　動画の再生範囲を変更します。|
|②|[106]|現在のフレームを表示します。|
|③| \|<  / >\| |1フレーム前 / 後に移動します。|
|④|<<  / >>|　次のプロファイルにジャンプします。|
|⑤|＞ / \|\| |　動画の再生 / 停止（再生すると一時停止ボタンが、一時停止すると再生ボタンが表示されます）|
|⑥|Video|動画名が表示されます（Videosウィンドウと同じ右クリックメニューが使用可能です）|
|⑦|Profile|現在タイムライン上でカーソルを乗せているプロファイルの名前が表示されます。|


##### タイムライン右クリックメニュー（Playback Settings）
<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Timeline002.png">

|項目|説明|
|:--------------:|:--------------|
|Snap|タイムラインをドラッグした際にプロファイルにスナップします。|
|Loop|タイムラインをループ再生します。|
|Mute|タイムライン再生時に音声をミュートします。|

##### ▼Resolution

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Timeline003.png">

|項目|説明|
|:--------------:|:--------------|
|1 : 1 - 1 : 8|表示している動画の解像度を変更します。|

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Timeline004.png">

##### ▼Sync
|項目|説明|
|:--------------:|:--------------|
|No Sync|タイムラインをMayaと同期しません。|
|To Maya|FCSのタイムラインの値をMayaのタイムスライダーへ送信します。|
|From Maya|Mayaのタイムスライダーの値をFCSのタイムラインへ送信します。　※要プラグイン|
|Both|FCSとMayaのタイムラインを相互に同期します。　※要プラグイン|

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Timeline005.png">
▼Speed

|項目|説明|
|:--------------:|:--------------|
|Every Frame|すべてのフレームを再生|
|Real Time|リアルタイム再生|

<BR><BR><BR>

## Maya
<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Maya001.png">

|項目||説明|
|:--------------:|:--------------:|:--------------|
|Status||Mayaとの接続状況を確認、クリックで接続をテストします。|
|Open Scene||セッションに登録しているMayaシーンを開きます。|
|Launch▶|2018 - 2026|セッションに登録しているバージョンのMayaを新規で開きます。<br>SettingsでOpen maya scene at launchをONにしている場合、Mayaシーンも開きます。|
|GenerateMesh for Tracking Edits||今授業では使用しません。|

<BR><BR><BR>

## View
<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_View001.png">

|項目|説明|
|:--------------:|:--------------|
|☑ Fullscreen|全画面表示|
|☑ VSync|垂直同期を設定します。基本的にはONにしてください。|
|Scale|UI表示の拡大率を変更します。|
|☑ Always on Top|FCSを常に最前面に表示します。|
|Layout▶|プリセットのレイアウトに切り替えます。プリセットは以下の通りです。|

<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_View002.png">

|項目||説明|
|:--------------:|:--------------:|:--------------|
|Pickup||Pickupレイアウトに切り替える|
|Process||Processレイアウトに切り替える|
|Register||Registerレイアウトに切り替える|
|Retarget||Retargetレイアウトに切り替える|
|sample_Layout(Layout名)▶|Apply|保存したレイアウトに変更する|
||Delete|保存したレイアウトを削除する|
|Save current||現在のレイアウトに名前を付けて保存する|

#### Pickup
<img width="1786" height="919" alt="image" src="https://github.com/user-attachments/assets/cd138494-a757-4688-b97a-200810df2ec8" />

#### Process
<img width="1786" height="919" alt="image" src="https://github.com/user-attachments/assets/7bc3f3b4-71e5-40df-b63e-5fd9b34798fa" />

#### Register
<img width="1786" height="919" alt="image" src="https://github.com/user-attachments/assets/77d12052-452f-4ec3-8797-5ae233939d9e" />

#### Retarget
<img width="1786" height="919" alt="image" src="https://github.com/user-attachments/assets/c45d77d0-e955-4205-9313-6df3403f7839" />


<BR><BR><BR>

## Explore
Windowsエクスプローラーを開きます。

<img alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Explorer001.png">

|項目|説明|
|:--------------:|:--------------|
|Project|プロジェクトフォルダを開きます。|
|FCS|FCSフォルダを開きます。|
|Facial|Facialフォルダを開きます。|
|tmp|Logなどが格納されているユーザー設定フォルダを開きます。|

<img alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Explorer002.png">

### FCS
||項目|説明|
|:--------------|:--------------:|:--------------|
|FCS▶|Actor|Actorフォルダを開きます。|
||Character|Characterフォルダを開きます。|
||Retarget Folder|RetargetDataフォルダを開きます。|
||Video Data|VideoDataフォルダを開きます。|

### Facial
<img alt="image" src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Explorer003.png">

||項目|説明|
|:--------------|:--------------:|:--------------|
|Facial▶|Actor|Facialフォルダを開きます。|
||Assets|workspaceフォルダを開きます。|
||RecData|RecDataフォルダを開きます。|
||Scenes|Scenesフォルダを開きます。|
||SetData|SetDataフォルダを開きます。|
||Output Scene|_Outputsフォルダを開きます。|


<BR><BR><BR>

## Info
<img  src="https://github.com/ZukunFCS/fcs-doc/blob/main/doc/images/FCSMenu_Info001.png">

|項目|説明|
|:--------------:|:--------------|
|License|ライセンスの管理|
|About|FCSについて|
|Help|FCSマニュアルの表示|
|3rd party licenses|サードパーティーライセンスについて|

<BR><BR><BR>
