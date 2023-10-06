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
