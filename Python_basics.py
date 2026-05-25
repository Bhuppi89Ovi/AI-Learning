name ="Anthropic"
year = 2024
score = 98.5
is_ai = True
print("Basic variable types:")
print(name)
print(year)
print(score)
print(is_ai)


# String operations
print("String operations:")
prompt = "What is the capital of France?"
print(len(prompt))
print(prompt.upper())
print(prompt.lower())
print(prompt.replace("France", "Germany"))
print(f"The prompt is: {prompt}")

# List operations
print("List operations:")
models = ["GPT-3", "BERT", "T5", "RoBERTa", "Claude-3", "Gemini-1.5 Pro", "llama-2-70b-chat-hf"]
print(models[0])  # GPT-3
print(models[3])  # RoBERTa
print(models[-1]) # llama-2-70b-chat-hf
print(models[1:4]) # ['BERT', 'T5', 'RoB
models.append("Gemini-1.5 Pro")
print(models)

for model in models:
    print("Model:", model)

# Dictionary operations
print("Dictionary operations:")
model_info = {
    "GPT-3": {"year": 2020, "developer": "OpenAI"},
    "BERT": {"year": 2018, "developer": "Google"},
    "T5": {"year": 2019, "developer": "Google"},
    "RoBERTa": {"year": 2019, "developer": "Facebook"},
    "Claude-3": {"year": 2024, "developer": "Anthropic"},
    "Gemini-1.5 Pro": {"year": 2024, "developer": "Google"},
    "llama-2-70b-chat-hf": {"year": 2023, "developer": "Meta"}
}

print(model_info["GPT-3"])  # {'year': 2020, 'developer': 'OpenAI'}
print(model_info["Claude-3"]["year"])  # 2024

# Conditional statements
print("Conditional statements:")
if score > 90:
    print("Excellent score!")
elif score > 80:
    print("Good score!")
else:
    print("Keep practicing!")


# Looping through dictionary
print("Model information Loop:")
for model, info in model_info.items():
    print(f"{model} was developed by {info['developer']} in {info['year']}.")


# Function definition
print("Function to get model info:")
def get_model_info(model_name):
    return model_info.get(model_name, "Model not found")

print(get_model_info("T5"))  # {'year': 2019, 'developer': 'Google'}
print(get_model_info("Unknown Model"))  # Model not found


