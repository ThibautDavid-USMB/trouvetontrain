function dollar(prix) {
    var prix = parseFloat(document.getElementById("prixref").innerHTML)
    prix = prix * 1.09
    document.getElementById(prix).innerHTML =  prix
}

function livre(prix) {
    document.getElementById(prix).innerHTML = parseFloat(document.getElementById("prixref").innerHTML) * 0.87
}

function euro(prix) {
    document.getElementById(prix).innerHTML = parseFloat(document.getElementById("prixref").innerHTML)
}