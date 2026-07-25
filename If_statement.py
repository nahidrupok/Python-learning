is_male = False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are nighter male or tall")

is_student=True
is_graduate=False
if is_student and is_graduate:
    print("You are not eligible for this company")
else:
    print("You must complete your study.")
    
is_rain=True
is_sunny=True

if is_rain and is_sunny:
    print("Take your Umbrella")
elif is_rain and not(is_sunny):
    print("Open your umbrella")
elif not(is_rain) and is_sunny:
    print("Donot open your umbrella")
else:
    print("Keep your umbrella in your bag")