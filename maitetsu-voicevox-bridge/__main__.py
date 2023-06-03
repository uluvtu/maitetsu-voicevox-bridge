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
    parser.add_argument("word", type=str, help="read out sentence")
    args = parser.parse_args()

    async with Client() as client:
        audio_query = await client.create_audio_query(args.word, speaker=1)
        with open(args.output, "wb") as f:
            f.write(await audio_query.synthesis(speaker=args.speaker))


if __name__ == "__main__":
    asyncio.run(main())
