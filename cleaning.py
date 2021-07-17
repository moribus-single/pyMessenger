def clean_msg(text: str) -> str:
    """cleaning from excess gaps, new lines and tabs."""
    tmp = list(text.strip())
    flag = True

    while flag:
        for i in range(len(tmp)):

            if tmp[i] == ' ' and tmp[i + 1] == ' ' or tmp[i] == '\n' and tmp[i + 1] == '\n' or tmp[i] == '\t':
                tmp.pop(i)
                break

            if i == len(tmp) - 1:
                flag = False

    return "".join(tmp)

