def is_opening_tag(tag):
        return not tag.startswith('</')
    
def matching_tag(tag):
    if is_opening_tag(tag):
        return '</' + tag[1:]
    return '<' + tag[2:]

def getTags(htmlStr):
    tags = htmlStr.split('>')
    for i in range(len(tags)):
        if tags[i] == '':
            tags.remove(tags[i])
        elif tags[i][0] != '<':
            ind = tags[i].find('<')
            tags[i] = tags[i][ind:] + '>'
        else:
            tags[i] = tags[i] + '>'
    return(tags)

def check_html_nesting(htmlstring):
    tags = getTags(htmlstring)

    stack = []
    var = None

    for i, tag in enumerate(tags):
        if is_opening_tag(tag):
            stack.append((tag, i))
        else:
            # print(stack)
            # print(var, '--', stack[-1][0], tag)
            if stack and matching_tag(stack[-1][0]) == tag:
                stack.pop()
            else:
                if not stack and not is_opening_tag(tag):
                    return False 
                if var is None:
                    var = stack[-1][0] 
                else:
                    return False
    if not stack:
        return True

    if len(stack) == 1 and var is None:
        return stack[0][0]

    if var != None:
        return var[1:-1]
    return False

html_correct = "<div><b><p>hello world</p></b></div>"
html_incorrect = "<div><i>hello</i>world</b>"
html_fixable = "</div><p></p><div>"
html_fixable1 = "<em></em><em></em><p></b>"

print(check_html_nesting(html_correct))  # Should return True
print(check_html_nesting(html_incorrect))  # Should return False
print(check_html_nesting(html_fixable)) 
print(check_html_nesting(html_fixable1)) # Should suggest a fix
