window.onload = init();

let myPicturesArray = [
{
"albumId": 1,
"id": 1,
"title": "accusamus beatae ad facilis cum similique qui sunt",
"url": "https://placehold.it/600/92c952",
"thumbnailUrl": "https://placehold.it/150/92c952"
},
{
"albumId": 1,
"id": 2,
"title": "reprehenderit est deserunt velit ipsam",
"url": "https://placehold.it/600/771796",
"thumbnailUrl": "https://placehold.it/150/771796"
},
{
"albumId": 2,
"id": 51,
"title": "non sunt voluptatem placeat consequuntur rem incidunt",
"url": "https://placehold.it/600/8e973b",
"thumbnailUrl": "https://placehold.it/150/8e973b"
},
{
"albumId": 2,
"id": 52,
"title": "eveniet pariatur quia nobis reiciendis laboriosam ea",
"url": "https://placehold.it/600/121fa4",
"thumbnailUrl": "https://placehold.it/150/121fa4"
},
{
"albumId": 3,
"id": 127,
"title": "magnam quia sed aspernatur",
"url": "https://placehold.it/600/74456b",
"thumbnailUrl": "https://placehold.it/150/74456b"
},
{
"albumId": 3,
"id": 128,
"title": "est facere ut nam repellat numquam quia quia eos",
"url": "https://placehold.it/600/b0931d",
"thumbnailUrl": "https://placehold.it/150/b0931d"
}
];

// Display pictures
function init() {

  myPicturesArray.forEach(function(currentImage) {
    let image = document.createElement("img");
    image.src = currentImage.thumbnailUrl;
    image.alt = currentImage.title;
    document.body.append(image);
  });
 

}

