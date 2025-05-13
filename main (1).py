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
from livekit.plugins.turn_detector.multilingual import MultilingualModel # Corrected indentation

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are Shrikant Vijay, a dedicated mathematics teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach mathematics according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
                                                                llm=google.beta.realtime.RealtimeModel(
                                                                                model="gemini-2.0-flash-exp",
                                                                                                voice="Puck",
                                                                                                                temperature=0.8,
                                                                                                                                instructions="You are a helpful assistant"
                                                                                                                                            ))

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
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint)) # Corrected indentation