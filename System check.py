import platform

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"system: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {platform.processor()}")
print("="*100)