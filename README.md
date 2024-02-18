This is a simple http interface for NVIDIA NeMo [model](https://huggingface.co/nvidia/stt_be_conformer_ctc_large) for transcribing Belarusian speech to text

#### How to run?

```bash
docker build . -t be_transcriber
```

```
docker run be_transcriber
```

#### Warning

It looks like it's not possible to build it for mac OS because of absence of triton library support.
