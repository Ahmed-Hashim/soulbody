"""import openai
openai.api_key ="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"
def ask(data):
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"أريد كتابة نص اعلاني مكون من 15 كلمة عن {data}",
    temperature=0.5,
    max_tokens=1500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    message=response.choices[0].text
    return message
"""