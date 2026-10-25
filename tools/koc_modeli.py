"""Uygulamadaki koç modelinden sitenin küçük modelini hazırlar.

Kullanım: python3 tools/koc_modeli.py <uygulama.glb> <çıktı.glb>
Ardından (README → "Koçunla tanış"):
  npx -y @gltf-transform/cli@4 prune <çıktı> <çıktı>
  npx -y @gltf-transform/cli@4 webp <çıktı> <çıktı>
  npx -y @gltf-transform/cli@4 meshopt <çıktı> <çıktı>

Sitedeki üç hareket ve bekleme duruşu kalır; duvar ve sopa sahneden çıkar
(kalan veriyi `prune` atar). Yatak ve rengi uygulamadaki gibi kalır.
"""
import json
import struct
import sys

HAREKETLER = {'shoulder_elevation', 'glute_bridge', 'cat_cow', 'idle_breathe_01'}
ATILAN = {'duvar', 'çubuk'}

src, dst = sys.argv[1], sys.argv[2]
b = open(src, 'rb').read()
n = struct.unpack('<I', b[12:16])[0]
j = json.loads(b[20:20 + n])
binary = b[20 + n:]

j['animations'] = [a for a in j['animations'] if a['name'] in HAREKETLER]
assert len(j['animations']) == len(HAREKETLER), [a['name'] for a in j['animations']]
atilan = {i for i, x in enumerate(j['nodes']) if x.get('name') in ATILAN}
assert len(atilan) == len(ATILAN), atilan
for x in j['nodes']:
    if 'children' in x:
        x['children'] = [c for c in x['children'] if c not in atilan]
for s in j['scenes']:
    s['nodes'] = [c for c in s['nodes'] if c not in atilan]

js = json.dumps(j, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
js += b' ' * (-len(js) % 4)
with open(dst, 'wb') as f:
    f.write(struct.pack('<4sII', b'glTF', 2, 12 + 8 + len(js) + len(binary)))
    f.write(struct.pack('<I4s', len(js), b'JSON'))
    f.write(js)
    f.write(binary)
print(dst, [a['name'] for a in j['animations']])
