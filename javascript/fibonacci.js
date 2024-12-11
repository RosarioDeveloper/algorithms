// Given an interger value, generate the fibonacci sequence
function finbonacci(value) {
   let fib = [0, 1];
   let negFib = [];

   for (let i = 2; i <= Math.abs(value); i++) {
      fib.push(fib[i - 1] + fib[i - 2]);
   }

   if(value < 0){
      for (let i = Math.abs(value); i >= 0; i--) {
         negFib.push((-1) ** (i + 1) * fib[i]);
      }
   }
   
   return [...negFib, ...fib];
}

const result = finbonacci(5);
console.log(result);

// Positive: F(5) = f[n - 1] + f[n - 2]
// Nagative: F(-n) = (-1)ˆn+1 * f[n]
