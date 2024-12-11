
// Given an interger value, generate the fibonacci sequence
function finbonacci(value) {
   let fib = [0, 1]

   for (let i = 2; i < value; i++) {
      fib.push(fib[i -1 ] + fib[i - 2])
   }

   return fib;
}

const result = finbonacci(59);
console.log(result)
