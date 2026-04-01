## Contorollerの登録
 
Contollerウィンドウでは、接続しているMayaSceneのコントローラーリグを登録することができます。

```{list-table}
:widths: 40 60
:header-rows: 0

* - ![](/images/03_workflow_register_controller_window_controller.jpg)
  - Window&rarr;Controllerで  
  Contollerウィンドウが起動します。
```

```{note}
Contollerウィンドウについての説明は[ユーザーガイド/Menu/Window/Contollers](../06_glossary/01_Menu/window)をご覧ください。
```

<br>

```{rubric} **Region（リージョン）とは**
```

FCSでは顔のパーツ区分のことをRegionと呼びます。  

```{note}
 - Upper（アッパー）：眉周りの動きのこと 眉の上下や眉間にしわを寄せる動きなど  
 - Eyelid（アイリッド）：まぶたの動きのこと まばたきや目を細める動きなど  
 - Gaze（ゲイズ）：目線の動きのこと 目線の上下左右や寄り目の動きなど   
 - Lower（ロウワー）：鼻、頬、口周りの動きのこと 頬や鼻から下の動き全般
```

アニメーション解析のため、Upper、Eyelid、Gaze、Lowerにそれぞれコントローラーリグを１つ以上登録してください。    

<br>

また、コントローラーリグの登録時にコントローラーの最大値最小値も登録できます。  
最大値最小値は自動で入力されますが、値があまりにも大きすぎる場合は調整を行って下さい。  

```{figure} /images/03_workflow_register_controller_min_max.jpg
:width: 100%
:align: center
```
<br>

```{warning}
「True/False」などの数値ではないアトリビュートがあると正常に動作しないため、登録から除外してください。
```

<br><br>

```{rubric} **Controllerの登録**
```

Upperの登録を例にcontrollerの登録方法を説明します。  

1. MayaでUpperに登録したいコントローラーを選択し、
```{figure} /images/03_workflow_register_controller_maya_upper_select.jpg
:width: 80%
:align: center
```

<br><br>

2.【Add selected】ボタンを押します。
```{figure} /images/03_workflow_register_controller_add_selected_uppper.jpg
:width: 100%
:align: center
```

<br><br>

3. Mayaで選択したコントローラーが「Controller」に表示されたら、  
チェックボックスや【select All】（=全選択）でUpperに登録したいコントローラーを選択します。
```{figure} /images/03_workflow_register_controller_select_all_uppper.jpg
:width: 100%
:align: center
```

<br><br>

4. 今回はUpperに登録したいので 【Upper】を押します。  
Regionの列にUpperと表示されたら設定完了です。  
```{figure} /images/03_workflow_register_controller_confirmation_uppper.jpg
:width: 100%
:align: center
```

<br><br>

5. 同じ手順で他のRegion（Eyelid/Gaze/lower）も設定してください。  

<br><br>

```{rubric} **連続して登録する場合**
```

Mayaでコントローラーを選択して【Add selected】を実行すると、 選択したコントローラーが「Controller」に追加され、自動的にチェックが入ります。  
```{figure} /images/03_workflow_register_controller_add_selected_improvement.jpg
:width: 100%
:align: center
```

<br><br>

この状態で【Upper】を押すと今までチェックが入っていたコントローラーのチェックが外れ、RegionがUpperに変更されます。  
そのまま別のコントローラーを選択して【Add selected】した例が下図です。
```{figure} /images/03_workflow_register_controller_auto_check.jpg
:width: 100%
:align: center
```

<br>

新しく【Add selected】したコントローラーのみにチェックが入っています。  
このように、連続して登録する際は追加されたコントローラーに対して自動でチェックが反映されるようになっています。

<br>

このとき、Regionを設定せずに新しく【Add selected】した場合にも、今までチェックが入っていたコントローラーのチェックが外れ、新しく追加したコントローラーのみにチェックが入る仕様となっています。  
```{figure} /images/03_workflow_register_controller_add_selected_eyelid.jpg
:width: 100%
:align: center
```

<br><br>


Regionが未登録状態(null)のものがあるとSaveできません。  
controllerウィンドウでは、Regionの種類や登録の有無でフィルターをかけ表示を絞り込むことができます。  

フィルターを『null』にすることで、Regionが設定されてないcontrollerのみを表示できます。  

 - 右上のall▼のタブを選択し、null▼に変更する  
Regionを設定したものを非表示にし、未登録のコントローラーのみ表示させることができます。    
また、Upper/Eyelid/Gaze/Lowerを選択すればそれぞれ登録したRegionで絞り込むこともできます。
```{figure} /images/03_workflow_register_controller_all_null_eyelid.jpg
:width: 100%
:align: center
```

<br>

```{note}
【select All】は表示されているもののみ選択します。  
また、【Unselect All】で選択解除が可能です。
```

<br>


nullで絞り込んでいるのでこの状態でRegionを登録すると非表示になります。  
allに戻すとすべて表示されます。  

---

`````{grid} 1 1 2 2 
:gutter: 3
:items-align: top

````{grid-item}

〇all選択時  

```{image} /images/03_workflow_register_controller_all_view.jpg
:width: 100%
```

````

````{grid-item}

〇null選択時  

```{image} /images/03_workflow_register_controller_null_view.jpg
:width: 100%
```

````

`````

---

<br><br>

```{rubric} **登録しないコントローラーを削除する方法**
```

1.コントローラー単体で削除する場合  
削除したいコントローラーを選択(☑)  &rarr; 【Remove】を押します。
```{figure} /images/03_workflow_register_controller_remove.jpg
:width: 100%
:align: center
```

<br><br>

2.nullのコントローラーを一括で削除する場合  
【Remove empty】を押します。
```{figure} /images/03_workflow_register_controller_remove_empty.jpg
:width: 100%
:align: center
```

<br><br>

Upper/Eyelid/Gaze/Lowerをすべて登録し終えたら 【Save】してください。
```{figure} /images/03_workflow_register_controller_save.jpg
:width: 100%
:align: center
```

<br><br>

```{warning}
Regionが未登録状態(null)のものがあるとSave出来ません
```

<br><br>

---

<br>

```{rubric} **マニュアル以外のコントローラーを登録したい場合**
```
本マニュアルでは、UnrealEngineのMetahumanを使用していますが、別の3DCG作成ソフトで作成したものでも、各部位に連携できるコントローラーリグがあれば対応可能です。  
また、必要最低限のコントローラーのみを登録していますので、任意で登録するコントローラーを増やすことができます。  

<br>

```{rubric} **Add selectでコントローラーの追加ができない場合**
```

設定したMayaバージョンとsceneを作成したMayaバージョンが一致しているか確認してください。    

```{warning} 
設定したバージョンとsceneを作成したMayaバージョンが違うとコントローラーを読み取れません。 
```

<br>

```{rubric} **コントローラーの登録順を変えたい場合**
```

例：L/R　blinkが離れていて不便なのでblinkを上下（隣接するよう）に並べたい場合  

【▶Advanced】 → 【Rearrange】に☑を入れ、  
並び替えたいコントローラーをドラッグしドロップすると、順番を変更できます。  
```{figure} /images/03_workflow_register_controller_Rearrange.jpg
:width: 100%
:align: center
```

<br><br>

```{rubric} **コントローラーの登録順を戻したい場合**
```

【▶Advanced】 → 【Reset】を押すと、前回【Save】した時点での順番に戻ります。
```{figure} /images/03_workflow_register_controller_reset.jpg
:width: 100%
:align: center
```

<br><br>

**作業しやすいように登録順を並び替えたら必ず【Save】してください。**
```{figure} /images/03_workflow_register_controller_save.jpg
:width: 100%
:align: center
```

<br>

---
