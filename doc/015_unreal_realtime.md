## Unrealのリアルタイム通信

FCSは、UnrealEngineにリアルタイムでデータストリーミングする機能を持っています。
この機能を使うためには、FCS側とUnrealEngine側でそれぞれ操作が必要です。

### UnrealEngine側の設定
UnrealEngine側では、FCSLiveLinkプラグインを使用する必要があります。  
FCSLiveLinkプラグインは、UnrealEngine5.3で利用可能です。  
FCSLiveLinkプラグインは以下からダウンロードできます。  

#### 接続設定
1. UnrealEngineのメインウィンドウから、[Edit]>[plugins]を選択して、プラグインウィンドウを開きます。  
2. プラグインウィンドウからFCSLiveLinkにチェックを入れます。
3. [Window]>[Virtual Production]>[Live Link]を選択して、LiveLinkウィンドウを開きます。
4. Livelinkウィンドウ右上隅にある[+Source]を選択します。
5. [FCSLiveLink]を選択し、表示されたUIからFCS入力と一致するようにIPAddress, PortNumber, SubjectNameを設定します。
設定後、OKを選択します。
6. Sourceが作成され、SourceType欄にFCSLiveLinkが追加されます。

#### ABP設定
FCSLiveLinkを使用して、SkeletalMeshを動かすためには、AnimationBlueprintを作成する必要があります。

1. コンテンツブラウザを右クリックして、[Animation]>[Animation Blueprint]を選択し、新しいAnimationBlueprintを作成します。
2. 作成したAnimationBlueprintを開きます。
3. EventGraphを開き、UpdateAnimationノードからEvaluateLiveLinkFrameノードを作成して接続します。
4. EvaluateLiveLinkFrameノードの[Subject]プルダウンに[ControllerValues], [Role]プルダウンに[FCSLiveLinkRole]を設定します。
5. [Data Result]ピンからドラッグし、[Break FCSAnimationBlueprintData]ノードを作成します。
6. [Break FCSAnimationBlueprintData]ノードkar

### FCS側の設定