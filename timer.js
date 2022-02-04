let now = new Date()
let millisecTillTime =
  new Date(now.getFullYear(), now.getMonth(), now.getDate(), 07, 45, 0, 0) - now
if (millisecTillTime < 0) {
  millisecTillTime += 86400000 // it's after 07.45am, try 07.45am tomorrow.
}
setTimeout(function () {
  console.log('Hello Peak!')
  alert('Hello Peak!')
}, millisecTillTime)
