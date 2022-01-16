from deepgram import Deepgram
import asyncio, json

# The API key
DEEPGRAM_API_KEY = 'API_KEY'

AUDIO_URL = 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav'

async def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    source = {'url': AUDIO_URL}

    print('Requesting transcript...')
    print('Your file may take up to a couple minutes to process.')

    response = await dg_client.transcription.prerecorded(source,  {'punctuate': True})
    print(json.dumps(response, indent=4))

asyncio.run(main())
