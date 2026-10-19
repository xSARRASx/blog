# Transcription de secours d'une video YouTube publique via l'API Gemini (quand yt-dlp est bloque).
# Usage : python3 .robot-blog/transcrire-gemini.py <ID_VIDEO> <sortie.txt>
# La cle est lue dans GEMINI_API_KEY (jamais dans le repo).
import json,subprocess,os,sys
vid=sys.argv[1]; out=sys.argv[2]
tmp=os.path.dirname(os.path.abspath(out))
fb=os.path.join(tmp,'gem_body.json'); fo=os.path.join(tmp,'gem_out.json')
body={"contents":[{"parts":[
 {"file_data":{"file_uri":"https://www.youtube.com/watch?v="+vid}},
 {"text":"Transcris intégralement et mot pour mot, en français, tout ce qui est dit dans cette vidéo, du début à la fin. Ne résume pas, ne reformule pas, n'ajoute aucun titre ni commentaire : donne uniquement le texte prononcé, en paragraphes."}]}],
 "generationConfig":{"temperature":0,"maxOutputTokens":30000}}
open(fb,'w').write(json.dumps(body))
if os.path.exists(fo): os.remove(fo)
subprocess.run(["curl","-sS","--max-time","600","-o",fo,"-w","http=%{http_code}\n","-H","x-goog-api-key: "+os.environ["GEMINI_API_KEY"],"-H","Content-Type: application/json","--data-binary","@"+fb,
 "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"])
d=json.load(open(fo))
if 'candidates' not in d: print(json.dumps(d)[:800]); sys.exit(1)
c=d['candidates'][0]; t=''.join(p.get('text','') for p in c['content']['parts'])
open(out,'w').write(t); print('finish',c.get('finishReason'),'mots',len(t.split())); print(d.get('usageMetadata'))
