from pathlib import PureWindowsPath
from voicevox import Client
import argparse
import asyncio


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--speaker", type=int, help="VOICEVOX speaker id", default=1
    )
    parser.add_argument(
        "-o", "--output", type=PureWindowsPath, help="output path", default="output.wav"
    )
    parser.add_argument("--speed", type=float, help="reading speed", default=None)
    parser.add_argument("--volume", type=float, help="voice volume", default=None)
    parser.add_argument("--api_base_url",type=str, help="VOICEVOX API url", default="http://localhost:50021")
    parser.add_argument("word", type=str, help="read out sentence")
    args = parser.parse_args()

    
    async with Client(args.api_base_url) as client:
        audio_query = await client.create_audio_query(args.word, speaker=args.speaker)
        if args.speed is not None:
            audio_query.speed_scale=args.speed
        if args.volume is not None:
            audio_query.volume_scale=args.volume
        with open(args.output, "wb") as f:
            f.write(await audio_query.synthesis(speaker=args.speaker))


if __name__ == "__main__":
    asyncio.run(main())
