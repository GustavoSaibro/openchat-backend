import re
from openai import AsyncOpenAI
import asyncio
from concurrent.futures import ThreadPoolExecutor

openai = AsyncOpenAI(api_key="test", base_url="http://localhost:8000/v1/")

# openai.api_key = "test"
# openai.base_url = "http://localhost:8000/v1/"

model = "vicuna-7b-v1.5"
# prompt = "Once upon a time"

_executor = ThreadPoolExecutor(1)


async def prompt_response2(prompt):   
    response_prompt = ""

    with openai.chat.completions.with_streaming_response.create(
      prompt=prompt,
      model=model,
    ) as response:
      print(response.headers.get("X-My-Header"))

      for line in response.iter_text():
          print(line)


    return response_prompt

async def prompt_response(prompt):
    stream = await openai.completions.create(model=model, prompt=prompt, max_tokens=500, stream=True)
    response_prompt = ""
    regex_pattern = r'[^.]*\.'
    async for chunk in stream:
       response_prompt+=chunk.choices[0].text
    
    matches = re.findall(regex_pattern, response_prompt)
    answer = ''.join(matches)
    return answer

async def completion_prompt2(prompt):
    # loop = asyncio.new_event_loop()
    loop = asyncio.get_event_loop()
    # asyncio.set_event_loop(loop)
    try:
      # completion = await loop.run_in_executor(_executor, prompt_response, prompt)
      # completion = await asyncio.run(prompt_response(prompt), debug=True)
      completion = await asyncio.get_event_loop().run_until_complete(prompt_response(prompt))
    except RuntimeError as e:
      if "This event loop is already running" in str(e):
        # completion = await asyncio.run(asyncio.gather(prompt_response(prompt)),debug=True)
        completion = await asyncio.get_event_loop().run_until_complete(asyncio.gather(prompt_response(prompt)))
      else:
          raise
    # finally:
    #    loop.close()

    # completion = await loop.run_until_complete(prompt_response(prompt))
    # completion = loop.run_in_executor(_executor, prompt_response, prompt)
    # t = await asyncio.gather(completion)
    
    # completion = await loop.run_until_complete(prompt_response(prompt))
    # completion  = await loop.run_in_executor(_executor, openai.completions.create(model=model, prompt=prompt, max_tokens=64))
    # completion  = await openai.completions.create(model=model, prompt=prompt, max_tokens=64)
    return prompt + completion.choices[0].text

async def generate_loop():
   return

async def completion_prompt(prompt):
  # completion  = await openai.completions.create(model=model, prompt=prompt, max_tokens=64)
  completion = await prompt_response(prompt)
  return prompt + completion



# def completion_prompt(prompt):
#     thread = Thread(target=prompt_response, args=prompt)
#     thread.start()
#     # thread = Thread(target=tread_completion, args=(prompt)) 
#     thread.start()
#     thread.join()
#     return thread

# # create a completion
# completion = openai.completions.create(model=model, prompt=prompt, max_tokens=64)
# # print the completion
# print(prompt + completion.choices[0].text)

# # create a chat completion
# completion = openai.chat.completions.create(
#   model=model,
#   messages=[{"role": "user", "content": "Hello! What is your name?"}]
# )
# # print the completion
# print(completion.choices[0].message.content)