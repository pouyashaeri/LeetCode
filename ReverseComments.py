def reverseComment(comments):
    # reverseComments = []
    # if comments:
    #     for i in range (len(comments)-1 , -1, -1):
    #         reverseComments.append(comments[i])

    # return reverseComments

    reverseComments = []
    while comments:
        reverseComments.append(comments.pop())

    return reverseComments


print(reverseComment(["A great work", "B nice job", "C awesome!"]))
print(reverseComment(["First comment", "Second comment", "third comment!"]))
print(reverseComment(["", "Second comment", "third comment!"]))
print(reverseComment([""]))
print(reverseComment([]))