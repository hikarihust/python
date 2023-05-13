# Input : Cho 1 chuỗi và tag html
# Output: Tạo ra tag html với nội dung là chuỗi 
                                        
content = "Hello"
tag     = "div"
result1  = "<{tag}>{content}</{tag}>".format(tag = tag, content = content)
result2  = "<%s>%s</%s>" % (tag, content, tag)
print(result1)
print(result2)