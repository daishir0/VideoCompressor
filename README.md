# VideoCompressor

## Overview
A script to compress video files using ffmpeg with customizable parameters.

## Installation
1. Clone this repository:
   ```
   git clone <repository-url>
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have `ffmpeg` installed on your system.

## Usage
```
python compress_video.py <input_file> <output_file> [-b BITRATE] [-c CODEC] [-p PRESET] [--crf CRF]
```

## Note
- Ensure that `ffmpeg` binary is installed and accessible from your system's PATH.
- Adjust the parameters as needed to get the desired compression and quality.

## License
This project is licensed under the MIT License.

---

# VideoCompressor

## 概要
ffmpegを使用してカスタマイズ可能なパラメータでビデオファイルを圧縮するスクリプト。

## インストール方法
1. このリポジトリをクローンします:
   ```
   git clone <repository-url>
   ```
2. 必要なパッケージをインストールします:
   ```
   pip install -r requirements.txt
   ```
3. システムに`ffmpeg`がインストールされていることを確認してください。

## 使い方
```
python compress_video.py <入力ファイル> <出力ファイル> [-b ビットレート] [-c コーデック] [-p プリセット] [--crf CRF]
```

## 注意点
- `ffmpeg`のバイナリがインストールされ、システムのPATHからアクセス可能であることを確認してください。
- 圧縮と品質を希望通りにするために、必要に応じてパラメータを調整してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。
