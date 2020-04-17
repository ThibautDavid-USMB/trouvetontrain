function dollar(distance,prix,devise) {
  var dist = document.getElementById(distance).innerHTML;
  dist = dist.replace(",",".")
  dist = dist.substring(0,dist.length -3);

  const request = new XMLHttpRequest();
  const url='http://localhost:5000/prix?distance='+dist+'&devise=dollar';
  
  request.onreadystatechange = function(){
    document.getElementById(prix).innerHTML = JSON.parse(this.responseText);
  }

  request.open("GET", url, true);
  request.send();
  document.getElementById(devise).innerHTML = "$"
}

function livre(distance,prix,devise) {
  var dist = document.getElementById(distance).innerHTML;
  dist = dist.replace(",",".")
  dist = dist.substring(0,dist.length -3);

  const request = new XMLHttpRequest();
  const url='http://localhost:5000/prix?distance='+dist+'&devise=livre';
  
  request.onreadystatechange = function(){
    document.getElementById(prix).innerHTML = JSON.parse(this.responseText);
  }

  request.open("GET", url, true);
  request.send();
  document.getElementById(devise).innerHTML = "£"
}

function euro(distance, prix,devise) {
  var dist = document.getElementById(distance).innerHTML;
  dist = dist.replace(",",".")
  dist = parseFloat(dist.substring(0,dist.length -3));

  var request = new XMLHttpRequest();
  var url="http://localhost:5000/prix?distance="+dist+"&devise=euro";

  request.onreadystatechange = function(){
    document.getElementById(prix).innerHTML = JSON.parse(this.responseText);
  }

  request.open("GET", url, true);
  request.send();
  document.getElementById(devise).innerHTML = "€"
}