document.addEventListener('DOMContentLoaded', function(){
    eliminarProducto();
});

function generarAlerta(mensaje,tipo){
    if(document.querySelector('#contenedorAlerta')){
        const alertas = document.querySelector('#contenedorAlerta');
        if(alertas.firstChild) {
            return;
        }
        const h2 = document.createElement('H2');
        h2.textContent = mensaje;
        h2.classList.add('alert')
        if(tipo === 0){
            h2.classList.add('alert-danger');
        }else if(tipo === 1){
            h2.classList.add('alert-success');
        }
        console.log(h2);
        alertas.insertAdjacentElement('beforeend',h2);

        setTimeout( () => {
            h2.remove();
        }, 2000);
    }
}


function eliminarDatosAntiguos(){
    if(document.querySelector('#contenedorProductos')){
        const listado = document.querySelector('#contenedorProductos');
        while(listado.firstChild){
            listado.removeChild(listado.firstChild);
        }
    }
}


function eliminarProducto(){
    if(document.querySelectorAll('.eliminarProductos')[0]){
        const iconosEliminar = document.querySelectorAll('.eliminarProductos');
        iconosEliminar.forEach(icono =>{
            icono.addEventListener('click', e =>{
                e.preventDefault();
                id = icono.dataset.eliminar;
                url = `http://localhost:8000/producto/eliminar/${id}/`;
                fetch(url,{
                    method: 'GET',
                    headers: {},
                }).then(respuesta=>{
                    return respuesta.json();
                }).then(datos =>{
                    if(datos.status === "ok"){
                        //console.log("Producto Eliminada");
                        eliminarDatosAntiguos();
                        cargarlistado(datos.message,1);
                    }else if(datos.status === "error"){
                        console.log("error");
                        generarAlerta(datos.message,0);
                    }
                }).catch(error =>{
                    console.log(error);
                })
            });
        });
    }
}

async function cargarlistado(mensaje,tipo){
    try {
        url = "http://localhost:8000/producto/listadoJson/";
        const resultado = await fetch(url);
        const datos = await resultado.json();
        //Evitar error
        if(!datos.status){
            datos.productos.forEach(producto =>{
                htmlDatos = crearHtmlDAtos(producto);
                if(document.querySelector('#contenedorProductos')){
                    const listado = document.querySelector('#contenedorProductos');
                    listado.append(htmlDatos);
                }
            });
            generarAlerta(mensaje,tipo);
            eliminarProducto();
        }else if(datos.status === "error"){
            console.log("error");
            generarAlerta(datos.message,0);
        }
    } catch (error) {
        console.log(error);
    }
}

function crearHtmlDAtos({id,nombre,descripcion,precio,cantidad,imagen,subcategoria}){
    const divCard = document.createElement('DIV');
    divCard.classList.add('producto__card');
    divCard.classList.add('animate__animated');
    divCard.classList.add('animate__fadeInUp');

    // Div opciones
    const divHeader = document.createElement('DIV');
    divHeader.classList.add('producto__header');

    const divCategoria = document.createElement('DIV');
    divCategoria.classList.add('producto__categoria');

    const textSubcategoria = document.createElement('H3');
    textSubcategoria.textContent = `${subcategoria}`;
    divCategoria.appendChild(textSubcategoria);
    divHeader.appendChild(divCategoria);

    const divOpciones = document.createElement('DIV');
    divOpciones.classList.add('producto__opciones');

    const divOpcionEditar = document.createElement('DIV');
    const aOpcionEditar = document.createElement('A');
    aOpcionEditar.href= `/producto/editar/${id}/`;
    aOpcionEditar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-edit" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#00abfb" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
        <path d="M9 7h-3a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-3" />
        <path d="M9 15h3l8.5 -8.5a1.5 1.5 0 0 0 -3 -3l-8.5 8.5v3" />
        <line x1="16" y1="5" x2="19" y2="8" />
    </svg>`;
    divOpcionEditar.appendChild(aOpcionEditar);

    const divOpcionEliminar = document.createElement('DIV');
    const aOpcionEliminar = document.createElement('A');
    aOpcionEliminar.classList.add("eliminarProductos");
    aOpcionEliminar.dataset.eliminar = id;
    aOpcionEliminar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ff2825" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <line x1="4" y1="7" x2="20" y2="7" />
    <line x1="10" y1="11" x2="10" y2="17" />
    <line x1="14" y1="11" x2="14" y2="17" />
    <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
    <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
    </svg>`;
    divOpcionEliminar.appendChild(aOpcionEliminar);

    divOpciones.appendChild(divOpcionEditar);
    divOpciones.appendChild(divOpcionEliminar);

    divHeader.appendChild(divOpciones);
    // Div Body
    const divBody = document.createElement('DIV');
    divBody.classList.add('producto__body');
    const divImg = document.createElement('DIV');
    divImg.classList.add('producto__img');

    const img = document.createElement('IMG');
    (imagen.length > 0) ? img.src=`/media/${imagen}` : img.src="/static/img/logo.png";
    
    divImg.appendChild(img)


    const divText = document.createElement('DIV');
    divText.classList.add('producto__text');

    const h2 = document.createElement('H2');
    h2.textContent = `${nombre}`;
    
    const pDescripcion = document.createElement('P');
    pDescripcion.textContent = `Descripcion: ${descripcion}`;
    
    const pPrecio = document.createElement('P');
    pPrecio.textContent = `Precio: $ ${precio}`;
    
    const pCantidad = document.createElement('P');
    pCantidad.textContent = `Cantidad: ${cantidad}`;

    divText.appendChild(h2);
    divText.appendChild(pDescripcion);
    divText.appendChild(pPrecio);
    divText.appendChild(pCantidad);
    
    divBody.appendChild(divImg);
    divBody.appendChild(divText);


    // Div card
    divCard.appendChild(divHeader);
    divCard.appendChild(divBody);

    return divCard;
}
