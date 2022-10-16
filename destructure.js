const myObject = {
    name: "John Smith",
    age: 38,
    portfolio: ["AMZN", "AAPL", "GOOG", "LCID"]
}

const portfolio = myObject.portfolio;

const first = portfolio[0];
const third = portfolio[2];
const fourth = portfolio[3];

console.log(first, third, fourth);

