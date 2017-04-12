# format specifier
formatter= "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %('one','two','three','four')
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
        "I had this thing.",
        "That could type up right .",
        "But I didn't sing.",
        "I said learn creativity"
)
