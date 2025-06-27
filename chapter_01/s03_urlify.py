def urlify_forrest(url, num):
    chars = []
    i = 0
    while i < num:
        if url[i] == ' ':
            chars.append('%20')
        else:
            chars.append(url[i])
        i += 1
    return ''.join(chars)


def urlify_forrest2(url, num):
    return url[:num].replace(' ', '%20')
