(function(e,t){
    function r(e){
        var t=null;
    
        if(e.firstChild.nodeName!="#text"){
            return e.firstChild;}
        else{
            e=e.firstChild;
        do{
            e=e.nextSibling;
        }
            
        while(e&&e.nodeName=="#text");  
            return e||null;
    }
  }
  
function i(e){
  var t=e.nodeName.toUpperCase();
  
  if(t=="DETAILS"){
    return false;
  }
  else if(t=="SUMMARY"){
    return true;
  }
  else {
    return i(e.parentNode);
    }
}

function s(e){
    var n=e.type=="keypress",r=e.target||e.srcElement;
    
    if(n||i(r)){
        if(n){
            n=e.which||e.keyCode;if(n==32||n==13){}else{
                return;
            }
        }
    
        var s=this.getAttribute("open");
    
        if(s===null){
            this.setAttribute("open","open");
        } else {
            this.removeAttribute("open");
        } setTimeout(function(){
            t.body.className=t.body.className;
        },13);
    
        if(n){
            e.preventDefault&&e.preventDefault();return false;
        }
    }
}

function o(){
    var e=t.createElement("style"),n=t.getElementsByTagName("head")[0],r=e.innerText===undefined?"textContent":"innerText";var i=["details{display: block;}","details > *{display: none;}","details.open > *{display: block;}","details[open] > *{display: block;}","details > summary:first-child{display: block;cursor: pointer;}",'summary:before{content: "▶ ";}',"details[open]{display: block;}"];
    
    f=i.length;e[r]=i.join("\n");
    
    n.insertBefore(e,n.firstChild);
}

if("open"in t.createElement("details"))
    return;
    
var n=function(){
    if(t.addEventListener){
        return function(t,r,i){
            if(t&&t.nodeName||t===e){
                t.addEventListener(r,i,false);
            }else if(t&&t.length){
                for(var s=0;s<t.length;s++){
                    n(t[s],r,i);
                }
            }
        };
    } else {
        return function(t,r,i){
            if(t&&t.nodeName||t===e){
                t.attachEvent("on"+r,function(){
                    return i.call(t,e.event);
                });
            } else if(t&&t.length){
                for(var s=0;s<t.length;s++){
                    n(t[s],r,i);
                }
            }
        };
    }
}();

var u=t. getElementsByTagName("details"), a, f=u.length, l, c=null, h=t.createElement("summary");

h.appendChild(t.createTextNode("Details"));

while(f--){
    c=r(u[f]);
    
    if(c!=null&&c.nodeName.toUpperCase()=="SUMMARY"){
    }else{
        c=t.createElement("summary");
        c.appendChild(t.createTextNode("Details"));
        
        if(u[f].firstChild){
            u[f].insertBefore(c,u[f].firstChild);
        } else {
            u[f].appendChild(c);
        }
    }
    
    l=u[f].childNodes.length;
    while(l--){
        if(u[f].childNodes[l].nodeName==="#text"&&(u[f].childNodes[l].nodeValue||"").replace(/\s/g,"").length){
            a=t.createElement("text");a.appendChild(u[f].childNodes[l]);u[f].insertBefore(a,u[f].childNodes[l]);
        }
    }
    
    c.legend=true;
    c.tabIndex=0;
}

t.createElement("details");n(u,"click",s);n(u,"keypress",s);o();

})(window,document);