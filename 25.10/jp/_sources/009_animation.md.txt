## アニメーションの出力方法

```{caution}
解析する動画が広角レンズを使って撮影されている場合、Solverの設定変更が必要です。  
詳しくはSolverの詳細設定ページをご確認ください。
```

### 単体のアニメーション出力

#### 出力画面説明

```{figure} images/A001.jpg
:width: 80%
:align: center
```

▼Process

☑ Reprocess：作成したProfile情報を読み取る

```{note}
基本的に ☑ を付けることをオススメします。
```

Upload Options
-  ☑ Animation：アニメーションデータを生成、Mayaに反映
-  ☑ Audio：解析する動画の音声データをMayaに反映
-  ☑ Frames：解析する動画の連番画像を生成、Mayaのイメージプレーン上に反映
-  ☑ Landmark Frames：顔の動きをオートトラッキングする連番画像を生成、Mayaのイメージプレーン上に反映

Export Options
-  ☑ Playblast：出力されたアニメーションをmov形式の動画で出力、保存する
-  ☑ Scene：出力されたMayaシーンを自動で保存する

Start process：アニメーションの出力を開始する

#### 単体のアニメーション出力方法

Videoウィンドウで
 - 解析/出力したい動画名の上で右クリック

画像のメニューが表示されるので
 - ▼Process　を選択
 - 該当する項目に ☑ を入れ

```{figure} images/A002.jpg
:width: 80%
:align: center
```

 - Start process
```{figure} images/A004.jpg
:width: 80%
:align: center
```


```{note}
 - 解析結果を見てから再度調整を行いたい場合はPlayblastやSceneの ☑ を外しておくと時間短縮できます。
```
```{figure} images/A003.jpg
:width: 80%
:align: center
```

 - 初回出力時は時間がかかるため待機
```{figure} images/A005.jpg
:width: 80%
:align: center
```

- Mayaシーン上に ☑ を入れた項目が反映されていく
   - タイムスライダーに音声データ
   - イメージプレーンに連番画像
   - アニメーションデータ の順で反映される
   - アニメーションデータ反映時はスライダーが動く

```{figure} images/image133.jpg
:width: 80%
:align: center
```

```{note}
【playblastやsceneに ☑ していた場合】

出力が完了したらエクスプローラーがポップアップします。
```
```{figure} images/image127.jpg
:width: 80%
:align: center
```
<br>

#### 動画の一部範囲のみを再処理して出力
（FCS 25.04.02～）
```{note}
タイムラインの一部表示機能を使用して、FCSのタイムラインで表示している範囲のみのアニメーションを出力することができます。
```

```{figure} images/Partialprocess_timeline.jpg
:width: 80%
:align: center
```
- FCSのタイムライン範囲をアニメーション出力したい部分に設定

```{figure} images/Partialprocess_rightClick.jpg
:width: 80%
:align: center
```
- FCSのタイムラインの動画名を右クリックして表示されるメニューからのみ実行可能(Videosウィンドウからは実行不可)
- ☑ Partial Process：動画の一部範囲のみ出力、選択項目はアニメーションのみ
- Start processingで処理開始

```{figure} images/Partialprocess_maya.jpg
:width: 80%
:align: center

実行結果
```
<br>

### 複数のアニメーション出力

#### 出力画面説明

```{figure} images/A006.jpg
:width: 80%
:align: center
```
Output Folder：出力先を指定

Output Targets
-  ☑ Animation：アニメーションデータを生成、Mayaに反映
-  ☑ Audio：解析する動画の音声データをMayaに反映
-  ☑ Frames：解析する動画の連番画像を生成、Mayaのイメージプレーン上に反映
-  ☑ Landmark Frames：顔の動きをオートトラッキングする連番画像を生成、Mayaのイメージプレーン上に反映
-  ☑ Playblast：出力されたアニメーションをmov形式の動画で出力、保存する
-  ☑ Scene：出力されたMayaシーンを自動で保存する

Advenced  
-  ☑ Reprocess：作成したProfile情報を読み取る

Output Filename：出力されるデータ名。任意の名前に変更可能

Start：アニメーションの出力を開始する

#### 複数のアニメーション出力方法

Videoウィンドウで

 - 解析/出力したい動画名の左側の ☑ をつける
```{figure} images/A007.jpg
:width: 80%
:align: center
```

 - Processorウインドウを開く
```{figure} images/A008.jpg
:width: 80%
:align: center
```
<br>

```{figure} images/P37_processorWindow.jpg
:width: 80%
:align: center
```

 - 該当する項目に ☑ を入れ
 - Output Filename を任意の名前に変更
```{note}
- {solver} → solverの名前
- {video} → ビデオのファイル名
- {user} → windows ユーザ名
- {project} → 案件フォルダ名
- {chara} → キャラクター名
- {actor} → 役者名
- {%Y%m%d}, {%H%M%S} → 年月日、時間分秒

{video}のみにするとimportした動画名で出力される
```
 - Start
```{figure} images/A009.jpg
:width: 80%
:align: center
```

出力が完了したらエクスプローラーがポップアップします。
```{figure} images/image136.jpg
:width: 80%
:align: center
```
<br>

### カメラ・イメージプレーンについて
Frames、またはLM Framesにチェックを入れた場合、Maya内のイメージプレーンに連番画像がセットされます。  
連番画像をセットしたいカメラ・イメージプレーンの名前を「Settings/Maya/Camera」「Settings/Maya/ImagePlane」から設定してください。

デフォルトの設定は以下の通りです。

- イメージプレーン → imagePlane1
- カメラ → fcs_cam1

指定した名前のカメラ・イメージプレーンがシーン内に無い場合は新しく作成されます。  
パイプラインに合わせてカメラの名前を随時設定してください。
