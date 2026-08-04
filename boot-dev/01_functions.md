# Boot.dev - Functions

## Concept & Explanation

Functions allow us to reuse and organize code. For example, say we have some code that calculates the area of a circle:

```python
radius = 5
area = 3.14 * radius * radius
```

That works! The problem is when we want to calculate the area of other circles, each with its own radius. We could just copy the code and change the variable names like this:

```python
radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2
```

But we want to reuse our code! Why would we want to redo our work? What if we wanted to calculate the area of thousands of circles??? That's where functions help.

Instead, we can define a new function called `area_of_circle` using the `def` keyword.

```python
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result
```

### Breakdown of `area_of_circle`:
- **Parameter**: It takes one input (aka "parameter" or "argument") called `r`.
- **Function Body**: After the `:`, the indented lines form the function body – this is the code block that will run each time we use (aka "call") the function.
- **Return Value**: It returns a single value (the output of the function). In this case, it's the value stored in the `result` variable.

To "call" this function, we pass in any number as the argument (in this case, 5) for parameter `r`, and capture the output into a new variable:

```python
area = area_of_circle(5)
print(area)
# 78.5
```

1. `5` goes in as input `r`.
2. The body of the function runs, storing `78.5` in the `result` variable.
3. The function returns `result`, so `area_of_circle(5)` evaluates to `78.5`.
4. `78.5` is stored in the `area` variable and printed.

Because we've already defined the function, now we can use it as many times as we want with different inputs!

```python
area = area_of_circle(6)
print(area)
# 113.04

area = area_of_circle(7)
print(area)
# 153.86
```

---

## Assignment: Weapon Attack Area

We need to calculate the size of a weapon's "attack area." With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the `area_of_circle` function to do that calculation.

**Goal:** Fix the bug where `spear_area` is `0` by calling the `area_of_circle` function with `spear_length` as input and store the result in `spear_area`.

### Solution Code

```python
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
```

### Output
```text
Sword length: 1.0 meters.
Sword attack area: 3.14 square meters
Spear length: 2.0 meters.
Spear attack area: 12.56 square meters
```
