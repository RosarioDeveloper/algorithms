
// Given an interger value, generate the fibonacci sequence
function finbonacci(value) {
   let count = 0;
   let curr = 1;

   let ans = [0]

   for (let i = 0; i < value; i++) {
      curr = count + curr;
      ans.push(curr)
      count = ans[ans.length - 2]
   }

   return ans;
}

const result = finbonacci(59);
console.log(result)
