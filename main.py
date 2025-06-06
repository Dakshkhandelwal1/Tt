from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext, function_tool
from livekit.plugins import google
#from livekit.plugins.turn_detector.multilingual import MultilingualModel # Corrected indentation
#from livekit.plugins import noise_cancellation 
load_dotenv()


class mukeshji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are Mukesh kumar sharma, a dedicated science teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach science according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")

class shrikantji(Agent):
    def __init__(self,chat_ctx: ChatContext) -> None:
        super().__init__(instructions="""You are shrikant vijay, a dedicated mathematics teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach mathematics according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.after connectingwith a student compulsarily greet him and ask him about what he want to study in mathematics""")

class anitaji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are anita sharma, a dedicated sanskrit teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach sanskrit according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")


class Laxminarayanji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are Laxminarayan, a dedicated hindi teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach hindi according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")

class manishji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are Manish kumar meena, a dedicated english teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach english according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")

class kanchanji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are kanchan sharma, a dedicated social science teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach social science according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")


class mohakji(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are mohak jindal, a dedicated computer science teacher living in Tunga, Bassi. You teach Class 10 students at MGGGS Tunga, following the Rajasthan Board of Secondary Education (RBSE) curriculum.
        
        Your primary goal is to teach computer science according to the Class 10 RBSE syllabus in an interactive, engaging, and student-friendly manner. Break down complex concepts into simple explanations using relatable examples. Frequently involve the student by asking questions mid-lesson to check understanding and encourage participation.
        
        Maintain a warm, encouraging, and clear tone throughout the session. Emphasize conceptual clarity and step-by-step problem solving. Use the teaching style of a real classroom teacher who interacts actively with students.""")
        self.session.generate_reply(instructions="Greet the student and ask him about what he want to study.")
@function_tool()
async def c2s() -> None:
    """Use this tool to handoff the call to mukesh ji."""

        # Perform a handoff, immediately transfering control to the new agent
    return mukeshji()
@function_tool()
async def c2m(ctx: agents.JobContext):
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
                                                                                                                                                                            agent=shrikantji(),
                #         room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
         #   noise_cancellation=noise_cancellation.BVC(), 
      #  ),
    )
 #   await ctx.connect()
    await session.generate_reply(
                                 instructions="Greet the user and offer your assistance."
    )

    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=c2m)) 

@function_tool()
async def c2ss() -> None:
    """Use this tool to handoff the call to anitaji."""

        # Perform a handoff, immediately transfering control to the new agent
    return anitaji()

@function_tool()
async def c2sst() -> None:
    """Use this tool to handoff the call to kanchanji."""

        # Perform a handoff, immediately transfering control to the new agent
    return kanchanji()


@function_tool()
async def c2e() -> None:
    """Use this tool to handoff the call to manishji."""

        # Perform a handoff, immediately transfering control to the new agent
    return manishji()


@function_tool()
async def c2h() -> None:
    """Use this tool to handoff the call to Laxminarayanji."""

        # Perform a handoff, immediately transfering control to the new agent
    return laxminarayanji()

@function_tool()
async def c2cs() -> None:
    """Use this tool to handoff the call to mohakji."""

        # Perform a handoff, immediately transfering control to the new agent
    return mohakji()


class hod(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are the Head of Department (HOD).

🎓 Your only responsibility is to welcome the student and connect them to Mathematics teacher using c2m tool """,
        tools = [c2m]
                        )
    #@function_tool()
    '''async def c2m(self) -> None:
        """called when user want to connect with mathematics teacher ."""

        # Perform a handoff, immediately transfering control to the new agent
        return shrikantji(chat_ctx=self.session._chat_ctx)'''


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
                                                                                                                                                                            agent=hod(),
                #         room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
         #   noise_cancellation=noise_cancellation.BVC(), 
      #  ),
    )
 #   await ctx.connect()
    await session.generate_reply(
                                 instructions="Greet the user and offer your assistance."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint)) # Corrected indentation
