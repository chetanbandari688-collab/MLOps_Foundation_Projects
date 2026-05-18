import psutil
def test_ai_ready_status():
ram_usage = psutil.virtual_memory().percent
assert ram_usage < 80, "error: RAM usage too high for AI training!"
print("System is ready for AI training!")

