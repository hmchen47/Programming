// Instanciate the template
var t = document.querySelector('#mytemplate');
 
// Create a root node under our h1 title
var host = document.querySelector('#myWidget');
const shadowRoot = host.attachShadow({mode: 'open'});
 
 
shadowRoot.appendChild(document.importNode(t.content, true));

