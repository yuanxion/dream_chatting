### Model

```sh
HF_ENDPOINT=https://hf-mirror.com HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download --resume-download silk-road/ChatHaruhi_RolePlaying_qwen_7b --local-dir silk-road/ChatHaruhi_RolePlaying_qwen_7b --local-dir-use-symlinks False
```

### Run
```sh
cd demo/
python3 demo-stream.py
```
