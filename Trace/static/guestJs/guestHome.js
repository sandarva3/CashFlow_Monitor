var itemsArray = JSON.parse(localStorage.getItem("guestItems"));

itemsArray.sort(function (a, b) {
  return new Date(a.date) - new Date(b.date);
});

itemsArray.forEach(function (item, index) {
  var row = document.createElement("tr");
  var dateCell = document.createElement("td");
  var purchasedCell = document.createElement("td");
  var wastedCell = document.createElement("td");
  var notCell = document.createElement("td");
  var savedCell = document.createElement("td");
  var deleteCell = document.createElement("td");

  dateCell.innerHTML = formatDate(item.date);
  purchasedCell.innerHTML = item.purchased;
  wastedCell.innerHTML = item.wasted;
  notCell.innerHTML = item.not;
  savedCell.innerHTML = item.saved;
  deleteCell.innerHTML =
    '<i class="material-icons" id="icon" title="Delete Row" onclick="deleteItem(' +
    index +
    ')">delete</i>';

  dateCell.classList.add("date");
  purchasedCell.classList.add("wasted");
  wastedCell.classList.add("wasted");
  notCell.classList.add("saved");
  savedCell.classList.add("saved");
  deleteCell.classList.add("cell");

  purchasedCell.style = "border-right: 1px dotted black;";
  wastedCell.id = "third";
  notCell.style = "border-right: 1px dotted black;";
  deleteCell.style = "cursor: pointer;";

  row.appendChild(dateCell);
  row.appendChild(purchasedCell);
  row.appendChild(wastedCell);
  row.appendChild(notCell);
  row.appendChild(savedCell);
  row.appendChild(deleteCell);

  document.getElementById("guest-items").appendChild(row);
});

var wastedCells = document.getElementsByClassName("wasted");
var totalWasted = 0;

for (var i = 0; i < wastedCells.length; i++) {
  var wastedValue = Number(wastedCells[i].innerHTML);

  if (!isNaN(wastedValue)) {
    totalWasted += wastedValue;
  }
}

var totalWastedCell = document.getElementById("total-wasted");

totalWastedCell.innerHTML = "Total Amount: " + totalWasted;

var savedCells = document.getElementsByClassName("saved");
var totalSaved = 0;
for (var i = 0; i < savedCells.length; i++) {
  var savedValue = Number(savedCells[i].innerHTML);
  if (!isNaN(savedValue)) {
    totalSaved += savedValue;
  }
}
var totalSavedCell = document.getElementById("total-saved");
totalSavedCell.innerHTML = "Total Amount: " + totalSaved;
