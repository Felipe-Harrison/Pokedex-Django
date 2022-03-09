function renderCard(){

    var card = document.querySelector(".description");  
    var nome = document.querySelector(".pokemonName").value;
    var numero = document.querySelector(".pokemonID").value;
    var tipos = document.querySelectorAll("input:checked")
    
    card.innerHTML = `
            
                        <span class="pokemon-id">#${numero}</span>
                        <h1 class="pokemon-name">${nome}</h1>
                        <div class = "pokemon-types">
                            
                        </div>
            
    `;
    var tiposDiv = document.querySelector(".pokemon-types");
    for(var i = 0; i < tipos.length; i++){
        if(i < 2){
            tiposDiv.innerHTML += `<span class="pokemon-type-style pokemon-type-${tipos[i].value}">${tipos[i].value}</span>`
        }
    }
}
    
function previewFile() {
    var preview = document.querySelector('.pokemon-imagem');
    var file    = document.querySelector('.pokemonUrl').files[0];
    var reader  = new FileReader();
    
    console.log(preview,file,reader);

    reader.onloadend = function () {
        preview.src = reader.result;
    }
    
    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}
    
function checklimit(){
    let limit = 2
    
    num_checked = document.querySelectorAll("input:checked")
    console.log(num_checked.length)
    if(num_checked.length === limit){
        num_unchecked = document.querySelectorAll("input[type=checkbox]")
        for (input in num_checked){
            console.log(input.checked)
            if (input.checked == false){
                input.disabled
            }
        }
    }
}

// Mapear todos os tipos disponiveis

    var tipos = [
        {nome:"fire"},
        {nome:"water"},
        {nome:"bug"},
        {nome:"grass"},
        {nome:"poison"},
        {nome:"flying"},
        {nome:"normal"},
        {nome:"eletric"},
        {nome:"ground"},
        {nome:"fairy"},
        {nome:"fighting"},
        {nome:"psychic"},
        {nome:"rock"},
        {nome:"stell"},
        {nome:"ice"},
        {nome:"ghost"},
        {nome:"dragon"},
    ]
    
    var tipos_campo = document.querySelector(".lista-tipos")
    var tipos_atuais = document.querySelector(".tipos")

    var tipos_selecionado = []
    if(tipos_atuais != null){
        var separar = tipos_atuais.value
        tipos_selecionado = separar.split(" ")
    }

    var index = 0;
    
    for(var i = 0; i < tipos.length/5;i++){
        for(var j = 0; j < 5;j++){
            if(tipos_selecionado[0] == tipos[index].nome || tipos_selecionado[1] == tipos[index].nome ){
                tipos_campo.innerHTML += 
            `
                <li>
                    <input type = "checkbox" class = " pokemon-type" name = "pokemon-type" value="${tipos[index].nome}" checked onclick="renderCard()">
                    <label for = "type">${tipos[index].nome}</label>
                </li>
            `
            }else{
            tipos_campo.innerHTML += 
                `
                    <li>
                        <input type = "checkbox" class = "pokemon-type" name = "pokemon-type" value="${tipos[index].nome}" onclick="renderCard()">
                        <label for = "type">${tipos[index].nome}</label>
                    </li>
                `
            }
            index++;
            if(index == tipos.length){
                break;
            }
        }
}

    // Mapeando todos os elementos que estão em um array  e colacando em HTML
    // tipos_campo.innerHTML = tipos.map(tipo =>
    //     `
    //     <li>
    //         <input type = "checkbox" class = "pokemon-type" name = "pokemon-type" value="${tipo.nome}" onclick="renderCard()">
    //         <label for = "type">${tipo.nome}</label>
    //     </li>
    //     `
    //     ).join('')
    
    
    