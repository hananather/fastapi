# ~/Desktop/LEARN/async/yield_from_chain.py

def bottom():
    print("bottom: yielding 42")
    received = yield 42  # Yields 42, waits for send()
    print(f"bottom: received {received}")
    return received  # This becomes StopIteration.value

def middle():
    print("middle: delegating to bottom")
    result = yield from bottom()  # Magic: automatic delegation
    print(f"middle: bottom returned {result}")
    return result

def top():
    return (yield from middle())

# Run it
gen = top()

# Step 1: Start generator, get first yield
value = next(gen)
print(f"Got: {value}")  # Prints 42

# Step 2: Send value back in
try:
    value = gen.send(value * 2)  # Send 84 back
except StopIteration as exc:
    final_value = exc.value
    print(f"Final return value: {final_value}")  # Prints 84