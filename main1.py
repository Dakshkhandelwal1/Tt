from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
        elevenlabs,
            gladia,
                noise_cancellation,
                    silero,
                    )
                    # The following import statement was incorrectly indented
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a math teacher maria living in tunga,bassi and teach mgggs tunga your goal is to teach user math according to class 10th rbse cirruculum. teach students in a interactive way also ask them question in the mid.")


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
                                stt=gladia.STT(),
                                                                            llm=google.LLM(model="gemini-2.0-flash-exp"),
                                                                                        tts=elevenlabs.TTS(),
                                                                                                    vad=silero.VAD.load(),
                                                                                                                turn_detection=MultilingualModel(),
                                                                                                                        )

    await session.start(
                                                                                                                                            room=ctx.room,
                                                                                                                                                        agent=Assistant(),
                                                                                                                                                                    room_input_options=RoomInputOptions(
                                                                                                                                                                                    # LiveKit Cloud enhanced noise cancellation
                                                                                                                                                                                                    # - If self-hosting, omit this parameter
                                                                                                                                                                                                                    # - For telephony applications, use `BVCTelephony` for best results
                                                                                                                                                                                                                                    noise_cancellation=noise_cancellation.BVC(),
                                                                                                                                                                                                                                                ),
    )
    await session.generate_reply(
                                                                                                                                                                                                                                                                            instructions="Greet the user and offer your assistance."
                                                                                                                                                                                                                                                                                    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))