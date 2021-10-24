# Re.split() in python - hacker rank solution
# Python 3
# Re.split() in python - hacker rank solution START 
regex_pattern = r"[.,]+"    # Do not delete 'r'.
# Re.split() in python - hacker rank solution END
import re
print("\n".join(re.split(regex_pattern, input())))