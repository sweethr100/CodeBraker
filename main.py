def brakecode(user_code):
    output=""
    for i in user_code:
        if i == "m":
            output+="rn"
        elif i == "l":
            output+="I"
        else:
            output+=i
    return output

if __name__ == "__main__":
    user_code = input("니 코드 입력 : ")
    print(brakecode(user_code))