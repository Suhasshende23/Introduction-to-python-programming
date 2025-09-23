import sys

print("Arguments:", sys.argv)


# if len(sys.argv)<2:
#     sys.exit("Too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("too many arguments")

# print("Arguments ",sys.argv[1])


if len(sys.argv)<2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Arguments",arg)