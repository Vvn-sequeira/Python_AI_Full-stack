
def chai():
    yield "it's a cup of chai"
    yield "it's a cup of tea"
    yield "it's a cup of  Juice"
    yield "it's a cup of Milk"

chai_statement = chai()
# print(chai_statement)

# for chai in chai_statement:
#     print(chai)

print(next(chai_statement))
print(next(chai_statement))
print(next(chai_statement))