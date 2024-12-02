function minimumLoss(prices: number[]) {
   const indexedPrices = prices.map((price, index) => [price, index]);

   indexedPrices.sort((a, b) => a[0] - b[0]);
   let minLoss = Infinity;

   for (let i = 1; i < indexedPrices.length; i++) {
      const [currentPrice, currentIndex] = indexedPrices[i];
      const [previousPrice, previousIndex] = indexedPrices[i - 1];

      if (currentIndex < previousIndex) {
         const loss = currentPrice - previousPrice;
         if (loss < minLoss) {
            minLoss = loss;
         }
      }
   }

   return minLoss;

}

const result = minimumLoss([5,10,3])
console.log(result)
