# -*- coding: utf-8 -*-
import re, sys, io, unicodedata

path = sys.argv[1]; KW = sys.argv[2].lower()
html = io.open(path, encoding='utf-8').read()
body = re.sub(r'<style.*?</style>', ' ', html, flags=re.S|re.I)
body = re.sub(r'<script.*?</script>', ' ', body, flags=re.S|re.I)
heads = re.findall(r'<h([23])[^>]*>(.*?)</h\1>', body, flags=re.S|re.I)
heads = [(lv, re.sub(r'<[^>]+>', '', t).strip()) for lv, t in heads]
text = re.sub(r'<[^>]+>', ' ', body).replace('&nbsp;', ' ').replace('&rsquo;', "'")
text = re.sub(r'&#\d+;', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()
words = re.findall(r"[A-Za-zÀ-ÿ0-9'’%€-]+", text); nw = len(words)

def norm(s):
    s = s.lower().replace('’', "'")
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

kw_n = norm(KW)
occ = len(re.findall(re.escape(kw_n), norm(text)))
h_with = [(lv,t) for lv,t in heads if kw_n in norm(t)]
pct_h = 100.0*len(h_with)/len(heads) if heads else 0
sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.strip()) > 3]
TRANS = ["tout d'abord","ensuite","de plus","par ailleurs","cependant","toutefois","concretement",
"ainsi","donc","enfin","en revanche","surtout","precisement","de ce fait","en effet","pourtant",
"heureusement","avant tout","au final","quant aux","quant a","en pratique","notamment","par exemple",
"d'ailleurs","en outre","desormais","a l'inverse","effectivement","par consequent","en conclusion",
"d'abord","premierement","deuxiemement","troisiemement","en resume","autrement dit"]
TRANS = sorted(set(TRANS), key=len, reverse=True)
def has_trans(s):
    n = norm(s)
    return any(n.startswith(t + ' ') or n.startswith(t + ',') for t in TRANS)
tr = sum(1 for s in sentences if has_trans(s))
pct_tr = 100.0*tr/len(sentences) if sentences else 0
PASSIVE = re.compile(r"\b(est|sont|était|étaient|sera|seront|a été|ont été|être|soit)\s+[a-zà-ÿ]+(é|és|ée|ées|i|is|ie|ies|u|us|ue|ues)\b", re.I)
passives = [s for s in sentences if PASSIVE.search(s)]
longs = [s for s in sentences if len(s.split()) > 20]
dups = []
for i in range(1, len(sentences)):
    a = norm(sentences[i-1]).split(); b = norm(sentences[i]).split()
    if a and b and a[0] == b[0]: dups.append((sentences[i-1][:45], sentences[i][:45]))
internal = re.findall(r'href="(https://www\.locationcourteduree\.fr/[^"]+)"', html)
blank_internal = re.findall(r'<a[^>]+href="https://www\.locationcourteduree\.fr/[^"]*"[^>]*target="_blank"', html)
mdash = html.count('—') + html.count('&mdash;')
h1 = len(re.findall(r'<h1', html, re.I))
faq_p = len(re.findall(r'<p class="faq[a-z0-9]*-divider"', html, re.I))
faq_h3 = len(re.findall(r'<h3 class="faq[a-z0-9]*-divider"', html, re.I))
first_p = re.search(r'<p[^>]*>(.*?)</p>', body, flags=re.S)
kw_first = kw_n in norm(re.sub(r'<[^>]+>','',first_p.group(1))) if first_p else False
def f(ok): return "OK " if ok else "KO "
print("="*60)
print("MOTS               : %d" % nw)
print(f(occ>=12)+"MOT-CLE exact      : %d occurrences | densite %.2f%%" % (occ, 100.0*occ/nw))
print(f(50<=pct_h<=75)+"SOUS-TITRES kw     : %d/%d = %.1f%% (cible 50-65, max 75)" % (len(h_with), len(heads), pct_h))
print(f(pct_tr>=40)+"TRANSITIONS        : %d/%d = %.1f%%" % (tr, len(sentences), pct_tr))
print(f(len(passives)==0)+"PASSIVES           : %d/%d" % (len(passives), len(sentences)))
print(f(100.0*len(longs)/len(sentences)<25)+"PHRASES >20 mots   : %d/%d = %.1f%%" % (len(longs), len(sentences), 100.0*len(longs)/len(sentences)))
print(f(not dups)+"STARTS consecutifs : %d" % len(dups))
print(f(len(set(internal))>=2)+"LIENS INTERNES     : %d (uniques %d)" % (len(internal), len(set(internal))))
print(f(not blank_internal)+"INTERNES _blank    : %d" % len(blank_internal))
print(f(mdash==0)+"TIRETS LONGS       : %d" % mdash)
print(f(h1==0)+"H1                 : %d" % h1)
print(f(faq_p==0 and faq_h3>0)+"FAQ dividers       : h3=%d p=%d" % (faq_h3, faq_p))
print(f(kw_first)+"KW 1er paragraphe  : %s" % kw_first)
nwrap = html.count('class="lcd-wrap"')
print(f(nwrap == 1)+"WRAPPER lcd-wrap   : %d (obligatoire)" % nwrap)
print("="*60)
for a,b in dups[:10]: print("  DUP: '%s...' -> '%s...'" % (a,b))
for s in passives[:10]: print("  PASSIVE: %s" % s[:110])
