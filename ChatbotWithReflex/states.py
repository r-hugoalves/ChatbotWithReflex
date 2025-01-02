import reflex as rx
import os
from openai import AsyncOpenAI

class State(rx.State):
    
    question: str
    chat_history: list[tuple[str, str]]
    
    @rx.event
    async def answer(self):
        
        # OpenAI Settings
        client = AsyncOpenAI(
            api_key=os.environ["OPENAI_API_KEY"]
        )

        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )
        
        # Add response to the answer when the chatbot responds
        answer = ""
        self.chat_history.append((self.question, answer))
        self.question = ""
        yield
        
        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer
                )
                yield