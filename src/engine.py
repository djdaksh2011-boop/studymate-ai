import re, math, collections
STOP=set('the a an is are was were to of and or in on for with this that it as by from be can will at into your you we our their have has'.split())
def sentences(text):
    return re.split(r'(?<=[.!?])\s+|\n+',text.strip())
def keywords(text,limit=12):
    words=re.findall(r"[a-zA-Z][a-zA-Z'-]{2,}",text.lower())
    return [w for w,_ in collections.Counter(w for w in words if w not in STOP).most_common(limit)]
def summarize(text,count=4):
    s=[x.strip() for x in sentences(text) if len(x.strip())>15]
    if not s:return []
    freq=collections.Counter(re.findall(r'[a-z]+',text.lower()))
    scores=[]
    for i,line in enumerate(s):
        tokens=[w for w in re.findall(r'[a-z]+',line.lower()) if w not in STOP]
        scores.append((sum(freq[w] for w in tokens)/math.sqrt(len(tokens)+1),i))
    chosen={i for _,i in sorted(scores,reverse=True)[:count]}
    return [x for i,x in enumerate(s) if i in chosen]
def flashcards(text,limit=8):
    result=[]
    for s in sentences(text):
        m=re.match(r'\s*([\w\s-]{3,45}?)\s+(?:is|are|means|refers to|:|–)\s+(.{12,})',s,re.I)
        if m:result.append({'question':'What is '+m.group(1).strip()+'?', 'answer':m.group(2).strip()})
    return result[:limit]
def quiz(text,limit=5):
    keys=keywords(text,25)
    result=[]
    for line in sentences(text):
        present=[k for k in keys if re.search(r'\b'+re.escape(k)+r'\b',line,re.I)]
        if not present or len(line)<25:continue
        answer=present[0]
        result.append({'question':re.sub(r'\b'+re.escape(answer)+r'\b','_____',line,count=1,flags=re.I),'answer':answer})
        if len(result)>=limit:break
    return result
def study_plan(topics,days):
    items=[x.strip() for x in re.split(r'[,\n]+',topics) if x.strip()]
    return [{'day':i+1,'focus':items[i%len(items)],'activity':('Learn + make notes' if i%3==0 else 'Practice + recall' if i%3==1 else 'Revise + self-test')} for i in range(days)] if items else []
