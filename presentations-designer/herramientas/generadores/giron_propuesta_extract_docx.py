import zipfile,re,json,html
z=zipfile.ZipFile(r'C:\Users\FULLSE~1\AppData\Local\Temp\gir\p.docx')
x=z.read('word/document.xml').decode('utf8')
paras=[]
for p in re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S):
    out=''
    for r in re.findall(r'<w:r[ >].*?</w:r>',p,flags=re.S):
        b = bool(re.search(r'<w:b(?: [^>]*)?/>',r)) and not re.search(r'<w:b w:val="(0|false)"',r)
        t=''
        for m in re.finditer(r'<w:t[^>]*>(.*?)</w:t>|<w:br/>|<w:tab/>',r,flags=re.S):
            if m.group(0).startswith('<w:br') : t+='\n'
            elif m.group(0).startswith('<w:tab'): t+=' '
            else: t+=m.group(1)
        t=html.unescape(html.unescape(t))
        if not t: continue
        out += ('**'+t+'**') if (b and t.strip()) else t
    out=out.replace('****','')
    paras.append(out)
json.dump(paras,open(r'C:\Users\FULLSE~1\AppData\Local\Temp\gir\paras.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
for i,p in enumerate(paras,1):
    if '**' in p or '\n' in p or '&#' in p or '#91' in p: print(i,repr(p[:110]))
