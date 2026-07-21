from openai import OpenAI

class LLMService:
    def __init__(self):
        self.client=OpenAI()
    def generate_answer(self,question,context):
        prompt=f"""
You are an HR Assistant.
Answer only from the provided context.
If the answer is not available,
reply:

"I don't know."

context :
{
    context
}

Question :
{
    question
}

"""
        response=self.client.responses.create(
            model="gpt-5",
            input=prompt
        )
        return response.output_text
    