//"objects literals" or "singleton objects"
let js1 = {
    courseName: 'JavaScript intro',
    weeks: 5,
    madeBy: 'W3Cx',
    author: 'Michel Buffa' // no "," after the last property!, 
                           // even if ES5/6 accept it
}

// js1.author, js1.weeks

let darkVador1AsAnArray = ['villain', 'half human half machine'];
// darkVador1AsAnArray[0]
// darkVador1AsAnArray[1]

let darkVadorAsAnObject = {
    job: 'villain',
    race: 'half human half machine'
};

// Between the two darkVador versions, instead of '[' and ']' that we used for 
// defining an array, we use '{' and '}' for defining an object
// The elements of the object (its properties) are separated by a comma ','
// The pairs of keys/values are separated by ':' as in race: 'half human, half machine'
// The last pair of keys/values has no ',' at the end.
// It is possible to access the object's properties with "." or with brackets

let book = {
   title: 'Le Petit Prince',
   author: 'Saint-Exupery'
};

//var title = book.title;
// var title = book['title'];
// the two are the same
// var author = book['author'];

// In JavaScript, objects are arrays whose indexes are property names: please remember this!


// Property declaration syntax
let louis = {age: 40}; // WE DO THIS MOST OF THE TIME!
//let louis = {"age": 40}; // The JSON (module 5) format uses systematically this syntax
//let louis = {'age': 40};

// Properties that start with a number of have space in their name

// book.1stPublication = '6 avril 1943'; // begins with a number
                                      // Throws a SyntaxError
book['1stPublication'] = '6 avril 1943'; // OK
// book.date of publication = '6 avril 1943'; // spaces not allowed!
book['date of publication'] = '6 avril 1943'; // allowed, but avoid!

// Properties whose name is in a variable 
let key = 'title';
 
//book[key];


// An object can contain another object 
 let book2 = {
    name: 'Catch-22',
    published: 1961,
    author: {                 // embedded object!
        givenName: 'Joseph',
        familyName: 'Heller'
    }
};

