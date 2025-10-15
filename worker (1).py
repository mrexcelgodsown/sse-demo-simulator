import redis
import time
import re

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

def process_task(task_id):
    task_data = redis_client.hgetall(f"task:{task_id}")
    if not task_data:
        return
    redis_client.hset(f"task:{task_id}", "status", "processing")
    time.sleep(2)  # Simulate processing
    # Mock DLP: Mask credit card numbers
    masked_task = re.sub(r'\d{4} \d{4} \d{4} \d{4}', '**** **** **** ****', task_data['task'])
    result = f"Processed with SSE: No threats detected. DLP applied: {masked_task}"
    redis_client.hset(f"task:{task_id}", mapping={
        "status": "completed",
        "result": result
    })

while True:
    task_id = redis_client.brpop("task_queue", timeout=5)
    if task_id:
        process_task(task_id[1])