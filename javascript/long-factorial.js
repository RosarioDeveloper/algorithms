function factorial(n) {
   let result = BigInt(1)

   if (n === 0 || n === 1) {
      console.log(result.toString())
      return
   }

   for (let i = 2; i <= n; i++) {
      result *= BigInt(i)
   }

   console.log(result.toString())
}

factorial(100)
