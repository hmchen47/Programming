// TIP : use "document.currentScript" here to select
// the "local document", the one corresponding to this page.
// this may avoid problems when multiple WebComponents files
// are inserted in the same document. See below...
var localDoc = document.currentScript.ownerDocument;

class MyWidget extends HTMLElement {
  constructor() {
    super();
    const shadowRoot = this.attachShadow({mode: 'open'});
      
    // instanciate template
    let t = localDoc.querySelector('#mytemplate');
    // add it to the shadow DOM
      
    shadowRoot.appendChild(document.importNode(t.content, true));
  }
}

try {
  // Define the custom element to the browser
  customElements.define('my-widget', MyWidget);
  console.log("Element defined");
} catch (error) {
  console.log(error);
}

