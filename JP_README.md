English -> [README.md](https://github.com/Cj-bc/mcUI/blob/master/README.md)

[![tipmona](https://img.shields.io/badge/tipme-%40tipmona-orange.svg)](https://twitter.com/share?text=%40tipmona%20tip%20%40Cj-bc%2011.7)  [![monya/mona](https://img.shields.io/badge/tipme-%40monya/mona-orange.svg)](https://monya-wallet.github.io/a/?address=MBdCkYyfTsCxtm1wZ1XyKWNLFLYj8zMK3V&scheme=monacoin)  [![tipkotone](https://img.shields.io/badge/tipme-%40tipkotone-orange.svg)](https://twitter.com/share?text=%40tipkotone%20tip%20%40Cj-bc%2011.7)

このmod(?)は**あなたのパソコンを破壊する恐れすらあります**。自己責任でお使いください。
現段階、編集機能がつくまではその危険度は低いですが、ご了承ください。

# 概要

  mcUIは(恐らく)世界初の! パソコンに3DUIを提供するminecraftのmodです。
  何を言ってるのかわからない？
  ならここにある（予定）の動画を見てくれ！！（未定）


# なんだこれは

  mcUIはMinecraftのmodです。
  でもただのmodじゃありません。
  mcUIは、3DになったパソコンのUIを提供する（多分）唯一のmodです！！！

# 特徴

  * CUIをGUI、そしてmcUIへ-- 次世代型（ぽい）3DのUIを提供します（でも開発者はCUIが好きです）
  * Minecraftのmodとしては特異なることとして、(Jam modが動作すれば)マイクラのバージョンなんざ関係ありません！

## 進捗

  * カレントディレクトリのエントリ表示(mcUI.pyを実行してください)
  * 多彩なコンフィグ([config.py](mcpipy/mcui/config.py)を参照)
  * ファイルタイプ(現状は拡張子からの判定)に応じて表示するブロックを変更
  * ファイルタイプは拡張可能。対応するブロックも変更可能
  * 様々なチャットコマンド。チャット欄でタイプするだけで実行されます
    -  [x] `cat`     ---  'cat' コマンドの結果をMinecraftのチャット欄に出力
    -  [x] `cd`      ---  pane 0のカレントディレクトリを変更
    -  [ ] `cp`      ---  `cp`を実行
    -  [x] `exit`    ---  mcUIを終了。mcUIで作成されたブロック等は片付けられます。
    -  [ ] `help`    ---  mcUIのヘルプを表示
    -  [x] `ls`      --- `ls`を実行し、結果を新しいpaneに保存
    -  [ ] `man`     ---  'man'を実行
    -  [ ] `mv`      ---  'mv <file> <dst>'を実行
    -  [x] `pane`    ---  paneを管理します。サブコマンド: `create`/`mv`/`deactivate`/`activate`/`list`
    -  [x] `pwd`     ---  pane 0のカレントディレクトリを表示
    -  [ ] `reload`  ---  リロード
    -  [ ] `rm`      ---  `rm`を実行


# 必要なものたち

  上記の通り、バージョンは統一してあれば問題ありません！

  * [minecraft](https://minecraft.net)
  * [minecraft forge](https://files.minecraftforge.net)
  * [Minecraft Jam mod](https://github.com/arpruss/raspberryjammod)

# いんすとーるぅ

  今現在インストール方法はありません（だって出来上がってないんだもの）
  のちには、homebrewに対応させようかなとか思ってます。

# (無謀な)今後について

実現するとは言ってないが、やりたい事たち

-  [x] カレントディレクトリのエントリを設置する
-  [ ] とりあえず、読み込み部分を完成させる
-  [ ] 書き込みができるようにする
-  [ ] アプリケーションにアクセスできるようにする
-  [ ] 通知受け取れるようにする
-  [ ] サーバー対応できるようにする
-  [ ] マルチ対応もできればいいなぁ
-  [ ] VRChatのサーバ繋ぎたい
-  [ ] 依存するmodを少しずつ自前のに変えていく
-  [ ] ファイル共有とかしてみたい
-  [x] お寿司食べたい
