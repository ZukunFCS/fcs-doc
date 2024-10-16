## Solverの詳細設定（細かな調整が必要な方向け）
本ページは、おもに解析したアニメーション出力結果を更に細かく調整したい方向けのページになります。  
必要に応じて、各種設定を自由にカスタマイズすることが可能です。  

### Solverの画面説明

![](images/Sol001.png)

▼Global：解析時の設定を変更できます。
- ☑ Fisheye：チェックを入れると、魚眼レンズで撮影された動画を解析する仕様に最適化される

```{note}
デフォルト設定ではチェックが入っているため、広角レンズで撮影された動画を解析する際はチェックを外してください。
```

- Smoothing：アニメーション出力時にスムージング処理をかける設定を変更できます。各Regionごとに個別に変更可能です。  
  - Smoothing：スムージング処理の有無（基本的には有りを推奨）
  - Weight：一回あたりのスムージング処理の強度  
    数値が大きいほどスムージング処理が強くかかる（アニメーションカーブが滑らかになる）
  - Reps：スムージング処理の回数  
    回数を多くするほどアニメーションカーブが滑らかになる

▼Post processing：アニメーション出力時にクランプ処理をかける設定などを変更できます。
- Enforce annotation：アニメーション出力範囲内にProfileを作成したフレームが含まれる場合、チェックを入れると解析による予測値よりもリターゲット値を優先する
- Clamp mode：クランプ処理の設定を切り替える
  - No Clamp：クランプ処理なし
  - Hard Clamp：アニメーションカーブを、Controllerウィンドウで設定した最大値 - 最小値でクランプする（クランプされた範囲のスムージング処理なし）
  - Soft Clamp：アニメーションカーブを、Controllerウィンドウで設定した最大値 - 最小値でクランプする（クランプされた範囲のスムージング処理あり）

Train：ユーザーが変更した設定を参照し、Solverを再構築します。  
Delete cache：変更前の設定による解析キャッシュを削除します。  
