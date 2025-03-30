# RadioLab
録音したラジオ放送を分析するプロジェクト
## 環境構築
```
conda create --name radio python=3.10 -y
conda activate radio
pip install torch torchvision torchaudio
pip install -U openai-whisper
```