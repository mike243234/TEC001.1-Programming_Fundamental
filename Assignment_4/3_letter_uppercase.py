def is_valid_course_code(code):
    if len(code) != 6:
        return False
    
    letters = code[:3]
    digits = code[3:]
    
    return letters.isupper() and letters.isalpha() and digits.isdigit()
code = input("please type your course code:")
print(is_valid_course_code(code))