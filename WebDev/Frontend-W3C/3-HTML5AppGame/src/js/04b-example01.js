function instantiate() {
    var t = document.querySelector('#mytemplate');
      
    // Populate the src at runtime.
    t.content.querySelector('img').src = 'http://webcomponents.github.io/img/logo.svg';

      // clone template content
    var clone = document.importNode(t.content, true);
      
      // add it to the body of the HTML document
    document.body.appendChild(clone); 
}

