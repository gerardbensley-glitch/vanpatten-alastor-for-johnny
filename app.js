
const money = n => n == null ? "Request price" : new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(n);
async function loadJSON(path){const r=await fetch(path);if(!r.ok)throw new Error("Could not load "+path);return r.json()}
const menu=document.getElementById("menuToggle"),nav=document.getElementById("primaryNav");
if(menu&&nav){menu.addEventListener("click",()=>{const open=nav.classList.toggle("open");menu.setAttribute("aria-expanded",String(open));menu.setAttribute("aria-label",open?"Close navigation":"Open navigation")});nav.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.classList.remove("open");menu.setAttribute("aria-expanded","false")}))}
const toast=document.getElementById("toast");function showToast(m){if(!toast)return;toast.textContent=m;toast.classList.add("show");setTimeout(()=>toast.classList.remove("show"),4200)}
const year=document.getElementById("year");if(year)year.textContent=new Date().getFullYear();
if(document.getElementById("productGrid")){
  Promise.all([loadJSON("products.json"),loadJSON("brands.json")]).then(([products,brands])=>{
    const grid=document.getElementById("productGrid"),dept=document.getElementById("productDepartment"),tier=document.getElementById("productTier"),search=document.getElementById("productSearch");
    [...new Set(products.map(p=>p.dept))].sort().forEach(d=>{const o=document.createElement("option");o.value=d;o.textContent=d;dept.appendChild(o)});
    function render(){
      const q=search.value.trim().toLowerCase(),d=dept.value,t=tier.value;
      const list=products.filter(p=>(d==="all"||p.dept===d)&&(t==="all"||p.tier===t)&&[p.name,p.brand,p.dept,p.variant,p.tier].join(" ").toLowerCase().includes(q));
      document.getElementById("productCount").textContent=`Showing ${list.length} of ${products.length} selected product references`;
      grid.innerHTML=list.map(p=>{const priceSection=p.essentialPrice?`<div class="price-pair"><div class="price-line"><span>Brand price</span><strong>${money(p.brandPrice)}</strong></div><div class="price-line house"><span>Signature*</span><strong>${money(p.housePrice)}</strong></div><div class="price-line essential"><span>Essential*</span><strong>${money(p.essentialPrice)}</strong></div></div>`:`<div class="price-pair"><div class="price-line"><span>Brand price</span><strong>${money(p.brandPrice)}</strong></div><div class="price-line house"><span>VPA house price*</span><strong>${money(p.housePrice)}</strong></div></div>`;return`<article class="product-card"><div class="product-image"><img src="${p.image}" alt="${p.brand} ${p.name}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null;this.src='assets/van-patten-alastor-crest.png';this.style.maxWidth='58%';this.style.objectFit='contain'"></div><div class="product-copy"><span class="product-brand">${p.brand} · ${p.tier}</span><h3>${p.name}</h3><div class="product-variant">${p.variant}</div>${priceSection}<p class="product-note">${p.note}</p><a class="product-link" href="${p.url}" target="_blank" rel="noopener">View original brand listing ↗</a></div></article>`}).join("");
    }
    [search,dept,tier].forEach(el=>el.addEventListener("input",render));
    document.getElementById("resetProducts").addEventListener("click",()=>{search.value="";dept.value="all";tier.value="all";render()});
    const dir=document.getElementById("brandDirectory");
    dir.innerHTML=Object.entries(brands).map(([name,groups])=>`<article class="brand-group"><h3>${name}</h3>${Object.entries(groups).map(([tier,txt])=>`<p><strong>${tier}</strong><br>${txt}</p>`).join("")}</article>`).join("");
    render();
  }).catch(e=>{document.getElementById("productGrid").innerHTML="<p>Catalogue data could not be loaded. Open the site through a local web server rather than directly from the file system.</p>";});
}
const form=document.getElementById("clientBrief");
if(form){
  const params=new URLSearchParams(location.search);
  if(params.get("persona"))form.elements.persona.value=params.get("persona");
  if(params.get("package"))form.elements.package.value=params.get("package");
  form.addEventListener("submit",async e=>{
    e.preventDefault();if(!form.reportValidity())return;
    const d=new FormData(form);
    const brief=["VAN PATTEN-ALASTOR — PRIVATE CLIENT ENQUIRY",`Name: ${d.get("name")}`,`Email: ${d.get("email")}`,`Direction: ${d.get("persona")||"Not specified"}`,`Programme: ${d.get("package")||"Not specified"}`,`Budget: ${d.get("budget")||"Prefer to discuss"}`,`Areas: ${d.getAll("interests").join(", ")||"Not specified"}`,`Project: ${d.get("message")||"Not provided"}`].join("\n");
    try{await navigator.clipboard.writeText(brief);document.getElementById("formStatus").textContent="Your brief has been copied. It has not been transmitted or stored by Van Patten-Alastor. Connect a secure form endpoint before launch.";showToast("Brief copied locally. Nothing was sent.");}
    catch(err){document.getElementById("formStatus").textContent="Clipboard access was unavailable. No information was transmitted. Please copy your details manually.";showToast("Clipboard unavailable.");}
  });
}
const observerOptions={threshold:.1,rootMargin:"0px 0px -50px 0px"};
const observer=new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
},observerOptions);
document.querySelectorAll(".fade-in, .fade-in-left, .fade-in-right").forEach(el=>observer.observe(el));
