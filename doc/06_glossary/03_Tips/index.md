## Tips

このページではFCSの便利なTipsや各機能について説明します。

`````{tab-set}

````{tab-item} ベースシーンについて

<br>

FCSは、シーン内にFCS用のカメラが無い場合、perspのカメラの位置を参照してカメラを作成します。  
常に一定の画角でプレイブラストを出力するためには、あらかじめ適切な位置やサイズのイメージプレーンをシーンに配置し、ベースシーンとして保存しておく方法を推奨しています。  

※作成する前にFCSの設定ウィンドウ[File＞Settings＞▼Maya](../01_Menu/settings.md)でカメラ名とイメージプレーン名がどのように指定されているかを確認してください。  
以下fcs_cam、imagePlaneという名前が指定されているものとして説明します。  

<br>

```{rubric} **ベースシーンの作成**
```

① FCS用のカメラを顔のモデルが中心に来るように配置します。  
使用アトリビュート例：fcs_cam.translateY、fcs_cam.translateZ、fcs_camShape.focalLength
```{figure} /images/06_glossary_Tips_basescene_Maya_01.jpg
:width: 50%
:align: center
```

<br><br>

② FCS用のカメラを使用した状態でView ＞ Image Plane ＞ Import Image...から静止画用イメージプレーンを配置します。  
```{figure} /images/06_glossary_Tips_basescene_Maya_02.jpg
:width: 50%
:align: center
```

<br><br>

③ イメージプレーンをお好みの大きさに変更し、配置したい場所へ移動します。  
使用アトリビュート例：imagePlaneShape.depth、imagePlaneShape.sizeX、imagePlaneShape.sizeY、imagePlaneShape.offsetX、imagePlaneShape.offsetY  
```{figure} /images/06_glossary_Tips_basescene_Maya_03.jpg
:width: 50%
:align: center
```

<br><br>

④ 静止画連番画像を再生するためにimagePlaneShape.useFrameExtensionをON（1）にします。  
```{figure} /images/06_glossary_Tips_basescene_Maya_04.jpg
:width: 50%
:align: center
```

<br><br>

⑤ Mayaシーンを保存し、File＞Session▶＞Info...からMaya Sceneに登録します。  
```{figure} /images/06_glossary_Tips_basescene_Maya_05.jpg
:width: 70%
:align: center
```

````

````{tab-item} レイアウトについて

<br>

<!-- 更新予定・コメントアウトしてます。 -->
<!-- FCSにはレイアウトの変更・保存機能があります。
モニターの数や作業環境に合わせてカスタマイズしてください。

```{rubric} **配置例（二画面）**
```

```{figure} /images/06_glossary_Tips_layout02.jpg
:width: 80%
:align: center
```

<br><br>

```{rubric} **配置例（一画面）**
```
```{figure} /images/06_glossary_Tips_layout01.jpg
:width: 80%
:align: center
```

<br><br> -->

```{rubric} **レイアウトの変更方法**
```

Viewウィンドウ → Layoutからレイアウトのプリセットを呼び出せます。  
また、各ウィンドウはドラッグ＆ドロップでFCS内を移動・配置することができます。  
お好きな配置で作業してください。  

Viewウィンドウ → Layoutから変更したレイアウトを保存することも可能です。  

```{include} ../06_glossary/01_Menu/view.md
    :start-after: <!--start_here_Tips-->
    :end-before: <!--end_here_Tips-->
```

<br>

```{note}
Viewウィンドウについての説明は[ユーザーガイド/Menu/view](../06_glossary/01_Menu/view.md)をご覧ください。
```

<br>

保存したレイアウトのデータは以下のパスに格納されます。  
```
C:\Users\$USER\.fcs\Cortado\$FCS_VERSION\layouts\saved
```

<br>

````


`````