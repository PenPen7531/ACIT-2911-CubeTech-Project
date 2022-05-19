
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("table-data");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

/* Source: https://www.w3schools.com/howto/howto_js_sort_table.asp */

// Delete Confirm

// const row = document.querySelectorAll("tr")
// row.forEach(element => element.addEventListener('click', getEmpId))

// function getEmpId(ev) {
//    let tr = ev.target.parentNode.parentNode
//    let ids = tr.getElementsByTagName("td")[0].innerHTML
//    console.log(ids)

// }

function deleteConfirm(){
    return confirm(`Are you sure you want to delete Employee`)
}

// Display employee Salary
// function myFunction() {
//   const popup = document.getElementById("myPopup");
//   popup.classList.toggle("show");
// }


function myDropDown() {
  const dropNav = document.getElementById("menu")
  const search = document.querySelector(".search-top")
  const btn = document.querySelector('.icon')
  const btnTwo = document.querySelector('.icon-close')
  btnTwo.style.display = 'block'
  search.style.display = 'none'
  btn.style.display = 'none'
  dropNav.style.display = 'block'
}

function closeDrop() {
  const menu = document.getElementById("menu")
  const btn = document.querySelector('.icon')
  const search = document.querySelector(".search-top")
  menu.style.display = 'none'
  btn.style.display = 'block'
  search.style.display = 'flex'
}


