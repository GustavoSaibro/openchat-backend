curl -X POST http://localhost:21001/register_worker -H "Content-Type: application/json" -d '{"worker_name": "http://localhost:21002", "check_heart_beat":true}'