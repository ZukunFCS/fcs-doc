## Profileの作成

### Profileの作成の前に...

#### 解析動画を開く方法

Window&rarr;VideosでVideosウィンドウが開きます。  
Videosウィンドウでは解析したい動画を開いたり、インポートすることができます。
```{figure} images/P26_VideosWindow.jpg
:width: 80%
:align: center

Windows&rarr;Videos
```

```{figure} images/P002.jpg
:width: 80%
:align: center

Import
```

ウィンドウがポップアップされるので  

```{figure} images/P003.jpg
:width: 80%
:align: center

解析したい動画をクリックし開く
```

```{note}
Shift+クリックで複数同時にimportできます。
```


```{figure} images/P004.jpg
:width: 80%
:align: center

Videosウィンドウに解析したい動画が表示されます。
```

#### Timelineの画面説明

```{figure} images/P019.jpg
:width: 80%
:align: center
```
- Timeline：バーを左右に動かし、ビデオを手動で再生させる
- [0][20130]：ビデオの縮尺を変更できる。
- [7967]：現在のフレーム数
- |< >|：1フレーム前/後に移動する
- << >>：登録したprofileにジャンプする
- ＞ ||：動画の再生 - 停止（再生すると一時停止ボタンが表示される）
- 1:2▼：表示する動画の解像度を変更する（Scaleが小さくなるほどプレビューが鮮明に、大きくなるほど荒くなる）
- Sync：☑ でTimeline操作状況をMayaのTimeSliderと一致させる
- EveryFrame/Realtime：再生速度を変更する
- Video：Video playerに表示されている動画名

#### Editorの画面説明

```{figure} images/P007.jpg
:width: 80%
:align: center
```
Sync:
- To Maya：登録されているprofile情報をMayaに転送する
- From Maya at save：saveする際にMaya上での調整データを取得しFCSに反映する
- Both：FCSとMayaを双方向で連動させる
- No Sync：FCSとMayaを連動させない

```{note}
本ページではProfileの追加手順 - 編集手順について記載しております  
Mayaをベースに表情を調整するのか、FCSをベースに表情を調整するのかは任意で使い分けることができますが、  
最初は「Both」での使用をオススメします。
```

- Neutral：デフォルトの表情として必ず1つ登録する
- Enabled：解析する素材として使用する

Controller▼
- Controller：コントローラー表示が名前になる
- Value：コントローラー表示が数字になる 

▼Region
- Upper/Eyelid/Gaze/Lower：調整した情報を登録する  

▼Utils
- To Maya：FCS上で操作した値をMayaへ送る
- From Maya：Mayaで操作した値をFCSへ送る
- Predict：画像から表情を解析し、Mayaの3Dモデルに反映する機能

LM：LandMarkを表示する  

▼Filter
- ▼all/Upper/Eyelid/Gaze/Lower：選択した項目でコントローラーを絞り込む
- [ ]：入力した文字でコントローラーを絞り込む  

▼Reset：入力した情報を削除する
- Name：Profileとして登録する名前
- Save：変更した情報を保存する
- 画像部分：Timelineから+で追加した画像が表示される
- コントローラー：Controller Infoで登録したコントローラーが表示される

#### Galleryの画面説明

```{figure} images/P008.jpg
:width: 80%
:align: center
```
作成したProfileが表示されるウィンドウ

&larr;&rarr;：1列に表示するprofileの数を変更する。◀を押すと少なく、&rarr;を押すと多くなる。最小3、最大10。
Count:○○：登録しているprofileの総数

All&darr;：該当する項目を絞り込む
- All：すべてのprofileを表示する
- Enabled：解析に使用するprofileを表示する。Enabledに ☑ を入れて登録したprofileが対象となる。
- Disabled：解析に使用しないprofileを表示する。Enabledに ☑ を入れずに登録したprofileが対象となる。
- Default：数値がdefaultのprofileを表示する。
- Not Default：数値がdefaultではないprofileを表示する。
- Neutral：Neutralにチェックを入れて登録したprofileを表示する。
- （Region）Enabled：該当する（Region）に ☑ を入れて登録したprofileを表示する。
- （Region）Disabled：該当する（Region）に ☑ を入れず登録したprofileを表示する。

Sync timeline ☑ ：登録したprofileと同じ動画を開いた状態でprofileを選択すると、該当するフレームにジャンプする。

&uarr;&darr;：ソートの昇順 降順を変更する

Video▼：ソート機能
- Video：profileのName順にソート
- Created At：profileを作成した日時で順にソート
- Saved At：saveした日時で順にソート
- （controller名）：該当する（controller）に登録した数値でソート
  
ピックアップした画像
- 緑：「Neutral」に ☑ を入れて登録したProfile  
- 赤：数値がデフォルト状態/未編集のProfile  
- 青：選択中（編集中）のprofile  
- 黒：「Enabled」の ☑ を外し、「Disabled」で登録したprofile  
- 白：リターゲット後、登録したprofile  


### Profileの作成

様々な表示のProfileを追加することで解析の精度が上がっていきます。  
単純に数が多ければ良いわけではなく、似た表情のProfileに対し、コントローラーの数字が違ってしまった場合、ノイズになってしまうため注意が必要です。
また、解析する動画毎にProfileを1つ以上作成する必要があります。

```{note}
ROM体操と呼ばれる約50個のProfileの作成をオススメしています。
ROM体操の表情については、スターターキット同梱のPDFファイルをご参照ください
```
```{note}
profileには基本的に全てのRegionの登録を推奨していますが
一部例外があります。
[「Profileを作成するときの注意点 目を閉じる/薄目の時のGaze登録について」](https://zukunfcs.github.io/fcs-doc/latest/jp/008_profile.html#id6)をご参照ください
```

#### 解析したい動画の読み込み方法  

開いた動画ファイル名の上で右クリック  
```{figure} images/P005.jpg
:width: 80%
:align: center

Open
```


```{figure} images/P006.jpg
:width: 80%
:align: center

VideoPlayerに動画が表示されます
```

#### Profileの追加方法

VideoTimelineウィンドウの  
 - スライダーを動かし表情の登録を行いたいフレームで止め  
 - +を押す  

```{figure} images/P009.jpg
:width: 80%
:align: center

Galleryに指定したフレームの画像が追加される
```

```{note}
値が0（未登録）のProfileは赤枠
```

#### Neutralの表情の登録

Neutral表情とは、アクターの表情筋に力が入っていないナチュラルな表情のことです。  
セッション内で必ず一つNeutral表情を設定してください。 

 - Neutralに ☑  
 - 任意の名前に変更  
 - Save
```{figure} images/P010.jpg
:width: 80%
:align: center
```

```{note}
NeutralのProfileは登録が完了すると緑になります。
```
```{figure} images/P011.jpg
:width: 80%
:align: center
```

#### Mayaで表情を調整する場合

 - VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す
  
Galleryに指定したフレームの画像が追加されます。
```{figure} images/P012.jpg
:width: 80%
:align: center
```
```{note}
値が0（未登録）のProfileは赤枠
```
```{figure} images/P013.jpg
:width: 80%
:align: center

追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
```

```{figure} images/image90.jpg
:width: 80%
:align: center

Mayaのコントローラーリグで、追加したアクターの表情と同じになるようにキャラクターの表情を調節
```

```{figure} images/P014.jpg
:width: 80%
:align: center

From Mayaをクリックで、Mayaでの調整情報がFCSに反映されます。
```

```{note}
Syncのプルダウンで「From Maya at save」もしくは「Both」にしている場合は、調整した数値が自動で同期されます。
```

```{note}
コントローラーの登録忘れがあった場合は再度開いたときに作成した表情と異なる場合があります。
その際は、再度登録し忘れたコントローラーを登録しプロファイルの再登録を行ってください。
```
 
 - Nameを任意の名前に変更
 - Save
```{figure} images/P015.jpg
:width: 80%
:align: center
```
```{note}
名前は必ずしも変更する必要はありません。
```

#### FCS上で表情を調整する場合

 - VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す
 
Galleryに指定したフレームの画像が追加されます。
```{figure} images/P012.jpg
:width: 80%
:align: center
```
```{note}
値が0（未登録）のProfileは赤枠
```
 - 追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
```{figure} images/P013.jpg
:width: 80%
:align: center
```

```{warning}
Syncが「No Sync」の場合はProfileの自動情報共有が行われないためMaya上は1つ前に登録した表情のままになっています。
```
```{figure} images/image83.jpg
:width: 80%
:align: center
```

```{note}
Syncを「Both」にした状態で開きなおすと デフォルトの表情になります。  
既にしている場合はスキップ
```
 - Mayaのコントローラーリグで、追加したアクターの表情が同じになるようにキャラクターの表情を調節
```{figure} images/P020.jpg
:width: 80%
:align: center
```

 - To Mayaをクリック
```{figure} images/P016.jpg
:width: 80%
:align: center
```

```{note}
Syncのプルダウンで「To Maya」もしくは「Both」にしている場合は、調整した数値が自動で同期されます。
```

FCSで調整した内容がMayaに反映されます。
```{figure} images/P017.jpg
:width: 80%
:align: center
```

```{note}
絞り込みたい項目（文字含む）のみ表示されるようにするには…
 - ▼Filterから搾りたい項目をクリック
```
```{figure} images/P018.jpg
:width: 80%
:align: center
```


#### PredictでProfileを作成する場合

本ソフトでは、作成したProfileから自動でリターゲットをしてくる  
Predict機能を搭載しています  
ある程度のProfileを登録した後で、追加のProfileを登録する際にPredict機能を使えば、  
登録済のProfileを基に、ソフトが予想した表情を作成してくれます。

```{warning}
Predictで自動リターゲットする精度は、登録済のProfileの精度と連動します。  
また、動画全体を解析するわけではないので注意が必要です。
```

- VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す 
 
Galleryに指定したフレームの画像が追加される
```{figure} images/P012.jpg
:width: 80%
:align: center
```
```{note}
値が0（未登録）のProfileは赤枠
```

 - 追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
```{figure} images/P013.jpg
:width: 80%
:align: center
```

 - Predict実行  
valueの数値が変動します。
```{figure} images/P021.jpg
:width: 80%
:align: center
```

MayaにPredict結果が出るので、  
調整が必要な場合は調整し、登録できる内容になったら
```{figure} images/P022.jpg
:width: 80%
:align: center
```

 - Save
```{figure} images/P023.jpg
:width: 80%
:align: center
```


### Profileを作成するときの注意点

#### 目を閉じる/薄目の時のGaze登録について
```{warning}
目を閉じる、薄目のプロファイルで黒目が見えないものは登録する際にGazeの ☑ を外してください  
解析結果の精度が低下してしまう可能性があります  
```

例：眉のぎゅっと絞る動きを作りたい時には
```{figure} images/P024.jpg
:width: 80%
:align: center
```

 - 表情を調整した上で
```{figure} images/P025.jpg
:width: 80%
:align: center
```

 - Regionのgaze/lowerの ☑ を外す
```{figure} images/P026.jpg
:width: 80%
:align: center
```

 - Save

#### 解析結果が好ましくない場合
```{warning}
解析する動画は、必ず1動画1profile以上作成するようにしてください
Profileを作成していない場合、精度が十分ではない解析結果が出力される可能性があります 
```
Videosウィンドウの「Profiles」をご参照ください    
```{figure} images/P026-02.jpg
:width: 80%
:align: center
```


「Profiles」が表示されない場合  
 - メニューバー上部で右クリック  
 - 「Profiles」に ☑ を入れる  
```{figure} images/P026-03.jpg
:width: 80%
:align: center
```

### トラブルシューティング

#### ＋キーを押してもGalleryにProfileが追加されない場合
＋キーを押してもGalleryにProfileが追加されない場合  
Galleryの表示ウィンドウが小さいケースが考えられます。
```{figure} images/P027.jpg
:width: 80%
:align: center
```

その場合、Galleryウィンドウの◀&rarr;をクリックすると追加したProfileが表示されます。
```{figure} images/P028.jpg
:width: 80%
:align: center
```

```{note}
FCSでは同一フレームのProfileは重複して追加されないようになっています。  
重複した場合、Logウィンドウで  
WARNIG:Frame ○○ already has a Profile associated with it  
と表示されます。  
```
```{figure} images/P029.jpg
:width: 80%
:align: center
```
