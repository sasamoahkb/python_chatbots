from openai import OpenAI
import gradio

client = OpenAI(
    api_key = ""
)

messages = [{"role": "user", "content": "You are a clinical Psychologist"}]

def CustomChatBot(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )
    bot_reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": bot_reply})
    return bot_reply

demo = gradio.Interface(fn=CustomChatBot, inputs = "text", outputs = "text", title = "Mind Body and Soul")
demo.launch()