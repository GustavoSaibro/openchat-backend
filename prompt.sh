curl -X POST http://localhost:8001/complete -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'

# curl http://localhost:8000/v1/completions \
#   -H "Content-Type: application/json" \
#   -d '{
#     "model": "vicuna-7b-v1.5",
#     "prompt": "Once upon a time",
#     "max_tokens": 100,
#     "temperature": 0.5
#   }'