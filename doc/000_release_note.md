# リリースノート
## FCS 24.10.06
- リリース日: 2024/10/16
- リリースバージョン: 24.10.06
- リリースステージ: Stable

### ！ダウングレードできません！
**このバージョンで作成または開いたセッションを24.10.05を含む、以前のバージョンを開くことができません。
ご注意ください。**
アップデートされる前に、プロジェクトフォルダーをバックアップすることを強く推奨いたします。


### 概要
1. 動画表示が１フレームずれていることを修正しました
2. ソフト起動時の最適化
3. ログ方式の改善

#### 動画表示が１フレームずれていることを修正しました
Video/Playerの０フレームが重複して出力されていたことを修正いたしました。 （１００フレーム目が９９フレーム目として表示されていました）  
Profileのフレームカウントも1フレームずれていました。
そのため、以前のバージョンンで作成されたセッションについては、現バージョンで開くことにより、自動的に修正されるようになります。
ただし、修正されたものに関しては、以前のバージョン（24.10.05を含む）で開くことができなるなりました。
お手数をおかけしまして、大変申し訳ございません。

## FCS 24.10.05
- リリース日: 2024/10/11
- リリースバージョン: 24.10.05
- リリースステージ: Stable

### 概要
1. 動画開く際に、キャッシュされるはずのデータがキャッシュされていないことを修正しました
2. Auto　Profileのプロファイルの出力番号がずれていることを修正
3. リアルタイムアプリへの出力するソルバーの形式を修正
4. コントローラーの可動域が正しくない場合、エラーが表示されるように修正

## FCS 24.10.04
- リリース日: 2024/10/07
- リリースバージョン: 24.10.04
- リリースステージ: Stable

### 概要
1. 特定の場合において、ランドマーク画像の出力時にアプリケーションがクラッシュするバグを修正しました。


## FCS 24.10.03
- リリース日: 2024/09/25
- リリースバージョン: 24.10.03
- リリースステージ: Stable

### 概要
1. Gallery機能修正
2. インストーラ修正
3. その他修正

### 詳細
#### Gallery機能修正
1. Syncにチェックが入っている状態でResetボタンを押すとMayaにも反映されるようになりました
2. Editorにて、To Mayaなどの際にDisabledになっているリージョンの値は送信しないようになりました

#### インストーラ修正
1. デフォルトのインストール先をCドライブに変更しました
2. インストーラのアイコンを変更しました
3. インストーラが日本語・英語両方に対応しました

#### その他
1. コントローラーをリネームする際にアプリが落ちてしまう問題を修正しました
2. スムージングが適用されていない問題を修正しました（24.10.01）
3. Prioritize Profileの動作を修正しました  
<br>

## FCS 24.10.02
- リリース日: 2024/09/09
- リリースバージョン: 24.10.02
- リリースステージ: Beta

### 概要
1. Galleryのフィルタリング機能強化  
    プロフィールの一括変更や削除ができるようになりました  
2. EditorのLMの表示がONの場合、別のプロフィールを開いてもONの状態のままにしました（計算済みの場合のみ）  
3. Editorのコントローラー値を変更する箇所の表示方式を変更しました
4. Galleryの表示方式を改善しました
5. プロフィール優先機能(Prioritize Profile)を追加しました
6. コントローラーの名前を一括変更する機能を追加しました
7. ビデオ再生の速度を向上させました
8. リアルタイム版への出力機能を追加しました

### 詳細
#### Galleryのフィルタリング
1. 動画名、各Regionの状態などでフィルタリングする機能、一括リージョンON/OFF・一括削除などの機能を追加しました

#### Editorのコントローラー値の表示方式
1. Ctrl＋クリックで数値を入力
2. カーソルに合わせて数値が設定されるようになりました
   
#### プロフィール優先機能
1. FCSから出力されたアニメーションに関して、プロファイルが存在するフレームにおいて表情を厳密に一致させる機能を追加しました
2. 有効化するにはSolver/Post-processing/Prioritize ProfileをONにしてください

#### コントローラーの名前を一括変更
1. Controller Infoでコントローラーを選択し、Renameを押すと、コントローラーのリネームができるようになりました
2. 名前の変更に伴い、Galleryで登録された情報も変更されます

#### ビデオ再生の速度を向上させました
1. 動画をメモリーにコピーすることにより、HDDなどのストレージ媒体より早く再生できるようになります
2. デフォルトで有効になります
3. メモリーに余裕があれば開いた動画（5本まで）をメモリーに保存することができます、複数の動画を同時に編集してもメモリーにキャッシュするようになります

#### リアルタイム版への出力機能
1. Solver/ExportでFCSで作成されたソルバーが出力されます
2. リアルタイムサーバ（準備中）に読み込むとFCSでオフライン出力に近いクオリティーのアニメーションがリアルタイムで出力できるようになります  
<br>

## FCS 24.10.01
- リリース日: 2024/08/29
- リリースバージョン: 24.10.01
- リリースステージ: Beta

### 概要
#### マニュアル関連
1. 24.07, 24.10など、バージョンごとのマニュアルが確認できるようになりました
2. [English manual](https://zukunfcs.github.io/fcs-doc/24.10/en/index.html) (draft) now available

#### セットアップ
1. インストーラーからインストールができるようになりました
2. ffmpegがシステムにインストールされていない場合、自動的にダウンロードできるようになりました

#### Auto Pickup α
[動画から特定のフレームを自動的にGalleryに追加する機能を実装しました。](https://zukunfcs.github.io/fcs-doc/latest/en/012_auto_pickup.html)

#### 自動更新
新しいバージョンが発行された際に、FCSのUIから更新内容の表示およびダウンロードができるようになりました

#### Linuxサポート
実験的にLinux対応を始めました

### アップデート注意
以下のバージョンを使用しこれからアップデートする方は以下の事項に注意していただければと思います

1. 24.07  
    特になし 

### 詳細
#### マニュアル
1. マニュアルサイトが日本語・英語に対応しました。左下で切り替えられます
2. FCSソフトから開く際にはソフトに対応するバージョンが自動で開くようになります

#### インストール
1. ビルド方式をThemidaに変更しました。その際に、バーチャルマシン（VM）やデバッガーとの共同使用が対象外になりました。環境によって利用できなくなった方はご連絡ください。
2. インストーラーを追加しました。デフォルトではC:\FCSで作成されるようになります。インストール先フォルダの書き込み権限が必要になりますので、書き込み権限のないフォルダに入れると問題が発生します。

#### FFMPEG
1. 起動時に、ffmpegがシステムパスに存在しないとき、自動的に[github](https://github.com/BtbN/FFmpeg-Builds/)からダウンロードするようになっています。
2. Githubへの接続ができないお客様は手動でffmpegをインストールし、pathに追加するようにお願いいたします。

#### ユーザインタフェース  
1. ビデオ名をダブルクリックで開けるようになりました  
2. プログラム終了時のタブのレイアウトが保存されるようになりました  
3. FCS初回起動時のタブのレイアウトを整理しました  
4. タイムラインをドラッグする際に、範囲からカーソルをずらしても動くようになりました  
5. 一部のUIから選択できる項目がプログラムを終了しても保存されるようになりました
6. UIの日本語訳を更新しました
7. キーボードショートカットを修飾キーに対応させました
8. 一部の機能にキーボードショートカットを対応させました　　
   - Profile保存
   - Profileから動画を開く
   - Editorの値をMayaへ送信 (To Maya) 
   - Mayaからリグの値を受信 (From Maya)
   - レイアウトの変更 
9. Enforce AnnotationをPrioritize Profileへ名称変更しました

#### Maya
1. FCSからmayaへ送信する際に、Disabledされたリージョンを送信しなくなりました 

#### 自動更新
1. プログラム起動時に、新しいアップデータを検出するようになりました
2. アップデートに関しては以下の設定がSettingsウィンドウから変更できます
   1. Update channel: All | Patch | None  
    すべてをアップデートする、もしくはバグ修正（保守アップデート）のみ、またはアップデートしないことが選択できます
   2. Use Beta
    安定しない機能を含めたベータ版の利用ができるようになります

#### Linuxサポート
FCSがFedora 8に対応しました。ご興味のある方はご連絡ください。

#### その他
1. プログラムデータの保存先を`$USER/.fcs/Cortado`から`$USER/.fcs/Cortado/$version`に変更しました
