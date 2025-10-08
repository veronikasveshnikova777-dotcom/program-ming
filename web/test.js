console.log(5, "string")

// ASCII Art Gallery
console.log("\n🎨 ASCII ART GALLERY 🎨\n");

// Кот
console.log("🐱 Котик:");
console.log(`
    /\\_/\\  
   (  o.o ) 
    > ^ <
`);

// Сова
console.log("🦉 Сова:");
console.log(`
     ,___,
     [O.o]
  ___) (___ 
 /\\   -   /\\
( (.-"""-.) )
 \\\\/\\_/\\_//
  \\'-----'/
`);

// Замок
console.log("🏰 Замок:");
console.log(`
      /\\
     /  \\
    /____\\
   |      |
   | [][]|
   |  __  |
   |_|  |_|
`);

// Дерево
console.log("🌳 Дерево:");
console.log(`
       🍃🍃🍃
     🍃🍃🍃🍃🍃
   🍃🍃🍃🍃🍃🍃🍃
     🍃🍃🍃🍃🍃
       🍃🍃🍃
         |||
         |||
    _____|_____
`);

// Ракета
console.log("🚀 Ракета:");
console.log(`
       /\\
      /  \\
     |    |
     | ** |
     | ** |
     |____|
     /    \\
    /______\\
   /________\\
    ~~~~~~~~
`);

// Домик
console.log("🏠 Домик:");
console.log(`
      /\\  /\\
     /  \\/  \\
    /        \\
   /__________\\
   |  []  []  |
   |    __    |
   |   |  |   |
   |___|__|___|
`);

// Смайлик
console.log("😊 Большой смайлик:");
console.log(`
    @@@@@@@@@@
  @@          @@
 @   @@    @@   @
@               @
@               @
@   @        @   @
@    @@@@@@@@    @
 @              @
  @@          @@
    @@@@@@@@@@
`);

// Звезда
console.log("⭐ Звезда:");
console.log(`
       *
      ***
     *****
    *******
     *****
      ***
   *** *** ***
  ***** *****
   *** *** ***
      ***
     *****
    *******
     *****
      ***
       *
`);

console.log("\n✨ Конец галереи! ✨");
for (let i = 1; i <= 10; i++) {
    console.log(i)
}




function factorial(x) {
    let r = 1n
    for (let i = 1; i <= x; i++) {
        r = r * BigInt(i)
        console.log(i, r.toString())
    }
    console.log("-----------------------")
    return r
}

console.log("aaaaaaaaaaaaaaaaaaaaaaaa")
console.log(factorial(200).toString())

