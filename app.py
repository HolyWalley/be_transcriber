from flask import Flask, request, jsonify
import requests
import nemo.collections.asr as nemo_asr
import soundfile as sf
import tempfile

app = Flask(__name__)

# Initialize your ASR model
# asr_model = nemo_asr.models.EncDecRNNTBPEModel.restore_from("model.nemo")
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("nvidia/stt_be_conformer_ctc_large")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Extract the S3 URL from the request
    data = request.json
    s3_url = data['s3_url']

    # Download the audio file from S3
    response = requests.get(s3_url)
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        tmp.write(response.content)
        tmp_filename = tmp.name

    # Transcribe the audio file
    transcriptions = asr_model.transcribe(paths2audio_files=[tmp_filename])

    # Return the transcription
    return jsonify({'transcription': transcriptions})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
