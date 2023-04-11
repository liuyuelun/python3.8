import openai

openai.api_key = "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"


def generate_response(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message.strip()


while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("GPT: " + response)
