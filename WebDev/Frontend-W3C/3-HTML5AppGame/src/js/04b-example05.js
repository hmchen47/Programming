// Instanciate the template
var t = document.querySelector('#mytemplate');

// Create a root node under our H1 title
var host = document.querySelector('#withShadowDom');

const shadowRoot = host.attachShadow({mode: 'open'});
  
// insert something into the shadow DOM, this will be rendered
shadowRoot.appendChild(document.importNode(t.content, true)); 

