    
    var card = document.querySelector(".description");  
    var nome = document.querySelector(".pokemonName").value;
    var numero = document.querySelector(".pokemonID").value;
    var imagem = document.querySelector(".pokemonUrl");
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
    
    // opção nada esperta

    // switch (tipos.length){
    //     case 0:
    //         card.innerHTML = `
            
    //                     <span class="pokemon-id">#${numero}</span>
    //                     <h1 class="pokemon-name">${nome}</h1>
    //                     <div class = "pokemon-type">
                            
    //                     </div>
            
    //         `
    //         break;
    //     case 1:
    //         card.innerHTML = `
    //         <div>
    //                     <span class="pokemon-id">#${numero}</span>
    //                     <h1 class="pokemon-name">${nome}</h1>
    //                     <div class = "pokemon-type">
    //                         <span class="pokemon-type-${tipos[0].value}">${tipos[0].value}</span>
    //                     </div>
    //         </div>
    //         `
    //         break;
    //     default:
    //         card.innerHTML = `
    //         <div>
    //                     <span class="pokemon-id">#${numero}</span>
    //                     <h1 class="pokemon-name">${nome}</h1>
    //                     <div class = "pokemon-type">
    //                         <span class="pokemon-type-${tipos[0].value}">${tipos[0].value}</span>
    //                         <span class="pokemon-type-${tipos[1].value}">${tipos[1].value}</span>
    //                     </div>
    //         </div>
    //         ` 
    //         break;
    // }
