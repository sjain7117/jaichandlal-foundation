import sys
S="/private/tmp/claude-501/-Users-sahiljain-trust/09978835-b0ed-4e2a-bc71-ddcc56756797/scratchpad/"
h=open("_source/index.template.html").read()
imgs={"LOGO":"logo","ARCH":"arch","KIDSL":"kidsL","KIDSR":"kidsR","HERO":"hero"}
b={k:"data:image/jpeg;base64,"+open(S+v+".b64").read() for k,v in imgs.items()}
for k,v in b.items(): h=h.replace("{{%s}}"%k, v)
h=h.replace("--radius:14px;", "--radius:14px;\n  --photo-hero:url(\"%s\");" % b["HERO"], 1)
assert "{{" not in h
open("index.html","w").write(h)
inj="""<script>
(function(){var m=location.search.match(/s=(\\d+)/);if(!m)return;var i=+m[1];
[].slice.call(document.querySelectorAll('main > section, footer')).forEach(function(n,j){if(j!==i)n.style.display='none';});
document.querySelectorAll('.rv').forEach(function(e){e.classList.add('in');e.style.transition='none';});
document.querySelectorAll('[data-count]').forEach(function(e){e.textContent=e.dataset.count+e.dataset.suffix;});
})();
(function(){if(/menu=1/.test(location.search)){var p=document.getElementById('mobilenav');p.classList.add('is-open');p.style.transition='none';}})();
(function(){if(!/diag=1/.test(location.search))return;
var errs=[];window.addEventListener("error",function(e){errs.push("ERROR: "+e.message);});
window.addEventListener("load",function(){setTimeout(function(){
  var vw=document.documentElement.clientWidth, out=[];
  out.push("viewport="+vw+"x"+innerHeight);
  out.push("doc.scrollWidth="+document.documentElement.scrollWidth+" (overflow="+(document.documentElement.scrollWidth>vw)+")");
  var wide=[];
  document.querySelectorAll("body *").forEach(function(el){
    var r=el.getBoundingClientRect();
    if(r.width>vw+1 || r.right>vw+1 || r.left<-1){
      if(getComputedStyle(el).position!=="fixed") wide.push((el.className||el.tagName)+" ["+Math.round(r.left)+".."+Math.round(r.right)+"]");
    }
  });
  out.push("overflowing els="+(wide.length?wide.slice(0,8).join(" | "):"none"));
  var imgs=[].slice.call(document.images);
  out.push("images="+imgs.length+" loaded="+imgs.filter(function(i){return i.complete&&i.naturalWidth>0}).length);
  try{
    out.push("fonts: Marcellus="+document.fonts.check("16px Marcellus")+" Mukta="+document.fonts.check("16px Mukta")+" CourierPrime="+document.fonts.check("16px \'Courier Prime\'"));
  }catch(e){out.push("fonts: n/a");}
  out.push("headerH="+getComputedStyle(document.documentElement).getPropertyValue("--header-h").trim());
  out.push("revealed="+document.querySelectorAll(".rv.in").length+"/"+document.querySelectorAll(".rv").length);
  out.push("js errors="+(errs.length?errs.join(" ;; "):"none"));
  var pre=document.createElement("pre");
  pre.id="diag";
  pre.style.cssText="position:fixed;left:0;top:0;right:0;z-index:100000;background:#111;color:#0f0;font:12px monospace;padding:10px;white-space:pre-wrap;margin:0";
  pre.textContent=out.join(String.fromCharCode(10));
  document.body.appendChild(pre);
},400);});})();

</script>
</body>"""
open("qa.html","w").write(h.replace("</body>",inj,1))
print("built", len(h))
