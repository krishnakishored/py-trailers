import ollama


model_name = "llama3.2:1b"

# response = ollama.list()
# print(response)

# == Chat example ==
# res = ollama.chat(
#     model=model_name,
#     messages=[
#         {"role": "user", "content": "why is the sky blue?"},
#     ],
# )
# print(res["message"]["content"])

# # == Chat example streaming ==
# res = ollama.chat(
#     model=model_name,
#     messages=[
#         {
#             "role": "user",
#             "content": "why is the ocean so salty?",
#         },
#     ],
#     # stream=False,
#     stream=True,
# )
# # print(res["message"]["content"])

# for chunk in res:
#     print(chunk["message"]["content"], end="", flush=True)


# # ==================================================================================
# # ==== The Ollama Python library's API is designed around the Ollama REST API ====
# # ==================================================================================

# == Generate example ==
# res = ollama.generate(
#     model=model_name,
#     prompt="why is the sky blue?",
# )

# show
# print(ollama.show(model_name))


# # Create a new model with modelfile
modelfile = f"""
FROM {model_name}
SYSTEM You are very smart assistant who knows everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1
"""

ollama.create(model="knowitall", modelfile=modelfile)

res = ollama.generate(model="knowitall", prompt="why is the ocean so salty?")
print(res["response"])


# # delete model
ollama.delete("knowitall")
