
l =  [
  {"step":"START", "content":"User wants to solve the mathematical expression 3+3/12*45."},
  {"step":"PLAN", "content":"We should apply the BODMAS rule (Brackets, Orders, Division/Multiplication, Addition/Subtraction)."},
  {"step":"PLAN", "content":"First, we handle division and multiplication from left to right: 3 / 12 = 0.25."},
  {"step":"PLAN", "content":"Next, multiply the result by 45: 0.25 * 45 = 11.25."},
  {"step":"PLAN", "content":"Finally, add this to 3: 3 + 11.25 = 14.25."},
  {"step":"OUTPUT", "content":"3+3/12*45=14.25"}
]

print(l[0].get("content"))