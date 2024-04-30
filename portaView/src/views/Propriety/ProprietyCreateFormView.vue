<template>
    <div class="decoration-line"></div>
    <body>
    <form action="#" name="solucionFormulario">
    <!-- ######### Seccion de fechas ######## -->
    <section>
    <h3>Fechas</h3>      
	<label for="fechaInicio">Fecha Inicio:</label>
	<input type="date" id="fechaInicio" name="fechaInicio" v-model="fechaInicio">

	<label for="fechaFin">Fecha Fín:</label>
	<input type="date" id="fechaFin" name="fechaFin" v-model="fechaFin">
    </section>
    
     <!-- ######### seccion de informacion de la propiedad ######## -->
    <section>
    <h3>Información de la propiedad:</h3>      
	<label for="titulo">Título:</label>
	<input type="text" id="titulo" name="titulo" placeholder="Escribe el título de la propiedad" maxlength="80" v-model="titulo">

	<label for="comentario">Comentario:</label>
	<textarea name="comentario" id="comentario" maxlength="800" v-model="comentario"></textarea>

    <select name="tipoVivienda" id="tipoVivienda" v-model="tipoVivienda">
      <option value="Departamento">Departamento</option>
      <option value="Vivienda">Vivienda</option>
    </select>

    <label for="usoActual">Uso Actual:</label>
	<input type="text" id="usoActual" name="usoActual" placeholder="Escribe el uso actual de la propiedad" maxlength="80" v-model="usoActual">

    <label for="usoPermitido">Uso Permitido:</label>
	<input type="text" id="usoPermitido" name="usoPermitido" placeholder="Escribe el uso permitido de la propiedad" maxlength="80" v-model="usoPermitido">

    <label for="condicionFísica">Condición Física:</label>
	<textarea name="comentario" id="comentario" maxlength="800" v-model="condicionFisica"></textarea>

    <label for="claseInmueble">Clase de Inmueble:</label>
	<input type="text" id="claseInmueble" name="claseInmueble" placeholder="Escribe la clase de inmueble de la propiedad" maxlength="80" v-model="claseInmubele">

    <label for="numeroFrentes">Número de Frentes:</label>
	<input type="number" id="numeroFrentes" name="numeroFrentes" v-model="numeroFrentes">

    <label for="medidaTerreno">Medida del Terreno:</label>
	<input type="text" id="medidaTerreno" name="medidaTerreno" placeholder="Escribe la medida de la propiedad" maxlength="80" v-model="medidaTerreno">

    <label for="m2Terreno">M2 del Terreno:</label>
	<input type="text" id="m2Terreno" name="m2Terreno" placeholder="Escribe los m2 de la propiedad" maxlength="80" v-model="m2Terreno">

    <label for="construccionN1">Construccion N1:</label>
	<input type="text" id="construccionN1" name="construccionN1" placeholder="8" maxlength="80" v-model="construccionN1">

    <label for="construccionN2">Construccion N2:</label>
	<input type="text" id="construccionN2" name="construccionN2" placeholder="8" maxlength="80" v-model="construccionN2">
    
    <label for="construccionN3">Construccion N3:</label>
	<input type="text" id="construccionN3" name="construccionN3" placeholder="8" maxlength="80" v-model="construccionN3">

    <label for="gravamen">Gravamen:</label>
	<input type="text" id="gravamen" name="gravamen" placeholder="8" maxlength="80" v-model="gravamen">
     <!-- ######### En duda ######## -->
    <label for="valorGravamen">Valor de Gravamen:</label>
	<input type="text" id="valorGravamen" name="valorGravamen" placeholder="Escribe el valor del gravamen" maxlength="80" v-model="valorGravamen">

    <label for="valorAvaluo">Valor segun Avaúo:</label>
	<input type="text" id="valorAvaluo" name="valorAvaluo" placeholder="Escribe el valor segun avalúo" maxlength="80" v-model="valorAvaluo">

    <label for="operacion">Operación:</label>
	<input type="text" id="operacion" name="operacion" placeholder="Escribe la operacion" maxlength="80" v-modeol="operacion">

    <label for="condicionPago">Condición de Pago:</label>
	<input type="text" id="condicionPago" name="condicionPago" placeholder="Escribe la condición de pago" maxlength="80" v-model="condicionPago">

    <label for="escrituracion">Escrituración:</label>
	<input type="text" id="condicionPago" name="condicionPago" placeholder="Escribe la escrituración" maxlength="80" v-model="escrituracion">

    <label for="avaluo">Avalúo:</label>
	<input type="text" id="avaluo" name="avaluo" placeholder="Escribe el avalúo de la propiedad" maxlength="80"v-model="avaluo">

    <label for="impuestos">Impuestos:</label>
	<input type="text" id="impuestos" name="impuestos" placeholder="Escribe el avalúo de la propiedad" maxlength="80" v-model="impuestos">

    <label for="otros">Otros:</label>
	<textarea name="otros" id="otros" maxlength="400" v-model="otros"></textarea>

    <label for="total">Total:</label>
	<input type="text" id="total" name="total" placeholder="Escribe el avalúo de la propiedad" maxlength="80" v-model="total">
    </section>
    
    <!-- ######### seccion de precios y comisiones ######## -->
    <section>
    <h3>Precios y comisiones</h3>
    <label for="precioVenta">Precio de  Venta:</label>
	<input type="text" id="precioVenta" name="precioVenta" placeholder="Escribe el precio de venta de la propiedad" maxlength="80" v-model="precioVenta">

    <label for="precioRenta">Precio de Renta:</label>
	<input type="text" id="precioRenta" name="precioRenta" placeholder="Escribe el precio de renta de la propiedad" maxlength="80"v-model="precioRenta">

    <label for="precioMinimo">Precio Minimo:</label>
	<input type="text" id="precioMinimo" name="precioMinimo" placeholder="Escribe el precio minimo de la propiedad" maxlength="80" v-model="precioMinimo">

    <label for="precioPromedio">Precio Promedio:</label>
	<input type="text" id="precioPromedio" name="precioPromedio" placeholder="Escribe el precio promedio de la propiedad" maxlength="80" v-model="precioPromedio">

    <label for="precioMaximo">Precio Maximo:</label>
	<input type="text" id="precioMaximo" name="precioMaximo" placeholder="Escribe el precio maximo de la propiedad" maxlength="80" v-model="precioMaximo">
    
    <label for="comision1">Comision1:</label>
	<input type="text" id="comision1" name="comision1" placeholder="Escribe la comision de la propiedad" maxlength="80" v-model="comision1">

    <label for="ganancia1">Ganancia1:</label>
	<input type="text" id="ganancia1" name="ganancia1" placeholder="Escribe la ganancia de la propiedad" maxlength="80" v-model="ganancia1">
    
    <label for="comision2">Comision2:</label>
	<input type="text" id="comision2" name="comision2" placeholder="Escribe la comision de la propiedad" maxlength="80" v-model="comision2">

    <label for="ganancia2">Ganancia2:</label>
	<input type="text" id="ganancia2" name="ganancia2" placeholder="Escribe la ganancia de la propiedad" maxlength="80" v-model="ganancia2">
    </section>

    <!-- ######### seccion de la disponibilidad y exclusividad ######## -->
    <Section>
    <h3>Disponibilidad y exclusividad</h3>
    <select name="tipoDisponibilidad" id="tipoDisponibilidad" v-model="tipoDisponibilidad">
        <option value="Disponibilidad">Disponibilidad</option>
        <option value="Exclusividad">Exclusividad</option>
    </select>    
    </Section>
    <!-- ######### seccion de la transaccion de la propiedad ######## -->
    <section>
    <h3>Información de la transacción de la propiedad</h3>
    <label for="empresa">Empresa:</label>
    <input type="text" id="empresa" name="empresa" maxlength="60" v-model="empresa">

    <label for="agente">Agente:</label>
    <input type="text" id="agente" name="agente" maxlength="50" v-model="agente">

    <label for="propietario">Propietario:</label>
    <input type="text" id="propietario" name="propietario" maxlength="80" v-model="propietario">

    <label for="claveCastratal">Clave Catastral:</label>
    <input type="text" id="claveCastratal" name="claveCastratal" maxlength="30" v-model="claveCastratal">

    <label for="lote">Lote:</label>
    <input type="text" id="lote" name="lote" maxlength="30" v-model="lote">

    <label for="manzana">Manzana:</label>
    <input type="text" id="manzana" name="manzana" maxlength="30" v-model="manzana">

    <label for="cuentaAgua">Cuenta de Agua:</label>
    <input type="checkbox" id="cuentaAgua" name="cuentaAgua" v-model="cuentaAgua">

    <label for="ocultarDir">Ocultar Dirección:</label>
	<input type="checkbox" id="ocultarDir" name="ocultarDir" v-model="ocultarDir">

    <label for="aceptaInfonavid">Acepta Infonavit:</label>
	<input type="checkbox" id="aceptaInfonavid" name="aceptaInfonavid" v-model="aceptaInfonavid">

    <label for="aceptaFovisste">Acepta Fovisste:</label>
	<input type="checkbox" id="aceptaFovisste" name="aceptaFovisste" v-model="aceptaFovisste">

    <label for="autosEst">Autos Estacionados:</label>
    <input type="number" id="autosEst" name="autosEst" min="0" max="10" v-model="autosEst">

    <label for="autosIndep">Autos Independientes:</label>
    <input type="number" id="autosIndep" name="autosIndep" min="0" max="10" v-model="autosIndep">

    <label for="estacionamiento">Estacionamiento:</label>
    <input type="text" id="estacionamiento" name="estacionamiento" maxlength="30" v-model="estacionamiento">

    <label for="cocheraElectrica">Cochera Eléctrica:</label>
    <input type="text" id="cocheraElectrica" name="cocheraElectrica" v-model="cocheraElectrica">

    <label for="patio">Patio:</label>
    <input type="text" id="patio" name="patio" maxlength="30" v-model="patio">

    <label for="asador">Asador:</label>
    <input type="text" id="asador" name="asador" maxlength="70" v-model="asador">

    <label for="fuentes">Fuentes:</label>
    <input type="text" id="fuentes" name="fuentes" maxlength="90" v-model="fuentes">

    <label for="jacuzzi">Jacuzzi:</label>
    <input type="text" id="jacuzzi" name="jacuzzi" maxlength="120" v-model="jacuzzi">

    <label for="alberca">Alberca:</label>
    <input type="text" id="alberca" name="alberca" maxlength="70" v-model="alberca">

    <label for="jardin">Jardín:</label>
    <input type="text" id="jardin" name="jardin" maxlength="30" v-model="jardin">

    <label for="bodega">Bodega:</label>
    <input type="text" id="bodega" name="bodega" maxlength="50" v-model="bodega">

    <label for="cisterna">Cisterna:</label>
    <input type="text" id="cisterna" name="cisterna" maxlength="45" v-model="cisterna">

    <label for="tinaco">Tinaco:</label>
    <input type="text" id="tinaco" name="tinaco" maxlength="45" v-model="tinaco">

    <label for="acCentral">Aire Central:</label>
    <input type="checkbox" id="acCentral" name="acCentral" v-model="acCentral">

    <label for="proteccionVentana">Protección de Ventana:</label>
    <input type="checkbox" id="proteccionVentana" name="proteccionVentana" v-model="proteccionVentana">

    <label for="persianaCortina">Persiana Cortina:</label>
    <input type="checkbox" id="persianaCortina" name="persianaCortina" v-model="persianaCortina">

    <label for="hidroneumatico">Hidroneumático:</label>
    <input type="checkbox" id="hidroneumatico" name="hidroneumatico" v-model="hidroneumatico">

    <label for="patioEncementado">Patio Encementado:</label>
    <input type="checkbox" id="patioEncementado" name="patioEncementado" v-model="pisoEncementado">

    <label for="cocinaIntegral">Cocina integral:</label>
    <input type="text" id="cocinaIntegral" name="cocinaIntegral" maxlength="45" v-model="CocinaIntegral">

    <label for="amueblado">Amueblado:</label>
    <input type="checkbox" id="amueblado" name="amueblado" v-model="amueblado">

    <label for="piso1">Piso 1:</label>
    <input type="text" id="piso1" name="piso1" maxlength="30" v-model="piso1">

    <label for="piso2">Piso 2:</label>
    <input type="text" id="piso2" name="p1iso2" maxlength="30"v-model="piso2">

    <label for="piso3">Piso 3:</label>
    <input type="text" id="piso3" name="piso3" maxlength="30"v-model="piso3">

    <label for="alarma">Alarma:</label>
    <input type="checkbox" id="alarma" name="alarma" v-model="alarma">

    <label for="urlGoogleMap">URL Google Maps:</label>
    <input type="text" id="urlGoogleMap" name="urlGoogleMap" maxlength="150" v-model="urlGoogleMap">

    <label for="vitropiso">Tipo de Vitropiso:</label>
    <input type="text" id="vitropiso" name="vitropiso" maxlength="80" v-model="vitropiso">

    <label for="closet">Closet:</label>
    <input type="text" id="closet" name="closet" maxlength="30" v-model="closet">

    <label for="barda">Barda:</label>
    <input type="text" id="barda" name="barda" maxlength="30" v-model="barda">

    <label for="equipada">Equipada:</label>
    <input type="text" id="equipada" name="equipada" maxlength="30" v-model="equipada">
    </section>
        
    <!-- ######### seccion de la ubicacion ######## -->
    <section>
    <h3>Ubicación</h3>      
    <label for="pais">País:</label>
    <input type="text" id="pais" name="pais" maxlength="30" v-model="pais">

    <label for="estado">Estado:</label>
    <input type="text" id="estado" name="estado"  required maxlength="30" v-model="estado">

    <label for="municipio">Municipio:</label>
    <input type="text" id="municipio" name="municipio"  required maxlength="30" v-model="municipio">

    <label for="ciudad">Ciudad:</label>
    <input type="text" id="ciudad" name="ciudad"  required maxlength="30" v-model="ciudad">

    <label for="colonia">Colonia:</label>
    <input type="text" id="colonia" name="colonia"  required maxlength="30" v-model="colonia">

    <label for="codigoPostal">Código Postal:</label>
    <input type="text" id="codigoPostal" name="codigoPostal"  required maxlength="30" v-model="codigoPostal">

    <label for="calle">Calle:</label>
    <input type="text" id="calle" name="calle"  required maxlength="30" v-model="calle">

    <label for="numExterior">Número Exterior:</label>
    <input type="text" id="numExterior" name="numExterior"  required maxlength="30" v-model="numExterior">

    <label for="numInterior">Número Interior:</label>
    <input type="text" id="numInterior" name="numInterior"  required maxlength="30" v-model="numInteriror">

    <label for="entreCalle1">Entre calle 1:</label>
    <input type="text" id="entreCalle1" name="entreCalle1"  required maxlength="50" v-model="entreCalle1">

    <label for="entreCalle2">Entre calle 2:</label>
    <input type="text" id="entreCalle2" name="entreCalle2"  required maxlength="50" v-model="entreCalle2">

    <label for="nombreComplejo">Nombre Complejo:</label>
    <input type="text" id="nombreComplejo" name="nombreComplejo"  required maxlength="60" v-model="nombreComplejo">
    </section>

    <!-- ######### seccion de la imagen ######## -->
    <section>
    <label for="imagen">Ingrese las imagenes de la vivienda:</label>
    <input type="file" id="imagen" name="imagen" accept="image/png, image/jpeg" multiple />
    </section>

    <button type="summit" class="button-primary">Create</button>

</form>
</body>
</template>
<script>
import axios from 'axios';
    export default{
        name:"CreateForm",
    data: function(){
        return{
            proprieties:[],
        }
   },
   methods:{
        addPropriety(){
            let json = {
                "fechaInicio": this.fechaInicio,
                "fechaTermino": this.fechaTermino,
                "empresa": this.empresa,
                "agente": this.agente,
                "ocultarDir": this.ocultarDir,
                "exclusivo": this.exclusivo,
                "titulo": this.titulo,
                "comentario": this.comentario,
                "tipoVivienda": this.tipoVivienda,
                "usoActual": this.usoActual,
                "usoPermitido": this.usoPermitido,
                "condicionFisica": this.condicionFisica,
                "precioVenta": this.precioVenta,
                "precioRenta": this.precioRenta,
                "precioMinimo": this.precioMinimo,
                "precioPromedio": this.precioPromedio,
                "precioMaximo": this.precioMaximo,
                "comision1": this.comision1,
                "ganancia1": this.ganancia1,
                "comision2": this.comision2,
                "ganancia2": this.ganancia2,
                "disponibilidad": this.disponibilidad,
                "claseInmueble": this.claseInmueble,
                "numeroFrentes": this.numeroFrentes,
                "medidaTerreno": this.medidaTerreno,
                "m2Terreno": this.m2Terreno,
                "construccionN1": this.construccionN1,
                "construccionN2": this.construccionN2,
                "construccionN3": this.construccionN3,
                "gravamen": this.gravamen,
                "valorGravamen": this.valorGravamen,
                "valorSegunAvaluo": this.valorSegunAvaluo,
                "operacion": this.operacion,
                "condicionPago": this.condicionPago,
                "aceptaInfonavit": this.aceptaInfonavit,
                "aceptaFovisste": this.aceptaFovisste,
                "propietario": this.propietario,
                "claveCastratal": this.claveCastratal,
                "lote": this.lote,
                "manzana": this.manzana,
                "cuentaAgua": this.cuentaAgua,
                "autosEst": this.autosEst,
                "autosIndep": this.autosIndep,
                "estacionamiento": this.estacionamiento,
                "cocheraElectrica": this.cocheraElectrica,
                "patio": this.patio,
                "asador": this.asador,
                "fuentes": this.fuentes,
                "jacuzzi": this.jacuzzi,
                "alberca": this.alberca,
                "jardin": this.jardin,
                "bodega": this.bodega,
                "cisterna": this.cisterna,
                "tinaco": this.tinaco,
                "acCentral": this.acCentral,
                "proteccionVentana": this.proteccionVentana,
                "persianaCortina": this.persianaCortina,
                "hidroneumatico": this.hidroneumatico,
                "amueblado": this.amueblado,
                "piso1": this.piso1,
                "piso2": this.piso2,
                "piso3": this.piso3,
                "alarma": this.alarma,
                "uriGoogleMaps": this.uriGoogleMaps,
                "cocinaIntegral": this.cocinaIntegral,
                "vitropiso": this.vitropiso,
                "closet": this.closet,
                "barda": this.barda,
                "patioEncementado": this.patioEncementado,
                "equipada": this.equipada,
                "pais": this.pais,
                "estado": this.estado,
                "municipio": this.municipio,
                "ciudad": this.ciudad,
                "colonia": this.colonia,
                "codigoPostal": this.codigoPostal,
                "calle": this.calle,
                "numExterior": this.numExterior,
                "numInterior": this.numInterior,
                "entreCalle1": this.entreCalle1,
                "entreCalle2": this.entreCalle2,
                "nombreComplejo": this.nombreComplejo,
                "escrituracion": this.escrituracion,
                "avaluo": this.avaluo,
                "impuestos": this.impuestos,
                "otros": this.otros,
                "total": this.total,
                "imagen": this.imagen               
            }
        }
    },
}
</script>
<style scoped>
body {
    margin-top: 20px;
    font-family: Arial, sans-serif;
}

form {
    width: 90%;
    max-width: 600px; /* Limitamos el ancho máximo del formulario */
    margin: 0 auto;
}

section {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
textarea,
select,
input[type="date"] {
    width: calc(100% - 12px);
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
}

input[type="submit"]:hover {
    background-color: #45a049;
}

.decoration-line {
  height: 40px; /* Grosor de la línea */
  width: 100%; /* Ancho completo */
  background-color: #093b59; /* Color azul */
}

</style>