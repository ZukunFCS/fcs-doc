# Tips
## レイアウトについて
FCSにはレイアウトの変更・保存機能があります。
モニターの数や作業環境に合わせてカスタマイズしてください。
  
### 配置例（二画面）
<img width="3840" height="1014" alt="image" src="https://github.com/user-attachments/assets/5162f71c-fd16-4391-9883-0e2f24faa763" />


### 配置例（一画面）
<img width="1916" height="997" alt="image" src="https://github.com/user-attachments/assets/1c0435df-03e8-4ed0-bb85-2a356edc7031" />

### レイアウトの変更方法
- View＞Layout からプリセットを呼び出すことができます。
また、各ウィンドウはドラッグ＆ドロップでFCS内を移動・配置することができます。
お好きな配置で作業してください。

- 現在のレイアウトを保存することも可能です。<BR>
View＞Layout＞Save current

- 保存したレイアウトのデータは以下のパスに格納されます。
```
C:\Users\[ユーザー名]\.fcs\Cortado\[FCSバージョン]\layouts\saved
```
 
<BR><BR><BR>

## ベースシーンについて
FCSは、シーン内にFCS用のカメラが無い場合、perspのカメラの位置を参照してカメラを作成します。<BR>
常に一定の画角でプレイブラストを出力するためには、あらかじめ適切な位置やサイズのイメージプレーンをシーンに配置し、ベースシーンとして保存しておく方法を推奨しています。

※作成する前にFCSの設定ウィンドウ（File＞Settings＞▼Maya）でカメラ名とイメージプレーン名がどのように指定されているかを確認してください。<BR>
以下fcs_cam、imagePlaneという名前が指定されているものとして説明します。

### ベースシーンの作成
①FCS用のカメラを顔のモデルが中心に来るように配置します。<BR>
使用アトリビュート例：fcs_cam.translateY、fcs_cam.translateZ、fcs_camShape.focalLength
<img width="269" height="379" alt="image" src="https://github.com/user-attachments/assets/cbf2e24d-b4a6-43e1-b138-8780fb67f8b4" />

<BR>

②FCS用のカメラを使用した状態でView ＞ Image Plane ＞ Import Image...から静止画用イメージプレーンを配置します。
![basescene2](https://github.com/user-attachments/assets/09d31116-7ed4-4678-8f73-8613f409b28b)

<BR>

③イメージプレーンをお好みの大きさに変更し、配置したい場所へ移動します。<BR>
使用アトリビュート例：imagePlaneShape.depth、imagePlaneShape.sizeX、imagePlaneShape.sizeY、imagePlaneShape.offsetX、imagePlaneShape.offsetY

![basescene3](https://github.com/user-attachments/assets/b80464be-1d39-423a-8d70-2503c64f0eba)

<BR>

④静止画連番画像を再生するためにimagePlaneShape.useFrameExtensionをON（1）にします。
![basescene4](https://github.com/user-attachments/assets/8e62aa82-d97e-48d9-9377-12744e83ec98)

<BR>

⑤Mayaシーンを保存し、File＞Session▶＞Info...からMaya Sceneに登録します。
![basescene5](https://github.com/user-attachments/assets/ae7cbed2-08e3-47d8-95eb-4ea58aecacec)
