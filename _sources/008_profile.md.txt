## Profileの作成

### Profileの作成の前に...

#### 解析動画を開く方法

Window▶VideosでVideosウィンドウが開きます。  
Videosウィンドウでは解析したい動画を開いたり、インポートすることができます。
![](images/P26_VideosWindow.PNG)

・import
![](images/P002.png)

ウィンドウがポップアップされるので  
・解析したい動画をクリックし開く
![](images/P003.png)

```{note}
Shift+クリックで複数同時にimportできます。
```

Videosウィンドウに解析したい動画が表示されます。
![](images/P004.png)

#### Timelineの画面説明

![](images/P019.png)
- Timeline：バーを左右に動かし、ビデオを手動で再生させる
- [0][20130]：ビデオの縮尺を変更できる。
- [7967]：現在のフレーム数
- |< >|：1フレーム
- << >>：登録したprofileにジャンプする
- ＞ ||：動画の再生・停止（再生すると一時停止ボタンが表示される）
- 1:2▼：表示する動画の解像度を変更する（Scaleが小さくなるほどプレビューが鮮明に、大きくなるほど荒くなる）
- Sync：✅でTimeline操作状況をMayaのTimeSliderと一致させる
- EveryFrame/Realtime：再生速度を変更する
- Video：Video playerに表示されている動画名

#### Editorの画面説明

![](images/P007.png)
No Sync▼
- To Maya：FCSをMayaと連動させる
- From Maya at save：MayaをFCSに連動させる
- Both：FCSとMayaを双方向で連動させる
- No Sync：FCSとMayaを連動させない

```{note}
本ページではProfileの追加手順・編集手順について記載しております  
Mayaをベースに表情を調整するのか、FCSをベースに表情を調整するのかは任意で使い分けることができますが、  
最初は「Both」での使用をオススメします。
```

Neutral：✅デフォルトの表情として必ず1つ登録する  
Enabled：✅解析する素材として使用する/□使用しない  

Controller▼
- Controller：コントローラー表示が名前になる
- Value：コントローラー表示が数字になる 

▼Region
- Upper/Eyelid/Gaze/Lower：✅調整した情報を登録する  

▼Utils
- To Maya：FCS上で操作した値をMayaへ送る
- From Maya：Mayaで操作した値をFCSへ送る
- Predict：画像から表情を解析し、Mayaの3Dモデルに反映する機能

LM：LandMarkを表示する  

▼Filter
- ▼all/Upper/Eyelid/Gaze/Lower：選択した項目でコントローラーを絞り込む
- [ ]：入力した文字でコントローラーを絞り込む  

▼Reset：入力した情報を削除する

Name：Profileとして登録する名前

Save：変更した情報を保存する

画像部分：Timelineから+で追加した画像が表示される

コントローラー：Controller Infoで登録したコントローラーが表示される

#### Galleryの画面説明

![](images/P008.png)
作成したProfileが表示されるウィンドウ  
- 緑：Neutralで登録したProfile
- 赤：登録（save）していないProfile
- 白：登録（save）済のProfile


### Profileの作成

様々な表示のProfileを追加することで解析の精度が上がっていきます。  
単純に数が多ければ良いわけではなく、似た表情のProfileに対し、コントローラーの数字が違ってしまった場合、ノイズになってしまうため注意が必要です
```{note}
ROM体操と呼ばれる約50個のProfileの作成をオススメしています
ROM体操の表情については、スターターキットをご参照ください
```
```{note}
profileには基本的に全てのRegionの登録を推奨します
```

#### 解析したい動画の読み込み方法  

・開いた動画ファイル名の上で右クリック  
・Open
![](images/P005.png)

VideoPlayerに動画が表示されます。
![](images/P006.png)

#### Profileの追加方法

VideoTimelineウィンドウの  
・スライダーを動かし表情の登録を行いたいフレームで止め  
・+を押す  
・Galleryに指定したフレームの画像が追加される
![](images/P009.png)

```{note}
値が0（未登録）のProfileは赤枠
```

#### Neutralの表情の登録

Neutral表情とは、アクターの表情筋に力が入っていないナチュラルな表情のことです。  
セッション内で必ず一つNeutral表情を設定してください。 
・Neutralに✅  
・任意の名前に変更  
・Save
![](images/P010.png)

```{note}
NeutralのProfileは登録が完了すると緑になります。
```
![](images/P011.png)

#### Mayaで表情を調整する場合

・VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す  
Galleryに指定したフレームの画像が追加されます。
![](images/P012.png)
```{note}
値が0（未登録）のProfileは赤枠
```
・追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
![](images/P013.png)

・Mayaのコントローラーリグで、追加したアクターの表情と同じになるようにキャラクターの表情を調節
![](images/image90.png)

・From Mayaをクリック
![](images/P014.png)
Mayaでの調整情報がFCSに反映されます。

```{note}
Syncのプルダウンで「From Maya at save」もしくは「Both」にしている場合は、調整した数値が自動で同期されます。
```

```{note}
コントローラーの登録忘れがあった場合は再度開いたときに作成した表情と異なる場合があります。
その際は、再度登録し忘れたコントローラーを登録しプロファイルの再登録を行ってください。
```
 
・Nameを任意の名前に変更
・Save
![](images/P015.png)
```{note}
名前は必ずしも変更する必要はありません。
```

#### FCS上で表情を調整する場合

・VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す  
Galleryに指定したフレームの画像が追加されます。
![](images/P012.png)
```{note}
値が0（未登録）のProfileは赤枠
```
・追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
![](images/P013.png)

```{warning}
Syncが「No Sync」の場合はProfileの自動情報共有が行われないためMaya上は1つ前に登録した表情のままになっています。
```
![](images/image83.png)

```{note}
Syncを「Both」にした状態で開きなおすと デフォルトの表情になります。  
既にしている場合はスキップ
```
・Mayaのコントローラーリグで、追加したアクターの表情が同じになるようにキャラクターの表情を調節
![](images/P020.png)

・To Mayaをクリック
![](images/P016.png)

```{note}
Syncのプルダウンで「To Maya」もしくは「Both」にしている場合は、調整した数値が自動で同期されます。
```

FCSで調整した内容がMayaに反映されます。
![](images/P017.png)

```{note}
絞り込みたい項目（文字含む）のみ表示されるようにするには…
・▼Filterから搾りたい項目をクリック
```
![](images/P018.png)


#### PredictでProfileを作成する場合

本ソフトでは、作成したProfileから自動でリターゲットをしてくる  
Predict機能を搭載しています  
ある程度のProfileを登録した後で、追加のProfileを登録する際にPredict機能を使えば、  
登録済のProfileを基に、ソフトが予想した表情を作成してくれます。

```{warning}
Predictで自動リターゲットする精度は、登録済のProfileの精度と連動します。  
また、動画全体を解析するわけではないので注意が必要です。
```

・VideoTimelineウィンドウのスライダーを動かし表情の登録を行いたいフレームで止め+を押す  
Galleryに指定したフレームの画像が追加される
![](images/P012.png)
```{note}
値が0（未登録）のProfileは赤枠
```

・追加した赤色の画像をクリックし、Editor画面に表示されている画像が同じであることを確認
![](images/P013.png)

・Predict実行  
valueの数値が変動します。
![](images/P021.png)

MayaにPredict結果が出るので、  
調整が必要な場合は調整し、登録できる内容になったら
![](images/P022.png)

・Save
![](images/P023.png)


### Profileを作成するときの注意点

```{warning}
目を閉じる、薄目のプロファイルで黒目が見えないものは登録する際にGazeの✅を外してください  
解析結果の精度が低下してしまう可能性があります  
```

例：眉のぎゅっと絞る動きを作りたい時には
![](images/P024.png)

・表情を調整した上で
![](images/P025.png)

・Regionのgaze/lowerの✅を外す
![](images/P026.png)

・Save

### トラブルシューティング

#### ＋キーを押してもGalleryにProfileが追加されない場合
＋キーを押してもGalleryにProfileが追加されない場合  
Galleryの表示ウィンドウが小さいケースが考えられます。
![](images/P027.png)

その場合、Galleryウィンドウの◀▶をクリックすると追加したProfileが表示されます。
![](images/P028.png)

```{note}
FCSでは同一フレームのProfileは重複して追加されないようになっています。  
重複した場合、Logウィンドウで  
WARNIG:Frame ○○ already has a Profile associated with it  
と表示されます。  
```
![](images/P029.png)
