from html2image import Html2Image
from PIL import Image

hti = Html2Image(output_path='./generated-images')

def get_parts(html):
    parts = []
    part_type = []
    temp = ""
    flag = False

    for i in range(0, len(html)):
        if html[i] == '$':
            if flag == False:
                flag = True
                part_type.append(0)
                parts.append(temp)
                temp = ""
            else:
                flag = False
                part_type.append(1)
                parts.append(temp)
                temp = ""
        else:
            temp = temp + str(html[i])
    
    if temp != "":
        parts.append(temp)
        part_type.append(0)

    return parts, part_type

html = ""
with open('./figma_htmlgenerator/index.html') as html_file:
    for line in html_file:
        html += line

parts, part_type = get_parts(html)
n = len(parts)
print("parts:", sum(part_type))
print("generated-images:", 2**sum(part_type))
print("\n")

for i in range(0, 2**n):
    ok = False
    for j in range(0, n):
        if ((i & (1 << j)) == 0) and (part_type[j] == 0):
            ok = True
    if ok:
        continue
    
    get_bin = lambda x: format(x, 'b')
    subset = get_bin(i)
    p_set = ''
    for j in range(0, n):
        if part_type[j] == 1:
            p_set = p_set + str(subset[j])
    print(p_set)

    temp = ""
    for j in range(0, n):
        if (i & (1 << j)) != 0:
            temp += parts[j]
    
    # html to png
    f = open('./figma_htmlgenerator/temp.html','w')
    f.write(temp)
    f.close()
    hti.screenshot(
        url="./figma_htmlgenerator/temp.html",
        save_as=f"f{p_set}.png"
    )
    print("\n")

    # crop
    im = Image.open(f"./generated-images/f{p_set}.png")
    left = 0
    top = 0
    right = 842
    bottom = 790
    im = im.crop((left, top, right, bottom))
    im.save(f"./generated-images/f{p_set}.png", 'PNG')