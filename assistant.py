from openai import OpenAI

client = OpenAI(
    api_key = "PRIVATE")

messages = []
def getAssistantType():
    bot_type = input("What type of assistant would you like to create?\n")
    messages.append({"role": "system", "content": bot_type})
    print("\n" + "Ready when you are!" + "\n")
    
def chat_with_bot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    messages.append({"role": "user", "content": prompt})
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    getAssistantType()
    while True:
        user_input = input("you: ")
        if user_input in ["exit", "qiut", "bye"]:
            break
        
        response = chat_with_bot(user_input)
        messages.append({"role": "assistant", "content": response})
        print("\n" + "chatbot: ", response + "\n")    