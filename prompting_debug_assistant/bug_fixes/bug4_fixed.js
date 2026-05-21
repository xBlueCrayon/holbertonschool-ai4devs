function addPrices(price1, price2) {
    console.log("Price 1:", price1);
    console.log("Price 2:", price2);

    let total = Number(price1) + Number(price2);

    return total;
}

const item1 = "100";
const item2 = 50;

const finalPrice = addPrices(item1, item2);

console.log(finalPrice);