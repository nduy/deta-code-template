// Welcome to Delta Code template
// which gives you a chance to write, share and learn TypeScript.



const anExampleVariable = "Hello World"

function drawTree(height) {
    for ( var i = 0; i < height ; i++ ) {
        var star = '*';
        var space = ' ';

        for ( var j = 1; j <= i; j++ ) {
            star = star + '**';            
        }
           
        var spacesBefore = space.repeat(height-i-1);
        star = spacesBefore + star;
        console.log(star);
    }
}

console.log(anExampleVariable)
var levels = prompt('How many levels high should be the tree?');

drawTree(levels);

// To learn more about the language, click above in "Examples" or "What's New".
// Otherwise, get started by removing these comments and the world is your playground.
  