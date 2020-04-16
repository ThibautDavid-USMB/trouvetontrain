function dollar(prix) {
    document.getElementById(prix).innerHTML = parseFloat(document.getElementById("prixref").innerHTML) * 1.10
}

function livre(prix) {
    document.getElementById(prix).innerHTML = parseFloat(document.getElementById("prixref").innerHTML) * 0.87
}

function euro(prix) {
    document.getElementById(prix).innerHTML = parseFloat(document.getElementById("prixref").innerHTML)
}