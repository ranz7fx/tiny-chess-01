import json as J,os,urllib.request as r
V=os.environ["MAKEFUN_ENV_URL"]
L=40000;M=10**5;I=M+1
A=[0,100,320,330,500,900,0]
T=[0,'KKKKPUU7PFAKKKK_PPUdUU_i}}}}KKKK','##--#7KK-KUZ-PZ_-KZ_-PUZ#7KP##--','7AAAAKKKAKPUAPPUAKUUAUUUAPKK7AAA']+['K'*32]*2+['-###-###-###-###7--#A777__KK_iUK']
N=(33,18,14,31,-33,-18,-14,-31);B=(-17,-15,15,17);D=(-16,-1,1,16)
X={0:13,7:14,4:12,112:7,119:11,116:3}
b=[0]*128;W={};G={};U=[];Q=[0]*64
F=Exception
def q(s):return ord(s[0])+16*ord(s[1])-881
def a(s,y):
 for d in(15*y,17*y):
  t=s-d
  if not t&0x88 and b[t]==y:return 1
 for d in N:
  t=s+d
  if not t&0x88 and b[t]==2*y:return 1
 for d in B+D:
  t=s+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==5*y or p==6*y and t==s+d or p==(3*y if d in B else 4*y):return 1
    break
   t+=d
 return 0
def g(z=0):
 m=[]
 for f,p in enumerate(b):
  if f&0x88 or p*S<=0:continue
  v=abs(p)
  if v==1:
   d=16*S;ts=[]
   t=f+d
   if b[t]==0:
    ts.append(t)
    if(f>>4)==(1,6)[S<0]and b[f+2*d]==0:ts.append(f+2*d)
   for e in(d-1,d+1):
    t=f+e
    if not t&0x88 and(b[t]*S<0 or t==Y):ts.append(t)
   for t in ts:
    if(t>>4)==(7,0)[S<0]:
     for k in(5,4,3,2):m.append(f|t<<7|k<<14)
    elif not z or t&7!=f&7:m.append(f|t<<7)
  else:
   for d in(N,B,D,B+D,B+D)[v-2]:
    t=f+d
    while not t&0x88 and b[t]*S<=0:
     if not z or b[t]:m.append(f|t<<7)
     if b[t]or v%4==2:break
     t+=d
 if not z:
  kf=(4,116)[S<0]
  for cs,kt,rf,em in((1,6,7,(5,6)),(2,2,0,(3,2,1)),(4,118,119,(117,118)),(8,114,112,(115,114,113))):
   if C&cs and b[rf]==4*S and not any(b[x]for x in em)and not any(a(x,-S)for x in(kf,em[0],em[1])):m.append(kf|kt<<7)
 return m
def d(m):
 global C,Y,S
 f=m&127;t=m>>7&127;r=m>>14;p=b[f];z=t
 if p==S and t==Y and b[t]==0:z=t-16*S
 e=b[z];U.append((m,e,z,C,Y));b[t]=r*S if r else p;b[f]=0
 if z!=t:b[z]=0
 if p==6*S:
  if abs(t-f)==2:
   rf=t+1-3*(t<f);rt=t-1+2*(t<f);b[rt]=b[rf];b[rf]=0
  G[S]=t
 C&=X.get(f,15)&X.get(t,15);Y=f+16*S if p==S and abs(t-f)==32 else -1;S=-S
def j():
 global C,Y,S
 m,e,z,C,Y=U.pop();S=-S;f=m&127;t=m>>7&127;r=m>>14;p=b[t]
 b[f]=S if r else p;b[t]=0;b[z]=e
 if p==6*S:
  if abs(t-f)==2:
   rf=t-1+2*(t<f);rt=t+1-3*(t<f);b[rt]=b[rf];b[rf]=0
  G[S]=f
def v():
 s=0;w=0;x=0
 for i,p in enumerate(b):
  if p and not i&0x88:
   t=i>>2&60|(i&7)^((i&7)>>2)*7
   if p>0:s+=A[p]+ord(T[p][t^28])-75;w+=p==3
   else:s-=A[-p]+ord(T[-p][t])-75;x+=p==-3
 s+=30*((w>1)-(x>1))
 return s*S
def h(ms,tt,ply):
 ms.sort(key=lambda x:10**7*(x==tt)+10*A[abs(b[x>>7&127])]-A[abs(b[x&127])]+1000*(x==Q[ply]),reverse=True)
def s(l,u,w,ply):
 global n
 n+=1
 if n>L:raise F
 if w<=0:
  st=v()
  if st>=u:return u
  if st>l:l=st
  ms=g(0)if a(G[S],-S)else g(1);tt=0
 else:
  k=tuple(b),S;tt=W.get(k);ms=g()
 h(ms,tt,ply);best=0;bs=-I
 for x in ms:
  d(x)
  if a(G[-S],S):j();continue
  sc=-s(-u,-l,w-1,ply+1);j()
  if sc>=u:
   Q[ply]=x
   return u
  if sc>bs:
   bs=sc;best=x
   if sc>l:l=sc
 if best==0:return -M+ply if a(G[S],-S) else(0 if w>0 else l)
 if w>0:W[k]=best
 return bs if w>0 else l
def m(lg):
 global n
 ms=[q(z[:2])|q(z[2:4])<<7|("nbrq".find(z[4])+2 if len(z)>4 else 0)<<14 for z in lg]
 h(ms,0,0);best=ms[0];n=0;W.clear()
 try:
  for w in range(1,64):
   l=-I;bm=best
   for x in ms:
    d(x)
    if a(G[-S],S):j();continue
    sc=-s(-I,-l,w-1,1);j()
    if sc>l:l=sc;bm=x
   best=bm
   if l>M-1000:raise F
   ms.remove(best);ms.insert(0,best)
 except F:pass
 x=best
 return "abcdefgh"[x&7]+str((x>>4&7)+1)+"abcdefgh"[x>>7&7]+str((x>>11&7)+1)+("nbrq"[(x>>14)-2]if x>>14 else"")
def f(fe):
 global b,S,C,Y,G
 b=[0]*128;ps=fe.split()
 for r,row in enumerate(ps[0].split("/")):
  g=0
  for ch in row:
   if ch.isdigit():g+=int(ch)
   else:b[(7-r)*16+g]=("PNBRQK".find(ch.upper())+1)*((ch<"a")*2-1);g+=1
 S=2*(ps[1]=="w")-1;c=ps[2];C=("K"in c)+2*("Q"in c)+4*("k"in c)+8*("q"in c)
 Y=q(ps[3])if ps[3]!="-"else -1;G={1:b.index(6),-1:b.index(-6)}
def t(pa,bo):return J.load(r.urlopen(r.Request(V+pa,data=J.dumps(bo).encode())))
while 1:
 e=t("/game",{});y=e["status"]
 if y=="done":break
 if y=="your_move":
  f(e["fen"]);e=t("/move",{"game":e["game"],"move":m(e["legal_moves"])})
