document.addEventListener('DOMContentLoaded', function(){
    eliminarSubcategoria();
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
    if(document.querySelector('.subcategorias-elementos')){
        const listado = document.querySelector('.subcategorias-elementos');
        while(listado.firstChild){
            listado.removeChild(listado.firstChild);
        }
    }
}

function eliminarSubcategoria(){
    if(document.querySelectorAll('.eliminarSubcategoria')[0]){
        const iconosEliminar = document.querySelectorAll('.eliminarSubcategoria');
        iconosEliminar.forEach(icono =>{
            icono.addEventListener('click', e =>{
                e.preventDefault();
                id = icono.dataset.eliminar;
                url = `http://127.0.0.1:8000/subcategoria/eliminar/${id}/`;
                fetch(url,{
                    method: 'GET',
                    headers: {},
                }).then(respuesta=>{
                    return respuesta.json();
                }).then(datos =>{
                    if(datos.status === "ok"){
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
        url = "http://127.0.0.1:8000/subcategoria/listadoJson/";
        const resultado = await fetch(url);
        const datos = await resultado.json();
        //Evitar error
        if(!datos.status){
            datos.subcategorias.forEach(subcategoria =>{
                trDatos = crearTrDAtos(subcategoria);
                if(document.querySelector('.subcategorias-elementos')){
                    const listado = document.querySelector('.subcategorias-elementos');
                    listado.append(trDatos);
                }
            });
            generarAlerta(mensaje,tipo);
            eliminarSubcategoria();
        }else if(datos.status === "error"){
            generarAlerta(datos.message,0);
        }
    } catch (error) {
        console.log(error);
    }
}


function crearTrDAtos({id,nombre,descripcion,categoria}){
    const tr = document.createElement("TR");
    const tdId = document.createElement("TD");
    tdId.textContent = id;
    const tdNombre = document.createElement("TD");
    tdNombre.textContent = nombre;
    const tdDescrip = document.createElement("TD");
    tdDescrip.textContent = descripcion;
    const tdCate = document.createElement("TD");
    tdCate.textContent = categoria;

    const tdOpciones = document.createElement("TD");
    const divActualizar = document.createElement("DIV");
    const divEliminar = document.createElement("DIV");

    const aActualizar = document.createElement("A");
    aActualizar.href= `/subcategoria/editar/${id}/`;
    aActualizar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-edit" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#00abfb" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <path d="M9 7h-3a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-3" />
    <path d="M9 15h3l8.5 -8.5a1.5 1.5 0 0 0 -3 -3l-8.5 8.5v3" />
    <line x1="16" y1="5" x2="19" y2="8" />
</svg>`;
    divActualizar.appendChild(aActualizar);

    const aEliminar = document.createElement("A");
    aEliminar.classList.add("eliminarSubcategoria");
    aEliminar.dataset.eliminar = id;
    aEliminar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ff2825" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <line x1="4" y1="7" x2="20" y2="7" />
    <line x1="10" y1="11" x2="10" y2="17" />
    <line x1="14" y1="11" x2="14" y2="17" />
    <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
    <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
    </svg>`;
    divEliminar.appendChild(aEliminar);

    const divOpciones = document.createElement("DIV");
    divOpciones.classList.add('producto__opciones_2');

    divOpciones.appendChild(divActualizar);
    divOpciones.appendChild(divEliminar);
    tdOpciones.appendChild(divOpciones);

    tr.appendChild(tdId);
    tr.appendChild(tdNombre);
    tr.appendChild(tdDescrip);
    tr.appendChild(tdCate);
    tr.appendChild(tdOpciones);
    return tr;
}